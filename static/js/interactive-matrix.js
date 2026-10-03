/**
 * SYNAPSE HELIOS ID - Interactive AI Taxonomy & Architectural Matrix Engine
 * Fetches from /api/ai-types & /api/languages and renders interactive views
 */

let allTaxonomyData = [];
let allLanguagesData = [];
let currentCategoryFilter = 'all';

async function fetchTaxonomyData() {
  try {
    const res = await fetch('/api/ai-types');
    if (res.ok) {
      const data = await res.json();
      allTaxonomyData = data.categories || [];
      renderTaxonomyCards();
    }
  } catch (err) {
    console.error("Gagal memuat taksonomi AI:", err);
  }
}

async function fetchLanguagesData() {
  try {
    const res = await fetch('/api/languages');
    if (res.ok) {
      const data = await res.json();
      allLanguagesData = data.languages || [];
      renderLanguageCards();
    }
  } catch (err) {
    console.error("Gagal memuat data bahasa komputasi:", err);
  }
}

function filterTaxonomy(catId, btnElement) {
  currentCategoryFilter = catId;
  const buttons = document.querySelectorAll('.taxonomy-filter-btn');
  buttons.forEach(b => {
    b.className = "taxonomy-filter-btn px-4 py-2 rounded-full border border-neutral-800 bg-[#0d0d0d] text-silver text-xs font-mono hover:text-white hover:border-neutral-600 transition-all";
  });
  if (btnElement) {
    btnElement.className = "taxonomy-filter-btn px-4 py-2 rounded-full border border-cyan-400 bg-cyan-950/50 text-cyan-300 text-xs font-mono font-bold shadow-[0_0_12px_rgba(0,243,255,0.25)] transition-all";
  }
  renderTaxonomyCards();
}

function searchTaxonomy() {
  const query = document.getElementById('taxonomy-search-input')?.value.toLowerCase() || '';
  renderTaxonomyCards(query);
}

function renderTaxonomyCards(searchQuery = '') {
  const container = document.getElementById('taxonomy-cards-container');
  if (!container) return;

  let filteredCategories = allTaxonomyData;
  if (currentCategoryFilter !== 'all') {
    filteredCategories = allTaxonomyData.filter(c => c.id === currentCategoryFilter);
  }

  let html = '';

  filteredCategories.forEach(category => {
    category.items.forEach(item => {
      // Check search match
      if (searchQuery) {
        const matchTitle = item.title.toLowerCase().includes(searchQuery);
        const matchDesc = item.description.toLowerCase().includes(searchQuery);
        const matchPioneers = item.pioneer_models.some(m => m.toLowerCase().includes(searchQuery));
        const matchCategory = category.name.toLowerCase().includes(searchQuery);
        if (!matchTitle && !matchDesc && !matchPioneers && !matchCategory) {
          return;
        }
      }

      const benchmarksList = item.benchmarks.map(b => `
        <div class="flex items-center justify-between text-[11px] font-mono py-1 border-b border-neutral-800/60">
          <span class="text-silver">${b.name}</span>
          <span class="text-cyan-400 font-bold">${b.score}</span>
        </div>
      `).join('');

      const pioneerBadges = item.pioneer_models.map(p => `
        <span class="px-2 py-0.5 rounded bg-neutral-900 border border-neutral-800 text-[10px] font-mono text-neutral-300">${p}</span>
      `).join('');

      html += `
        <div class="relative border border-[#222] rounded-xl bg-[#090909] p-6 sm:p-8 flex flex-col justify-between group hover:border-cyan-400/60 transition-all duration-300">
          <div class="crosshair-corner -top-1 -left-1"></div>
          <div class="crosshair-corner -top-1 -right-1"></div>
          
          <div>
            <!-- Header Meta -->
            <div class="flex items-center justify-between mb-4">
              <span class="font-mono text-xs text-neutral-500 font-bold tracking-widest uppercase">
                ${category.numeral} // ${category.english_name.toUpperCase()}
              </span>
              <span class="px-2.5 py-0.5 rounded-full border border-cyan-400/40 bg-cyan-950/30 text-cyan-300 font-mono text-[9px] font-bold tracking-wider">
                ${item.badge}
              </span>
            </div>

            <!-- Title & Tagline -->
            <h3 class="font-headline font-bold text-xl sm:text-2xl text-white mb-2 group-hover:text-cyan-300 transition-colors">
              ${item.title}
            </h3>
            <p class="text-cyan-400 font-mono text-xs mb-4">
              ${item.tagline}
            </p>

            <p class="text-silver text-xs sm:text-sm font-sans leading-relaxed mb-6">
              ${item.description}
            </p>

            <!-- Benchmark Snapshot -->
            <div class="bg-black/60 rounded-lg p-3 border border-neutral-800/80 mb-6">
              <div class="text-[10px] font-mono text-neutral-400 uppercase tracking-wider mb-2 font-semibold">
                SOTA BENCHMARK SNAPSHOT
              </div>
              <div class="space-y-1">
                ${benchmarksList}
              </div>
            </div>

            <!-- Pioneer Models Badges -->
            <div class="mb-6">
              <div class="text-[10px] font-mono text-neutral-500 uppercase tracking-wider mb-2">MODEL PIONIR:</div>
              <div class="flex flex-wrap gap-1.5">
                ${pioneerBadges}
              </div>
            </div>
          </div>

          <!-- Bottom Action -->
          <div class="pt-4 border-t border-[#1a1a1a] flex items-center justify-between">
            <span class="text-[11px] font-mono text-neutral-500">
              KOMPLEKSITAS: <span class="text-white">${item.computational_complexity.split(' ')[0]}</span>
            </span>
            <button 
              onclick="openDetailModal('${item.id}')" 
              class="px-4 py-1.5 rounded-full border border-white/30 hover:border-white bg-white/5 hover:bg-white hover:text-black font-mono text-xs tracking-wider uppercase transition-all flex items-center gap-1.5"
            >
              <span>Bedah Arsitektur</span>
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </button>
          </div>

          <div class="crosshair-corner -bottom-1 -left-1"></div>
          <div class="crosshair-corner -bottom-1 -right-1"></div>
        </div>
      `;
    });
  });

  if (html === '') {
    container.innerHTML = `
      <div class="col-span-full text-center py-16 font-mono text-silver">
        [TIDAK ADA DATA] Tidak ada jenis AI yang sesuai dengan kata kunci '${searchQuery}'.
      </div>
    `;
  } else {
    container.innerHTML = html;
  }
}

