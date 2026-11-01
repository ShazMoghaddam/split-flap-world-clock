// Split-Flap World Clock site: scales the live preview and builds the two-colour footer.

// The preview renders the clock at 1600 x 900 and scales it to the frame,
// so it looks like the real thing on a desktop screen at any width.
const screen = document.querySelector('.preview__screen');
const frame = document.querySelector('.preview__frame');
if (screen && frame) {
  const fit = () => {
    frame.style.transform = `scale(${screen.clientWidth / 1600})`;
  };
  fit();
  new ResizeObserver(fit).observe(screen);
}

// Footer: copy the content once more for the terracotta half. Each layer is
// clipped to its own triangle with ink that reads well on its colour.
// Screen readers and keyboards only meet the real content; the copy's
// links still work for a mouse or a tap on the terracotta side.
const layer = document.querySelector('.foot__layer');
if (layer) {
  const sun = layer.cloneNode(true);
  sun.classList.add('foot__layer--sun');
  sun.setAttribute('aria-hidden', 'true');
  sun.querySelectorAll('a, button, [tabindex]').forEach((el) => el.setAttribute('tabindex', '-1'));
  sun.querySelectorAll('[id]').forEach((el) => el.removeAttribute('id'));
  layer.after(sun);
}
