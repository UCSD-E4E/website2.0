(() => {
  const story = document.querySelector('[data-mangrove-story]');
  if (!story || !('IntersectionObserver' in window)) return;
  const graphic = story.querySelector('.mangrove-story__graphic img');
  const steps = [...story.querySelectorAll('.mangrove-story__step')];
  const wide = window.matchMedia('(min-width: 900px)');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let request = 0;
  let activeSource;
  let animation;

  function show(step) {
    const token = ++request;
    const image = new Image();
    image.onload = () => {
      if (token !== request || !wide.matches) return;
      graphic.src = image.src;
      if (activeSource !== image.src && !reducedMotion.matches && graphic.animate) {
        if (animation) animation.cancel();
        animation = graphic.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 250 });
      }
      activeSource = image.src;
      story.classList.add('is-enhanced');
    };
    image.onerror = () => {
      if (token === request) story.classList.remove('is-enhanced');
    };
    image.src = step.dataset.image;
  }

  function update() {
    if (!wide.matches) {
      ++request;
      story.classList.remove('is-enhanced');
      return;
    }
    const marker = window.innerHeight * 0.5;
    let current = steps[0];
    for (const step of steps) {
      if (step.getBoundingClientRect().top <= marker) current = step;
    }
    show(current);
  }
  const observer = new IntersectionObserver(update, { rootMargin: '-40% 0px -40% 0px' });
  steps.forEach(step => observer.observe(step));
  window.addEventListener('resize', update);
  update();
})();
