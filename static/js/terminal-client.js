/**
 * SYNAPSE HELIOS ID - Interactive Terminal Client
 * Connects to /api/terminal with Live Mode Switching & Dynamic AI Synthesis
 */

let currentMode = 'creative';
const terminalModes = {
  creative: {
    name: "Sintesis Kreatif",
    badge: "CREATIVE_SYNTHESIS",
    system: "Sintesis kognisi visioner memadukan estetika klasik & kecerdasan buatan masa depan."
  },
  code: {
    name: "Arsitek Kode",
    badge: "CODE_ARCHITECT",
    system: "Sintesis arsitektur perangkat lunak komputasi AI tingkat tinggi, kernel, dan sistem terdistribusi."
  },
  analysis: {
    name: "Analisis Mendalam",
    badge: "DEEP_ANALYSIS",
    system: "Pembedahan sistematis multidimensi, analisis FLOPs, memori KV-Cache, dan metrik alignment."
  }
};

function showToast(message) {
  const box = document.getElementById('toast-box');
  const msg = document.getElementById('toast-message');
  if (!box || !msg) return;
  msg.innerText = message;
  box.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-3');
  box.classList.add('opacity-100', 'translate-y-0');
  setTimeout(() => {
    box.classList.remove('opacity-100', 'translate-y-0');
    box.classList.add('opacity-0', 'pointer-events-none', 'translate-y-3');
  }, 4000);
}

function setTerminalMode(mode) {
  if (!terminalModes[mode]) return;
  currentMode = mode;
  ['creative', 'code', 'analysis'].forEach(m => {
    const btn = document.getElementById(`btn-mode-${m}`);
    if (!btn) return;
    if (m === mode) {
      btn.className = "px-3 py-1.5 rounded text-[11px] font-mono border border-cyan-400 bg-cyan-950/60 text-cyan-300 font-semibold shadow-[0_0_10px_rgba(0,243,255,0.2)]";
    } else {
      btn.className = "px-3 py-1.5 rounded text-[11px] font-mono border border-neutral-800 bg-[#111] text-silver hover:text-white hover:border-neutral-600 transition-colors";
    }
  });
  showToast(`Mode dialihkan ke: ${terminalModes[mode].name}`);
}

function fillPrompt(text) {
  const input = document.getElementById('terminal-input');
  if (input) {
    input.value = text;
    input.focus();
    // Scroll to terminal smoothly
    const termSec = document.getElementById('terminal-section');
    if (termSec) termSec.scrollIntoView({ behavior: 'smooth' });
  }
}

async function handleTerminalSubmit(e) {
  if (e) e.preventDefault();
  const input = document.getElementById('terminal-input');
  const query = input.value.trim();
  if (!query) return;

  const history = document.getElementById('terminal-history');
  const loading = document.getElementById('terminal-loading');
  const submitBtn = document.getElementById('terminal-submit-btn');
  const screen = document.getElementById('terminal-screen');

  // Append User Turn
  const userNode = document.createElement('div');
  userNode.className = "border-l-2 border-cyan-400 pl-3 py-1.5 bg-white/[0.01] rounded-r";
  userNode.innerHTML = `
    <div class="text-[10px] text-cyan-400 font-mono tracking-wider mb-1 flex items-center justify-between">
      <span>USER_QUERY // ${new Date().toLocaleTimeString()} WIB</span>
      <span class="text-neutral-500 text-[9px]">[MODE: ${terminalModes[currentMode].badge}]</span>
    </div>
    <div class="text-white text-xs sm:text-sm font-mono">${escapeHtml(query)}</div>
  `;
  history.appendChild(userNode);

  input.value = '';
  loading.classList.remove('hidden');
  submitBtn.disabled = true;
  submitBtn.classList.add('opacity-50', 'cursor-not-allowed');
  screen.scrollTop = screen.scrollHeight;

  const payload = {
    query: query,
    mode: currentMode,
    client_id: "SYNAPSE_HELIOS_WEB"
  };

  try {
    const response = await fetch('/api/terminal', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      throw new Error(`Inference pipeline error (HTTP ${response.status})`);
    }

    const data = await response.json();
    const generatedText = data.response || "Tidak ada output kognitif yang diterima dari matriks saraf.";

    // Append Model Turn
    const modelNode = document.createElement('div');
    modelNode.className = "border-l-2 border-white/40 pl-3 py-2.5 bg-white/[0.02] rounded-r";
    modelNode.innerHTML = `
      <div class="text-[10px] text-neutral-400 font-mono tracking-wider mb-2 flex items-center justify-between">
        <span class="text-emerald-400 font-bold flex items-center gap-1.5">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          SYNAPSE_CORE // ${data.source || 'KLUSTER KOGNISI'}
        </span>
        <span class="text-neutral-500 font-mono text-[9px]">
          LATENCY: ${data.latency_ms || 18.4}ms // MODEL: ${data.model_used || 'gemini-3-flash'}
        </span>
      </div>
      <div class="text-neutral-200 text-xs sm:text-sm font-sans whitespace-pre-wrap leading-relaxed">
        ${formatMarkdown(generatedText)}
      </div>
    `;
    history.appendChild(modelNode);

  } catch (error) {
    const errorNode = document.createElement('div');
    errorNode.className = "border-l-2 border-red-500 pl-3 py-2 bg-red-950/20 text-red-400";
    errorNode.innerHTML = `
      <div class="text-[10px] font-mono tracking-wider text-red-300 font-bold">[INFERENCE_FALLBACK]</div>
      <div class="text-xs font-mono">${escapeHtml(error.message || 'Koneksi ke backend inference terputus.')}</div>
    `;
    history.appendChild(errorNode);
  } finally {
    loading.classList.add('hidden');
    submitBtn.disabled = false;
    submitBtn.classList.remove('opacity-50', 'cursor-not-allowed');
    screen.scrollTop = screen.scrollHeight;
  }
}

