/**
 * SYNAPSE HELIOS ID - 3D Cycloid Wireframe Torus Sphere Canvas
 */
function initSpirographCanvas() {
  const canvas = document.getElementById('spirograph-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let rot = 0;

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
    const maxR = Math.min(w, h) * 0.42;

    ctx.clearRect(0, 0, w, h);
    ctx.save();
    ctx.translate(cx, cy);
    rot += 0.005;

    const count = 36;
    for (let i = 0; i < count; i++) {
      const angle = (i * Math.PI / count) + rot;
      ctx.save();
      ctx.rotate(angle);
      
      ctx.beginPath();
      // Draw an ellipse with varying width forming a 3D wireframe torus
      ctx.ellipse(0, 0, maxR, maxR * 0.38, 0, 0, Math.PI * 2);
      const isCyan = (i % 4 === 0);
      ctx.strokeStyle = isCyan 
        ? 'rgba(0, 243, 255, 0.5)' 
        : ((i % 2 === 0) ? 'rgba(255, 255, 255, 0.35)' : 'rgba(255, 255, 255, 0.12)');
      ctx.lineWidth = isCyan ? 1.5 * window.devicePixelRatio : 0.85 * window.devicePixelRatio;
      ctx.stroke();

      ctx.restore();
    }

    ctx.restore();
    requestAnimationFrame(draw);
  }
  draw();
}