function openDetailModal(typeId) {
  let targetItem = null;
  let targetCat = null;
  for (let cat of allTaxonomyData) {
    for (let item of cat.items) {
      if (item.id === typeId) {
        targetItem = item;
        targetCat = cat;
        break;
      }
    }
  }
  if (!targetItem) return;

  const modal = document.getElementById('taxonomy-modal');
  const title = document.getElementById('modal-title');
  const badge = document.getElementById('modal-badge');
  const body = document.getElementById('modal-body');
  if (!modal || !body) return;

  title.innerText = targetItem.title;
  badge.innerText = targetItem.badge;

  const mechanismsHtml = targetItem.key_mechanisms.map(m => `
    <li class="flex items-start gap-2 text-xs sm:text-sm text-silver font-sans">
      <span class="text-cyan-400 font-mono mt-0.5">▶</span>
      <span>${m}</span>
    </li>
  `).join('');

  const featuresHtml = targetItem.architectural_features.map(f => `
    <div class="border border-neutral-800 rounded-lg p-3 bg-black/60">
      <div class="text-xs font-mono font-bold text-white mb-1">${f.title}</div>
      <div class="text-xs font-sans text-silver mb-2">${f.detail}</div>
      ${f.code_or_formula ? `<pre class="text-[11px] font-mono text-cyan-300 bg-neutral-900/80 p-2 rounded border border-neutral-800 overflow-x-auto"><code>${f.code_or_formula}</code></pre>` : ''}
    </div>
  `).join('');

  const benchmarksFull = targetItem.benchmarks.map(b => `
    <div class="p-3 bg-neutral-900/50 border border-neutral-800 rounded">
      <div class="flex justify-between items-center mb-1">
        <span class="font-mono text-xs font-bold text-white">${b.name}</span>
        <span class="font-mono text-xs font-bold text-cyan-400">${b.score}</span>
      </div>
      <div class="text-[11px] text-neutral-400 font-sans mb-1">${b.description}</div>
      <div class="text-[10px] font-mono text-neutral-500">Baseline Komparasi: <span class="text-neutral-300">${b.baseline || 'N/A'}</span></div>
    </div>
  `).join('');

  const useCasesHtml = targetItem.use_cases.map(u => `
    <div class="px-2.5 py-1 rounded bg-[#161616] border border-neutral-800 text-xs font-mono text-neutral-300">
      ⚡ ${u}
    </div>
  `).join('');

  body.innerHTML = `
    <div class="space-y-6">
      <div>
        <div class="text-[11px] font-mono text-neutral-500 uppercase tracking-widest mb-1">KATEGORI: ${targetCat.name}</div>
        <p class="text-silver text-xs sm:text-sm leading-relaxed">${targetItem.deep_dive.replace(/\n/g, '<br/>')}</p>
      </div>

      <div>
        <h4 class="font-headline font-bold text-sm text-white uppercase tracking-wider mb-3 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
          Mekanisme Kunci & Paradigma Komputasi
        </h4>
        <ul class="space-y-2">
          ${mechanismsHtml}
        </ul>
      </div>

      <div>
        <h4 class="font-headline font-bold text-sm text-white uppercase tracking-wider mb-3 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
          Formulasi Arsitektural & Persamaan Matematika
        </h4>
        <div class="space-y-3">
          ${featuresHtml}
        </div>
      </div>

      <div>
        <h4 class="font-headline font-bold text-sm text-white uppercase tracking-wider mb-3 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-yellow-400"></span>
          Tolok Ukur Evaluasi SOTA (Benchmarks)
        </h4>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          ${benchmarksFull}
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-4 border-t border-neutral-800 font-mono text-xs">
        <div>
          <span class="text-neutral-500 block mb-1">KOMPLEKSITAS KOMPUTASI:</span>
          <span class="text-white">${targetItem.computational_complexity}</span>
        </div>
        <div>
          <span class="text-neutral-500 block mb-1">AFINITAS PERANGKAT KERAS:</span>
          <span class="text-cyan-400">${targetItem.hardware_affinity}</span>
        </div>
      </div>

      <div>
        <h4 class="font-headline font-bold text-sm text-white uppercase tracking-wider mb-2">Kasus Penggunaan Industri Spesifik</h4>
        <div class="flex flex-wrap gap-2">
          ${useCasesHtml}
        </div>
      </div>

      <div class="p-3 bg-red-950/20 border border-red-900/50 rounded-lg text-xs font-mono text-red-300">
        <span class="font-bold uppercase tracking-wider">[RISIKO & ALIGNMENT SAFETY]:</span>
        <span class="text-neutral-300 ml-1 font-sans">${targetItem.risk_and_alignment}</span>
      </div>
    </div>
  `;

  modal.classList.remove('hidden');
  document.body.classList.add('overflow-hidden');
}

