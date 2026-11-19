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

  // Table of contents active highlight on scroll
  var tocLinks = document.querySelectorAll('.toc-box a');
  if (tocLinks.length) {
    var sections = [];
    tocLinks.forEach(function (a) {
      var id = a.getAttribute('href');
      if (id && id.charAt(0) === '#') {
        var el = document.querySelector(id);
        if (el) sections.push({ link: a, el: el });
      }
    });
    function onScroll() {
      var pos = window.scrollY + 140;
      var current = null;
      sections.forEach(function (s) {
        if (s.el.offsetTop <= pos) current = s;
      });
      tocLinks.forEach(function (a) {
        a.style.color = '';
        a.style.borderColor = '';
      });
      if (current) {
        current.link.style.color = 'var(--primary)';
        current.link.style.borderColor = 'var(--primary)';
      }
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
