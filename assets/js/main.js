// Bigloong - shared interactions
(function () {
  'use strict';

  // Mobile menu toggle
  var toggle = document.querySelector('.menu-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
    });
  }

  // Mobile dropdown toggles (items with a submenu)
  document.querySelectorAll('.has-drop > .nav-link').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 820) {
        e.preventDefault();
        link.parentElement.classList.toggle('open');
      }
    });
  });

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(function (q) {
    q.addEventListener('click', function () {
      var item = q.closest('.faq-item');
      var isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(function (openItem) {
        openItem.classList.remove('open');
      });
      if (!isOpen) item.classList.add('open');
    });
  });

  // Table of contents: smooth jump so the target heading lands on the first visible line,
  // plus active highlight on scroll.
  var tocLinks = document.querySelectorAll('.toc-box a');
  if (tocLinks.length) {
    // sticky header is 76px tall; keep this much space above the heading
    var NAV_OFFSET = 96;
    var sections = [];
    tocLinks.forEach(function (a) {
      var id = a.getAttribute('href');
      if (id && id.charAt(0) === '#') {
        var el = document.getElementById(id.substring(1));
        if (el) {
          sections.push({ link: a, el: el });
          a.addEventListener('click', function (e) {
            e.preventDefault();
            var top = el.getBoundingClientRect().top + window.pageYOffset - NAV_OFFSET;
            if (window.scrollTo) {
              window.scrollTo({ top: top, behavior: 'smooth' });
            } else {
              window.scrollTo(0, top);
            }
            if (history.replaceState) history.replaceState(null, '', id);
            else window.location.hash = id;
            setActive(a);
          });
        }
      }
    });
    function setActive(activeLink) {
      tocLinks.forEach(function (a) {
        a.style.color = '';
        a.style.borderColor = '';
        a.removeAttribute('data-active');
      });
      if (activeLink) {
        activeLink.style.color = 'var(--primary)';
        activeLink.style.borderColor = 'var(--primary)';
        activeLink.setAttribute('data-active', '1');
      }
    }
    function onScroll() {
      var pos = window.scrollY + NAV_OFFSET + 8;
      var current = null;
      sections.forEach(function (s) {
        if (s.el.getBoundingClientRect().top + window.pageYOffset <= pos) current = s;
      });
      // if scrolled to the very bottom, highlight the last item
      if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 2 && sections.length) {
        current = sections[sections.length - 1];
      }
      setActive(current ? current.link : null);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Contact form (mailto fallback) -> build a mailto link from fields
  var form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.querySelector('[name=name]').value.trim();
      var email = form.querySelector('[name=email]').value.trim();
      var subject = form.querySelector('[name=subject]').value.trim();
      var message = form.querySelector('[name=message]').value.trim();
      var body = 'Name: ' + name + '\nEmail: ' + email + '\n\n' + message;
      var href = 'mailto:contact@bigloong.net?subject=' + encodeURIComponent(subject || 'Website enquiry') + '&body=' + encodeURIComponent(body);
      window.location.href = href;
    });
  }
})();