function closeDetailModal() {
  const modal = document.getElementById('taxonomy-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
  }
}

function renderLanguageCards() {
  const container = document.getElementById('languages-cards-container');
  if (!container) return;

  let html = '';
  allLanguagesData.forEach((lang, index) => {
    const metricsHtml = Object.entries(lang.metrics).map(([key, val]) => `
      <div class="flex justify-between items-center text-[11px] font-mono py-1 border-b border-neutral-800/50">
        <span class="text-neutral-400">${key}:</span>
        <span class="text-cyan-300 font-semibold">${val}</span>
      </div>
    `).join('');

    const useCasesList = lang.specific_use_cases.map(u => `
      <li class="flex items-start gap-1.5 text-xs text-silver">
        <span class="text-cyan-400 font-mono">▪</span>
        <span>${u}</span>
      </li>
    `).join('');

    html += `
      <div class="lang-card relative border border-[#222] rounded-xl bg-black p-6 sm:p-8 flex flex-col justify-between group hover:border-cyan-400/80 transition-all duration-300">
        <div class="crosshair-corner -top-1 -left-1"></div>
        <div class="crosshair-corner -top-1 -right-1"></div>
        
        <div>
          <!-- Top Row: Icon + Performance Tier -->
          <div class="flex items-start justify-between mb-6">
            <div class="w-14 h-14 p-2 rounded-xl bg-[#111] border border-neutral-800 flex items-center justify-center">
              <img 
                src="${lang.logo_url}" 
                alt="${lang.name} Logo" 
                class="lang-logo w-10 h-10 object-contain"
                onerror="this.src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg'"
              />
            </div>
            <div class="text-right">
              <span class="px-2.5 py-1 rounded-full border border-neutral-800 bg-[#121212] text-neutral-300 font-mono text-[10px] font-semibold tracking-wider uppercase block mb-1">
                ${lang.version_standard}
              </span>
              <span class="font-mono text-[9px] text-cyan-400 tracking-wider uppercase">
                ${lang.performance_tier.split(' - ')[0]}
              </span>
            </div>
          </div>

          <!-- Title & Role -->
          <h3 class="font-headline font-bold text-2xl text-white mb-2 group-hover:text-cyan-300 transition-colors">
            ${lang.name}
          </h3>
          <div class="text-xs font-mono text-cyan-400 mb-4 leading-snug">
            ${lang.role_indonesian}
          </div>

          <!-- Blueprint Metrik Box -->
          <div class="bg-[#0b0b0b] rounded-lg p-3.5 border border-neutral-800/80 mb-5">
            <div class="text-[10px] font-mono text-neutral-500 uppercase tracking-widest mb-2 font-bold">
              METRIK EFISIENSI SISTEM
            </div>
            <div class="space-y-1">
              ${metricsHtml}
            </div>
          </div>

          <!-- Ekosistem Utama -->
          <div class="mb-4">
            <div class="text-[10px] font-mono text-neutral-500 uppercase tracking-wider mb-1 font-semibold">EKOSISTEM UTAMA:</div>
            <div class="text-xs font-mono text-neutral-300 bg-neutral-900/60 p-2 rounded border border-neutral-800/60 leading-relaxed">
              ${lang.primary_ecosystem}
            </div>
          </div>

          <!-- Kasus Penggunaan Spesifik -->
          <div class="mb-6">
            <div class="text-[10px] font-mono text-neutral-500 uppercase tracking-wider mb-1 font-semibold">KASUS PENGGUNAAN SPESIFIK:</div>
            <ul class="space-y-1.5">
              ${useCasesList}
            </ul>
          </div>
        </div>

        <!-- Code Snippet Button -->
        <div class="pt-4 border-t border-[#1a1a1a] flex items-center justify-between">
          <span class="text-[10px] font-mono text-neutral-500">RUNTIME: ${lang.runtime_environment.split(',')[0]}</span>
          <button 
            onclick="openCodeModal('${lang.id}')" 
            class="px-4 py-1.5 rounded-full border border-cyan-400/40 hover:border-cyan-400 bg-cyan-950/20 hover:bg-cyan-950/60 text-cyan-300 font-mono text-xs font-semibold tracking-wider uppercase transition-all"
          >
            Lihat Kode ↵
          </button>
        </div>

        <div class="crosshair-corner -bottom-1 -left-1"></div>
        <div class="crosshair-corner -bottom-1 -right-1"></div>
      </div>
    `;
  });

  container.innerHTML = html;
}

