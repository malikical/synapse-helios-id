/**
 * SYNAPSE HELIOS ID - Mathematical Harmonic Moiré Wave Arc Canvas
 */
function initMoireArcCanvas() {
  const canvas = document.getElementById('moire-arc-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let t = 0;

  function resize() {
    const rect = canvas.getBoundingClientRect();
    if (rect.width === 0 || rect.height === 0) return;
    canvas.width = rect.width * window.devicePixelRatio;
    canvas.height = rect.height * window.devicePixelRatio;
  }
  window.addEventListener('resize', resize);
  resize();

  function draw() {
    const w = canvas.width;
    const h = canvas.height;
    if (w === 0 || h === 0) {
      requestAnimationFrame(draw);
      return;
    }
    ctx.clearRect(0, 0, w, h);
    t += 0.012;

    const lines = 46;
    const cx = w * 0.48;
    const cy = h * 0.95;

    for (let i = 0; i < lines; i++) {
      const rX = (w * 0.4) * (i / lines) + 10;
      const rY = (h * 0.82) * (i / lines) + Math.sin(t + i * 0.12) * 9;

      ctx.beginPath();
      ctx.ellipse(cx, cy, Math.max(5, rX), Math.max(5, rY), 0, Math.PI, 0);
      const isAccent = (i % 7 === 0);
      ctx.strokeStyle = isAccent 
        ? `rgba(0, 243, 255, ${0.3 + (i / lines) * 0.5})` 
        : `rgba(255, 255, 255, ${0.1 + (i / lines) * 0.35})`;
      ctx.lineWidth = isAccent ? 1.5 * window.devicePixelRatio : 1 * window.devicePixelRatio;
      ctx.stroke();
    }

    requestAnimationFrame(draw);
  }
  draw();
}