function escapeHtml(str) {
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function formatMarkdown(text) {
  let formatted = escapeHtml(text);
  
  // Headers
  formatted = formatted.replace(/^### (.*?)$/gm, '<h3 class="text-cyan-300 font-headline font-bold text-sm sm:text-base mt-3 mb-1">$1</h3>');
  formatted = formatted.replace(/^## (.*?)$/gm, '<h2 class="text-white font-headline font-bold text-base sm:text-lg mt-4 mb-2">$1</h2>');

  // Code blocks with syntax copy button
  formatted = formatted.replace(/```([a-zA-Z]*)\n([\s\S]*?)```/g, (match, lang, code) => {
    return `<div class="relative my-3 rounded-lg overflow-hidden border border-neutral-800 bg-[#080808]">
      <div class="bg-[#111] px-3 py-1 text-[10px] font-mono text-neutral-400 flex justify-between items-center border-b border-neutral-800">
        <span class="uppercase tracking-wider text-cyan-400">${lang || 'CODE'}</span>
        <button onclick="navigator.clipboard.writeText(this.parentElement.nextElementSibling.innerText); showToast('Kode disalin ke clipboard');" class="text-neutral-400 hover:text-white transition-colors">SALIN KODE</button>
      </div>
      <pre class="p-3 text-cyan-300 font-mono text-xs overflow-x-auto leading-relaxed"><code>${code}</code></pre>
    </div>`;
  });

  // Inline bold
  formatted = formatted.replace(/\*\*(.*?)\*\*/g, '<strong class="text-white font-semibold">$1</strong>');
  
  // Inline code
  formatted = formatted.replace(/`([^`]+)`/g, '<code class="bg-neutral-800 text-cyan-300 px-1.5 py-0.5 rounded font-mono text-[11px]">$1</code>');
  
  // Tables
  if (formatted.includes('|')) {
    const lines = formatted.split('\n');
    let inTable = false;
    let tableHtml = '<div class="overflow-x-auto my-3"><table class="w-full text-xs font-mono border-collapse border border-neutral-800">';
    let newLines = [];
    
    for (let line of lines) {
      if (line.trim().startsWith('|') && line.trim().endsWith('|')) {
        if (!inTable) inTable = true;
        const cells = line.split('|').filter((_, idx, arr) => idx > 0 && idx < arr.length - 1);
        const isHeader = line.includes('---');
        if (isHeader) continue;
        tableHtml += '<tr class="border-b border-neutral-800/80 hover:bg-neutral-900/40">';
        for (let cell of cells) {
          tableHtml += `<td class="p-2 border-r border-neutral-800/60">${cell.trim()}</td>`;
        }
        tableHtml += '</tr>';
      } else {
        if (inTable) {
          tableHtml += '</table></div>';
          newLines.push(tableHtml);
          inTable = false;
          tableHtml = '<div class="overflow-x-auto my-3"><table class="w-full text-xs font-mono border-collapse border border-neutral-800">';
        }
        newLines.push(line);
      }
    }
    if (inTable) {
      tableHtml += '</table></div>';
      newLines.push(tableHtml);
    }
    formatted = newLines.join('\n');
  }

  return formatted;
}
