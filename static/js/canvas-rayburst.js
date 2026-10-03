/**
 * SYNAPSE HELIOS ID - Rayburst Geometric Sunburst Canvas
 */
function initRayburstCanvas() {
  const canvas = document.getElementById('rayburst-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let angleOffset = 0;

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
    const cx = w / 2;
    const cy = h / 2;
    const radius = Math.min(w, h) * 0.46;

    ctx.clearRect(0, 0, w, h);
    ctx.save();
    ctx.translate(cx, cy);

    const totalRays = 180;
    angleOffset += 0.0015;

    for (let i = 0; i < totalRays; i++) {
      const theta = (i * (Math.PI * 2) / totalRays) + angleOffset;
      const innerRadius = radius * 0.42;
      const outerRadius = radius * (0.92 + 0.08 * Math.sin(i * 0.2 + angleOffset * 4));

      const x1 = Math.cos(theta) * innerRadius;
      const y1 = Math.sin(theta) * innerRadius;
      const x2 = Math.cos(theta) * outerRadius;
      const y2 = Math.sin(theta) * outerRadius;

      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.strokeStyle = (i % 6 === 0) ? 'rgba(0, 243, 255, 0.55)' : 'rgba(255, 255, 255, 0.15)';
      ctx.lineWidth = (i % 6 === 0) ? 1.5 * window.devicePixelRatio : 0.75 * window.devicePixelRatio;
      ctx.stroke();
    }

    // Inner and outer concentric blueprint rings
    ctx.beginPath();
    ctx.arc(0, 0, radius * 0.42, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(0, 243, 255, 0.4)';
    ctx.lineWidth = 1 * window.devicePixelRatio;
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(0, 0, radius, 0, Math.PI * 2);
    ctx.setLineDash([4 * window.devicePixelRatio, 6 * window.devicePixelRatio]);
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.restore();
    requestAnimationFrame(draw);
  }
  draw();
}
