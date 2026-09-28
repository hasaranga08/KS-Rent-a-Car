/**
 * KS Rent a Car Sri Lanka - Interactive Scripts
 * Domain: https://www.srilankacarrents.com
 * WhatsApp: +94 77 719 3915
 */

document.addEventListener('DOMContentLoaded', () => {
  // Resilient Brand Logo Fallback for GitHub Pages & custom domains
  const brandLogos = document.querySelectorAll("img.brand-logo");
  brandLogos.forEach(img => {
    img.addEventListener("error", function onLogoError() {
      if (!this.dataset.retryIndex) this.dataset.retryIndex = "0";
      const idx = parseInt(this.dataset.retryIndex, 10);
      const candidates = [
        "assets/images/Logo.png",
        "../assets/images/Logo.png",
        "../../assets/images/Logo.png",
        "assets/images/logo.png",
        "../assets/images/logo.png",
        "../../assets/images/logo.png"
      ];
      if (idx < candidates.length) {
        this.dataset.retryIndex = String(idx + 1);
        this.src = candidates[idx];
      }
    });
  });

  // Dynamic Sticky Navigation on Scroll
  const siteHeader = document.querySelector(".site-header");
  if (siteHeader) {
    const handleScroll = () => {
      if (window.scrollY > 20) {
        siteHeader.classList.add("scrolled");
      } else {
        siteHeader.classList.remove("scrolled");
      }
    };
    window.addEventListener("scroll", handleScroll, { passive: true });
    handleScroll();
  }

  // 1. Mobile Navigation Toggle
  const mobileToggle = document.getElementById('mobileNavToggle');
  const mobileDrawer = document.getElementById('mobileNavDrawer');
  const mobileBackdrop = document.getElementById('mobileNavBackdrop');
  const mobileClose = document.getElementById('mobileNavClose');

  function openMobileNav() {
    if (mobileDrawer && mobileBackdrop) {
      mobileDrawer.classList.add('open');
      mobileBackdrop.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeMobileNav() {
    if (mobileDrawer && mobileBackdrop) {
      mobileDrawer.classList.remove('open');
      mobileBackdrop.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  if (mobileToggle) mobileToggle.addEventListener('click', openMobileNav);
  if (mobileClose) mobileClose.addEventListener('click', closeMobileNav);
  if (mobileBackdrop) mobileBackdrop.addEventListener('click', closeMobileNav);

  // 1b. Mobile Navigation Dropdown Accordion (Location)
  const mobileDropdownToggles = document.querySelectorAll('.mobile-dropdown-toggle');
  mobileDropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const parentItem = toggle.closest('.mobile-nav-item-dropdown');
      if (parentItem) {
        const isOpen = parentItem.classList.contains('open');
        parentItem.classList.toggle('open');
        toggle.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
      }
    });
  });

  // Close mobile nav when clicking on standard links (excluding dropdown toggle buttons)
  const navigableMobileLinks = document.querySelectorAll('.mobile-nav-link:not(.mobile-dropdown-toggle), .mobile-dropdown-link');
  navigableMobileLinks.forEach(link => {
    link.addEventListener('click', closeMobileNav);
  });

  // 2. Sticky Header Elevation
  const header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 30) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  // 3. FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (question) {
      question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        
        // Close other open items for clean accordion effect
        faqItems.forEach(otherItem => {
          if (otherItem !== item) {
            otherItem.classList.remove('active');
            const otherBtn = otherItem.querySelector('.faq-question');
            if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
          }
        });

        // Toggle current item
        if (isActive) {
          item.classList.remove('active');
          question.setAttribute('aria-expanded', 'false');
        } else {
          item.classList.add('active');
          question.setAttribute('aria-expanded', 'true');
        }
      });
    }
  });

  // 4. Vehicle Category Filtering
  const filterButtons = document.querySelectorAll('.filter-btn');
  const vehicleCards = document.querySelectorAll('.vehicle-card');

  if (filterButtons.length > 0 && vehicleCards.length > 0) {
    filterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const category = btn.getAttribute('data-filter');

        vehicleCards.forEach(card => {
          const cardCat = card.getAttribute('data-category');
          if (category === 'all' || cardCat === category) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // 5. Automatic Vehicle Pre-selection via URL parameter
  // E.g.: contact.html?vehicle=Toyota%20Premio or index.html#enquiry?vehicle=Honda%20Vezel
  function checkUrlForVehicle() {
    const urlParams = new URLSearchParams(window.location.search);
    let vehicleParam = urlParams.get('vehicle');
    
    // Also check hash
    if (!vehicleParam && window.location.hash.includes('vehicle=')) {
      const hashPart = window.location.hash.split('vehicle=')[1];
      if (hashPart) {
        vehicleParam = decodeURIComponent(hashPart.split('&')[0]);
      }
    }

    if (vehicleParam) {
      const vehicleSelect = document.getElementById('vehicleSelect');
      if (vehicleSelect) {
        for (let i = 0; i < vehicleSelect.options.length; i++) {
          if (vehicleSelect.options[i].value.toLowerCase() === vehicleParam.toLowerCase()) {
            vehicleSelect.selectedIndex = i;
            break;
          }
        }
      }

      // Scroll smoothly to the form if requested
      const enquiryForm = document.getElementById('rentalEnquiryForm');
      if (enquiryForm && window.location.hash.includes('enquiry')) {
        setTimeout(() => {
          enquiryForm.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 150);
      }
    }
  }

  checkUrlForVehicle();

  // 6. Formspree / AJAX Enquiry Handling
  const enquiryForms = document.querySelectorAll('form[action*="formspree.io"], #rentalEnquiryForm, #weddingEnquiryForm, .enquiry-form');

  enquiryForms.forEach((enquiryForm) => {
    let formAlert = enquiryForm.closest('.form-container')?.querySelector('.form-alert') ||
                    enquiryForm.parentElement?.querySelector('.form-alert') ||
                    document.getElementById('formAlert');

    enquiryForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      if (!formAlert) {
        formAlert = document.createElement('div');
        formAlert.className = 'form-alert';
        enquiryForm.parentNode.insertBefore(formAlert, enquiryForm);
      }

      const formData = new FormData(enquiryForm);
      const action = enquiryForm.getAttribute('action') || 'https://formspree.io/f/mkjgbonn';

      const name = formData.get('name') || formData.get('fullName') || '';
      const phone = formData.get('phone') || formData.get('whatsappNumber') || '';
      const vehicle = formData.get('vehicle_required') || formData.get('preferredVehicle') || 'Not Sure';
      const rentalType = formData.get('rental_type') || formData.get('serviceType') || 'Rental';
      const pickupDate = formData.get('pickup_date') || formData.get('pickupDate') || 'TBD';
      const returnDate = formData.get('return_date') || formData.get('returnDate') || 'TBD';
      const pickupLoc = formData.get('pickup_location') || formData.get('pickupLocation') || 'Colombo / Airport';

      // Real Formspree submission
      const submitBtn = enquiryForm.querySelector('button[type="submit"], input[type="submit"]');
      const originalText = submitBtn ? (submitBtn.tagName === 'INPUT' ? submitBtn.value : submitBtn.textContent) : 'Send Rental Enquiry';
      if (submitBtn) {
        submitBtn.disabled = true;
        if (submitBtn.tagName === 'INPUT') {
          submitBtn.value = 'Sending Enquiry...';
        } else {
          submitBtn.textContent = 'Sending Enquiry...';
        }
      }

      try {
        const response = await fetch(action, {
          method: 'POST',
          body: formData,
          headers: {
            'Accept': 'application/json'
          }
        });

        if (response.ok) {
          if (formAlert) {
            formAlert.className = 'form-alert success';
            formAlert.innerHTML = `
              <strong>Thank you, ${name || 'Customer'}!</strong> Your rental enquiry has been received. Our team will review vehicle availability and contact you shortly. For immediate assistance, feel free to contact us on WhatsApp (+94 77 719 3915).
            `;
            formAlert.style.display = 'block';
            formAlert.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          }
          enquiryForm.reset();
        } else {
          const data = await response.json().catch(() => ({}));
          let errorMsg = data.error;
          if (Array.isArray(data.errors) && data.errors.length > 0) {
            errorMsg = data.errors.map(item => item.message).join(', ');
          }
          throw new Error(errorMsg || 'There was an issue submitting your enquiry to Formspree.');
        }
      } catch (err) {
        if (formAlert) {
          formAlert.className = 'form-alert error';
          formAlert.innerHTML = `
            <strong>Notice:</strong> ${err.message || 'Could not send enquiry.'}<br>
            Please contact us directly on WhatsApp for an immediate response:
            <a href="https://wa.me/94777193915" target="_blank" rel="noopener" style="font-weight:700; color:#15803d; text-decoration:underline;">+94 77 719 3915</a>.
          `;
          formAlert.style.display = 'block';
          formAlert.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          if (submitBtn.tagName === 'INPUT') {
            submitBtn.value = originalText;
          } else {
            submitBtn.textContent = originalText;
          }
        }
      }
    });
  });

  // 6. Vehicle Gallery Thumbnail Switcher
  const galleryThumbs = document.querySelectorAll('.vehicle-gallery-thumb');
  galleryThumbs.forEach(thumb => {
    thumb.addEventListener('click', () => {
      const targetSrc = thumb.getAttribute('data-img');
      const gallery = thumb.closest('.vehicle-gallery');
      if (gallery && targetSrc) {
        const mainImg = gallery.querySelector('.vehicle-main-img');
        if (mainImg) {
          mainImg.src = targetSrc;
          gallery.querySelectorAll('.vehicle-gallery-thumb').forEach(t => t.classList.remove('active'));
          thumb.classList.add('active');
        }
      }
    });
  });
});
