/**
 * MINAL INDUSTRES — CATALOG 2026
 * Interactive Behaviors — Fixed & Enhanced
 */
document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initScrollAnimations();
  initCatalogFilters();
  initFormHandling();
  initScrollToTop();
  initImageModal();
});

/* ─────────────────────────────────────────
   NAVIGATION — Sticky + Mobile Hamburger
───────────────────────────────────────── */
function initNavigation() {
  const nav       = document.getElementById('main-nav');
  const navToggle = document.getElementById('navToggle');
  const navLinks  = document.querySelector('.nav-links');
  const navItems  = document.querySelectorAll('.nav-link');

  // Always show dark nav (our cover is dark, so always scrolled-style)
  nav.classList.add('scrolled');

  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 10);
  });

  // Mobile hamburger
  if (navToggle) {
    navToggle.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      navToggle.classList.toggle('open', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });
  }

  // Close menu on nav link click
  navItems.forEach(item => {
    item.addEventListener('click', () => {
      navLinks.classList.remove('open');
      navToggle && navToggle.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  // Active section highlight
  const sections = document.querySelectorAll('section[id]');
  const onScroll = () => {
    let current = '';
    sections.forEach(sec => {
      if (window.scrollY >= sec.offsetTop - 120) current = sec.id;
    });
    navItems.forEach(item => {
      item.classList.toggle('active', item.getAttribute('href') === `#${current}`);
    });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* ─────────────────────────────────────────
   SCROLL ANIMATIONS — IntersectionObserver
───────────────────────────────────────── */
function initScrollAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-animated');
        observer.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

  // Only animate section-level elements (NOT product cards — they stay visible)
  document.querySelectorAll(
    '[data-animate="fade-up"], [data-animate="fade-left"], [data-animate="fade-right"], [data-animate="bespoke-card"]'
  ).forEach(el => observer.observe(el));
}

/* ─────────────────────────────────────────
   CATALOG FILTERS — Tab-based Filtering
───────────────────────────────────────── */
function initCatalogFilters() {
  const tabs   = document.querySelectorAll('.tab-btn');
  const blocks = document.querySelectorAll('.category-block');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => { t.classList.remove('active'); t.setAttribute('aria-selected', 'false'); });
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');

      const target = tab.getAttribute('data-category');
      blocks.forEach(block => {
        const match = target === 'all' || block.getAttribute('data-category') === target;
        block.style.display = match ? '' : 'none';
      });
    });
  });

  // Ensure all blocks are visible on load
  blocks.forEach(b => b.style.display = '');
}

/* ─────────────────────────────────────────
   FORM HANDLING
───────────────────────────────────────── */
function initFormHandling() {
  const form    = document.getElementById('inquiryForm');
  const toast   = document.getElementById('formToast');
  if (!form || !toast) return;

  // Pre-fill from bespoke CTA
  const bespokeBtn = document.getElementById('bespokeConsultBtn');
  if (bespokeBtn) {
    bespokeBtn.addEventListener('click', () => {
      const sel = document.getElementById('field-interest');
      if (sel) sel.value = 'bespoke';
    });
  }

  function showToast(msg) {
    toast.querySelector('span') && (toast.querySelector('span').textContent = msg);
    toast.classList.add('visible');
    setTimeout(() => toast.classList.remove('visible'), 5000);
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }

    const btn = document.getElementById('submitInquiryBtn');
    const orig = btn.innerHTML;
    btn.innerHTML = 'Sending…';
    btn.disabled = true;

    const data = {
      name:     form.querySelector('#field-name').value,
      org:      form.querySelector('#field-org').value,
      email:    form.querySelector('#field-email').value,
      qty:      form.querySelector('#field-qty').value || 'Not specified',
      interest: form.querySelector('#field-interest').value || 'Not specified',
      message:  form.querySelector('#field-message').value || 'None',
      _subject: 'New Inquiry — Minal Industres Catalog',
    };

    fetch('https://formsubmit.co/ajax/parthlahor@gmail.com', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(data)
    })
    .then(r => r.json())
    .then(r => {
      if (r.success === 'true' || r.success === true) {
        showToast('Inquiry received. We\'ll respond within 4 hours.');
        form.reset();
      } else throw new Error(r.message || 'Failed');
    })
    .catch(() => {
      showToast('Something went wrong — please WhatsApp or email us directly.');
    })
    .finally(() => { btn.innerHTML = orig; btn.disabled = false; });
  });
}

/* ─────────────────────────────────────────
   SCROLL TO TOP
───────────────────────────────────────── */
function initScrollToTop() {
  const btn = document.getElementById('scrollTopBtn');
  if (!btn) return;
  window.addEventListener('scroll', () => btn.classList.toggle('visible', window.scrollY > 700), { passive: true });
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

/* ─────────────────────────────────────────
   IMAGE LIGHTBOX MODAL
───────────────────────────────────────── */
function initImageModal() {
  const modal    = document.getElementById('imageModal');
  const modalImg = document.getElementById('imageModalImg');
  const closeBtn = document.querySelector('.image-modal-close');
  if (!modal || !modalImg) return;

  // Click any product photo to enlarge
  document.querySelectorAll('.product-photo').forEach(img => {
    img.style.cursor = 'zoom-in';
    img.addEventListener('click', () => {
      modalImg.src = img.src;
      modalImg.alt = img.alt;
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  const close = () => {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  };

  closeBtn && closeBtn.addEventListener('click', close);
  modal.addEventListener('click', e => { if (e.target === modal) close(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
}
