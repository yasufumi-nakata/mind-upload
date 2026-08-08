/* mind-upload.com — shared behavior for chapter pages */
(function () {
  // enable scroll-reveal styling only when JS runs (no-JS users see everything)
  document.documentElement.classList.add('js');

  // failsafe: reveal anything still hidden shortly after load (covers throttled
  // IntersectionObserver in background tabs and other edge cases)
  window.addEventListener('load', function () {
    setTimeout(function () {
      document.querySelectorAll('.reveal:not(.in)').forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) el.classList.add('in');
      });
    }, 1200);
  });
  // top reading-progress bar
  var progress = document.getElementById('progress');
  if (progress) {
    var onScroll = function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      progress.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
    };
    document.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // reveal on scroll
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

  // highlight current page in the global nav
  var path = location.pathname.replace(/\/index\.html$/, '/');
  document.querySelectorAll('.primary-nav a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === path || href === location.pathname) a.classList.add('active');
  });

  // animate meters / ladder fills when visible
  var mio = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.querySelectorAll('[data-fill]').forEach(function (f) {
          f.style.width = f.getAttribute('data-fill');
        });
        mio.unobserve(e.target);
      }
    });
  }, { threshold: 0.2 });
  document.querySelectorAll('.meters, .ladder').forEach(function (el) { mio.observe(el); });

  // mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') nav.classList.remove('open');
    });
  }
})();
