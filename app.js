/**
 * MINAL INDUSTRES — CATALOG 2026
 * Interactive Behaviors
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initScrollAnimations();
  initCatalogFilters();
  initFormHandling();
  initScrollToTop();
  initImageModal();
  initVideoModal();
});

/**
 * Mobile Navigation & Sticky Header
 */
function initNavigation() {
  const nav = document.getElementById('main-nav');
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.querySelector('.nav-links');
  const navItems = document.querySelectorAll('.nav-link');

  // Sticky Header
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  });

  // Initial check
  if (window.scrollY > 50) {
    nav.classList.add('scrolled');
  }

  // Mobile Toggle
  if (navToggle) {
    navToggle.addEventListener('click', () => {
      navToggle.classList.toggle('open');
      navLinks.classList.toggle('open');
      document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : '';
    });
  }

  // Close mobile menu on link click & handle active states
  navItems.forEach(item => {
    item.addEventListener('click', () => {
      if (navLinks.classList.contains('open')) {
        navToggle.classList.remove('open');
        navLinks.classList.remove('open');
        document.body.style.overflow = '';
      }
    });
  });

  // Active link highlight based on scroll position
  const sections = document.querySelectorAll('section');
  
  window.addEventListener('scroll', () => {
    let current = '';
    const scrollY = window.scrollY;

    sections.forEach(section => {
      const sectionTop = section.offsetTop - 100;
      const sectionHeight = section.clientHeight;
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navItems.forEach(item => {
      item.classList.remove('active');
      if (item.getAttribute('href').includes(current)) {
        item.classList.add('active');
      }
    });
  });
}

/**
 * Scroll Animations using IntersectionObserver
 */
function initScrollAnimations() {
  const animatedElements = document.querySelectorAll('[data-animate]');
  
  // Add staggering delays for elements in grids/rows
  const processGroup = (selector, dataAttr) => {
    const groups = document.querySelectorAll(selector);
    groups.forEach(group => {
      const items = group.querySelectorAll(`[data-animate="${dataAttr}"]`);
      items.forEach((item, index) => {
        // limit delay classes to 1-4
        const delayClass = `delay-${(index % 4) + 1}`;
        item.classList.add(delayClass);
      });
    });
  };

  processGroup('.intro-stats', 'stat');
  processGroup('.products-row', 'card');
  processGroup('.bespoke-grid', 'bespoke-card');

  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -10% 0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-animated');
        observer.unobserve(entry.target); // Only animate once
      }
    });
  }, observerOptions);

  animatedElements.forEach(el => {
    observer.observe(el);
  });
}

/**
 * Catalog Category Filtering
 */
function initCatalogFilters() {
  const tabs = document.querySelectorAll('.tab-btn');
  const blocks = document.querySelectorAll('.category-block');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      // Remove active from all tabs
      tabs.forEach(t => {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });
      
      // Add active to clicked
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');

      const targetCat = tab.getAttribute('data-category');

      // Show/Hide blocks
      blocks.forEach(block => {
        if (targetCat === 'all' || block.getAttribute('data-category') === targetCat) {
          block.classList.remove('hidden');
          // Re-trigger animation for newly shown items
          const cards = block.querySelectorAll('.product-card');
          cards.forEach(card => {
            card.classList.remove('is-animated');
            // Small timeout to allow display:block to apply before animating
            setTimeout(() => {
              card.classList.add('is-animated');
            }, 50);
          });
        } else {
          block.classList.add('hidden');
        }
      });
    });
  });
}

/**
 * Form Handling & Toast Notification
 */
function initFormHandling() {
  const form = document.getElementById('inquiryForm');
  const toast = document.getElementById('formToast');
  
  if (!form || !toast) return;

  // Pre-fill interest if user clicked a bespoke service CTA
  const bespokeBtn = document.getElementById('bespokeConsultBtn');
  const interestSelect = document.getElementById('field-interest');
  
  if (bespokeBtn && interestSelect) {
    bespokeBtn.addEventListener('click', () => {
      interestSelect.value = 'bespoke';
    });
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Basic validation check
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    const submitBtn = document.getElementById('submitInquiryBtn');
    const originalHTML = submitBtn.innerHTML;
    
    // Show loading state
    submitBtn.innerHTML = 'Sending…';
    submitBtn.style.opacity = '0.7';
    submitBtn.disabled = true;

    // Collect form data
    const data = {
      name:     form.querySelector('#field-name').value,
      org:      form.querySelector('#field-org').value,
      email:    form.querySelector('#field-email').value,
      qty:      form.querySelector('#field-qty').value || 'Not specified',
      interest: form.querySelector('#field-interest').value || 'Not specified',
      message:  form.querySelector('#field-message').value || 'No message provided',
      _subject: 'New Inquiry — Minal Industres Catalog',
    };

    // Send via Formsubmit (no account needed — first submission will ask you to verify your email)
    fetch('https://formsubmit.co/ajax/parthlahor@gmail.com', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {
      if (res.success === 'true' || res.success === true) {
        // ✅ Show success toast
        toast.classList.add('show');
        form.reset();
        setTimeout(() => toast.classList.remove('show'), 5000);
      } else {
        throw new Error(res.message || 'Submission failed');
      }
    })
    .catch(err => {
      console.error('Form error:', err);
      alert('Sorry, something went wrong. Please email us directly at gifts@minal-industres.com');
    })
    .finally(() => {
      submitBtn.innerHTML = originalHTML;
      submitBtn.style.opacity = '1';
      submitBtn.disabled = false;
    });
  });
}

/**
 * Scroll to Top functionality
 */
function initScrollToTop() {
  const scrollBtn = document.getElementById('scrollTopBtn');
  
  if (!scrollBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 800) {
      scrollBtn.classList.add('visible');
    } else {
      scrollBtn.classList.remove('visible');
    }
  });

  scrollBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/**
 * Image Modal
 */
function initImageModal() {
  const modal = document.getElementById("imageModal");
  const modalImg = document.getElementById("imageModalImg");
  const closeBtn = document.querySelector(".image-modal-close");
  // Only target photos from regular non-video product cards
  const productImages = document.querySelectorAll(".product-card:not([data-video]) .product-photo");

  if (!modal || !modalImg || !closeBtn) return;

  productImages.forEach(img => {
    img.addEventListener("click", function(e) {
      e.stopPropagation();
      modal.style.display = "block";
      modalImg.src = this.src;
    });
  });

  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  // Close when clicking outside the image
  modal.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.style.display = "none";
    }
  });

  // Close with escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === "Escape" && modal.style.display === "block") {
      modal.style.display = "none";
    }
  });
}

/**
 * Video Modal — click-to-play modal for video items
 */
function initVideoModal() {
  const modal = document.getElementById('videoModal');
  const player = document.getElementById('videoModalPlayer');
  const closeBtn = document.getElementById('videoModalClose');

  if (!modal || !player || !closeBtn) return;

  function closeVideoModal() {
    modal.classList.remove('active');
    player.pause();
    player.src = '';
    document.body.style.overflow = '';
  }

  closeBtn.addEventListener('click', closeVideoModal);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeVideoModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeVideoModal();
    }
  });
}

/**
 * Opens the video modal for a given video card element.
 * Called inline via onclick on [data-video] elements.
 */
function openVideoModal(cardEl) {
  const modal = document.getElementById('videoModal');
  const player = document.getElementById('videoModalPlayer');
  if (!modal || !player) return;

  const src = cardEl.getAttribute('data-video');
  if (!src) return;

  player.src = src;
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
  player.play().catch(() => {
    // Some browsers require manual user play gesture
  });
}