function openCodeModal(langId) {
  const lang = allLanguagesData.find(l => l.id === langId);
  if (!lang) return;

  const modal = document.getElementById('code-modal');
  const title = document.getElementById('code-modal-title');
  const body = document.getElementById('code-modal-body');
  if (!modal || !body) return;

  title.innerText = `${lang.name} // ${lang.code_example_title}`;
  body.innerHTML = `
    <div class="space-y-4">
      <div class="text-xs font-mono text-neutral-400">
        ${lang.architectural_role}
      </div>
      <div class="relative rounded-lg overflow-hidden border border-neutral-800 bg-[#080808]">
        <div class="bg-[#141414] px-4 py-2 text-xs font-mono text-silver flex justify-between items-center border-b border-neutral-800">
          <span class="text-cyan-400 font-bold uppercase">${lang.name} SOURCE</span>
          <button 
            onclick="navigator.clipboard.writeText(document.getElementById('code-raw-snippet').innerText); showToast('Kode disalin ke clipboard');" 
            class="px-2.5 py-1 rounded bg-neutral-800 hover:bg-neutral-700 text-white transition-colors"
          >
            SALIN KODE
          </button>
        </div>
        <pre id="code-raw-snippet" class="p-4 text-cyan-300 font-mono text-xs overflow-x-auto leading-relaxed whitespace-pre"><code>${escapeHtml(lang.code_example)}</code></pre>
      </div>
      <div class="font-mono text-xs text-neutral-500 flex items-center justify-between">
        <span>RUNTIME ENV: ${lang.runtime_environment}</span>
        <span>STANDARD: ${lang.version_standard}</span>
      </div>
    </div>
  `;

  modal.classList.remove('hidden');
  document.body.classList.add('overflow-hidden');
}

function closeCodeModal() {
  const modal = document.getElementById('code-modal');
  if (modal) {
    modal.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
  }
}

// Initial boot
window.addEventListener('DOMContentLoaded', () => {
  fetchTaxonomyData();
  fetchLanguagesData();
});
