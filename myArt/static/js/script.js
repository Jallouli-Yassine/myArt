document.addEventListener('DOMContentLoaded', () => {
  
  // 1. Mobile Navigation Toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  
  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', () => {
      navLinks.classList.toggle('nav-open');
      
      // Animate hamburger to X
      const spans = menuToggle.querySelectorAll('span');
      if (navLinks.classList.contains('nav-open')) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
      } else {
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
      }
    });
  }

  // 2. Intersection Observer for fade-in animations
  const faders = document.querySelectorAll('.fade-in-up');
  
  const appearOptions = {
    threshold: 0.15,
    rootMargin: "0px 0px -50px 0px"
  };
  
  const appearOnScroll = new IntersectionObserver(function(entries, observer) {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      
      entry.target.classList.add('appear');
      observer.unobserve(entry.target);
    });
  }, appearOptions);
  
  faders.forEach(fader => {
    appearOnScroll.observe(fader);
  });

  // 3. Floating Background Shapes Generator
  // Optimized for performance - removed heavy blurs and reduced number
  const createBgShapes = () => {
    const numShapes = 4;
    const bgContainer = document.querySelector('.starry-night-bg');
    if (!bgContainer) return;

    const colors = ['rgba(255, 228, 230, 0.4)', 'rgba(255, 204, 213, 0.3)', 'rgba(255, 255, 255, 0.2)'];
    
    for (let i = 0; i < numShapes; i++) {
        const shape = document.createElement('div');
        shape.classList.add('bg-shape');
        
        // Random properties for a cute soft look
        const size = Math.random() * 60 + 40; // 40px to 100px
        const color = colors[Math.floor(Math.random() * colors.length)];
        const left = Math.random() * 90; // 0% to 90%
        const top = Math.random() * 100; // use vh relative instead of scrollHeight
        
        shape.style.position = 'absolute';
        shape.style.width = `${size}px`;
        shape.style.height = `${size}px`;
        shape.style.background = `radial-gradient(circle, ${color} 0%, transparent 70%)`; // Built-in blur via gradient
        shape.style.borderRadius = '50%';
        shape.style.left = `${left}vw`;
        shape.style.top = `${top}vh`;
        shape.style.animation = `float ${Math.random() * 10 + 15}s ease-in-out infinite`;
        shape.style.animationDelay = `-${Math.random() * 5}s`;
        shape.style.pointerEvents = 'none';
        shape.style.willChange = 'transform';
        
        bgContainer.appendChild(shape);
    }
  };
  
  // Call it after a short delay
  setTimeout(createBgShapes, 500);

  // 4. "J'adore ❤️" Button Interaction
  const jadoreBtns = document.querySelectorAll('.jadore-btn');
  jadoreBtns.forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault(); // In case it's in a link
      const icon = this.querySelector('i');
      const countSpan = this.querySelector('.like-count');
      
      // Simple toggle animation effect
      this.style.transform = 'scale(0.9)';
      setTimeout(() => {
        this.style.transform = 'scale(1)';
        
        let count = countSpan ? parseInt(countSpan.textContent) : 0;
        
        if (this.classList.contains('liked')) {
          this.classList.remove('liked');
          if(icon) {
            icon.classList.remove('fa-solid');
            icon.classList.add('fa-regular');
          }
          this.style.color = 'var(--text-color)';
          if (countSpan) countSpan.textContent = count - 1;
        } else {
          this.classList.add('liked');
          if(icon) {
            icon.classList.remove('fa-regular');
            icon.classList.add('fa-solid');
          }
          this.style.color = 'var(--accent-color)';
          if (countSpan) countSpan.textContent = count + 1;
        }
      }, 150);
    });
  });

  // 5. Chatbot Toggle Logic
  const chatbotBtn = document.querySelector('#chatbot-toggle');
  const chatbotWindow = document.querySelector('#chatbot-window');
  const chatbotClose = document.querySelector('#chatbot-close');
  
  if (chatbotBtn && chatbotWindow && chatbotClose) {
    chatbotBtn.addEventListener('click', () => {
      chatbotWindow.classList.add('active');
    });
    
    chatbotClose.addEventListener('click', () => {
      chatbotWindow.classList.remove('active');
    });
  }

  // 6. Smooth Mouse Parallax for Background Swirls (Premium Feel, Optimized)
  const swirls = document.querySelectorAll('.swirl');
  const sparkles = document.querySelectorAll('.sparkle');
  
  if (swirls.length > 0 || sparkles.length > 0) {
    let mouseX = 0;
    let mouseY = 0;
    let targetX = 0;
    let targetY = 0;
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    document.addEventListener('mousemove', (e) => {
      mouseX = (e.clientX - windowWidth / 2) * 0.05; // 5% movement impact
      mouseY = (e.clientY - windowHeight / 2) * 0.05;
    });

    const renderParallax = () => {
      // Ease toward target (smooth interpolation)
      targetX += (mouseX - targetX) * 0.1;
      targetY += (mouseY - targetY) * 0.1;

      swirls.forEach((swirl, index) => {
        // Different layers move at different speeds based on index
        const speed = (index + 1) * 0.8;
        const x = targetX * speed;
        const y = targetY * speed;
        
        // Use CSS variables so we don't override the CSS rotate/float animations!
        swirl.style.setProperty('--px', `${x}px`);
        swirl.style.setProperty('--py', `${y}px`);
      });
      
      sparkles.forEach((sparkle, index) => {
        const speed = (index + 1) * 0.3; // Subtle movement for stars
        const x = targetX * speed * -1; // Move opposite to swirls for depth
        const y = targetY * speed * -1;
        sparkle.style.setProperty('--px', `${x}px`);
        sparkle.style.setProperty('--py', `${y}px`);
      });

      requestAnimationFrame(renderParallax);
    };

    requestAnimationFrame(renderParallax);
  }

});
