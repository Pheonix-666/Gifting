/**
 * PRESTIGE & CO. — CATALOG 2026
 * Interactive Behaviors
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initScrollAnimations();
  initCatalogFilters();
  initFormHandling();
  initScrollToTop();
  initImageModal();
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
    const originalText = submitBtn.innerHTML;
    
    // Simulate loading
    submitBtn.innerHTML = 'Sending...';
    submitBtn.style.opacity = '0.7';
    submitBtn.disabled = true;

    // Simulate API call
    setTimeout(() => {
      // Show toast
      toast.classList.add('show');
      
      // Reset form & button
      form.reset();
      submitBtn.innerHTML = originalText;
      submitBtn.style.opacity = '1';
      submitBtn.disabled = false;

      // Hide toast after 5s
      setTimeout(() => {
        toast.classList.remove('show');
      }, 5000);
      
    }, 1200);
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
  const productImages = document.querySelectorAll(".product-photo");

  if (!modal || !modalImg || !closeBtn) return;

  productImages.forEach(img => {
    img.addEventListener("click", function() {
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
