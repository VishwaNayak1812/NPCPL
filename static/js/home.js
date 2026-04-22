document.addEventListener('DOMContentLoaded', () => {
    const themeBtn = document.getElementById('theme-switch');
    const modeIcon = document.getElementById('mode-icon');
    const html = document.documentElement;
    const navLinks = document.querySelectorAll('.nav-link');
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
    html.setAttribute('data-theme', savedTheme);
    modeIcon.className = savedTheme === 'dark'
        ? 'fas fa-moon'
        : 'fas fa-sun';
}
    /* ===============================
       1. Theme & Icon Toggle
    =============================== */
    themeBtn.addEventListener('click', () => {
        const isDark = html.getAttribute('data-theme') === 'dark';
        const nextTheme = isDark ? 'light' : 'dark';
        
        html.setAttribute('data-theme', nextTheme);
        modeIcon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
        localStorage.setItem('theme', nextTheme);
    });

    /* ================= MOBILE MENU TOGGLE ================= */
const menuToggle = document.getElementById("menuToggle");
const navMenu = document.getElementById("main-nav");

if (menuToggle) {
    menuToggle.addEventListener("click", () => {
        navMenu.classList.toggle("active");
    });
}

    /* ===============================
       2. Navigation Active State
    =============================== */
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });
    /* ===============================
       3. Real-time Clock
    =============================== */
    function clock() {
        const now = new Date();
        document.getElementById('digital-clock').innerHTML = 
            `<small>${now.toDateString()}</small><br><b>${now.toLocaleTimeString()} IST</b>`;
    }
    setInterval(clock, 1000);
    clock();

    /* ===============================
       4. Typing Effect (Tagline)
    =============================== */
    const typingText = document.getElementById('typing-text');
    const text = "Ruling Mountains, Building Trust.";
    let index = 0;

    function typeEffect() {
        if (typingText && index < text.length) {
            typingText.textContent += text.charAt(index);
            index++;
            setTimeout(typeEffect, 70);
        }
    }

    // Delay typing slightly for cinematic feel
    setTimeout(typeEffect, 800);

    /* ===============================
       5. Hero Reveal Sync (Optional)
    =============================== */
    const heroTitle = document.querySelector('.main-heading');
    if (heroTitle) {
        heroTitle.style.opacity = "1";
    }

/* ===============================         
    6. Live Market Ticker
=============================== */


/* ===============================
   Market Ticker Visibility on Scroll
=============================== */
const tickerBar = document.querySelector('.market-ticker-bar');

window.addEventListener('scroll', () => {
    if (!tickerBar) return;

    if (window.scrollY > 80) {
        tickerBar.classList.add('hide');
    } else {
        tickerBar.classList.remove('hide');
    }
});

/* ===============================
   Auto Calculate Years of Experience
=============================== */
const expCounter = document.querySelector('.experience-counter');

if (expCounter) {
    const startYear = parseInt(expCounter.dataset.startYear);
    const currentYear = new Date().getFullYear();
    const experienceYears = currentYear - startYear;

    expCounter.dataset.target = experienceYears;
}
    /* ===============================
       7. Animated Stats Counter
    =============================== */
const counters = document.querySelectorAll('.counter');
const statsSection = document.getElementById('stats');
let counterStarted = false;

function startCounters() {
    counters.forEach(counter => {
        const target = parseInt(counter.dataset.target);
        let count = 0;
        const increment = Math.max(1, target / 100);

        function updateCounter() {
            count += increment;
            if (count < target) {
                counter.textContent = Math.ceil(count);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        }
        updateCounter();
    });
}

window.addEventListener('scroll', () => {
    if (!statsSection || counterStarted) return;

    const sectionTop = statsSection.getBoundingClientRect().top;
    const triggerPoint = window.innerHeight - 150;

    if (sectionTop < triggerPoint) {
        startCounters();
        counterStarted = true;
    }
});
/* ===============================
   8. Navigate to About Page
=============================== */
const aboutBtn = document.getElementById('aboutMoreBtn');

if (aboutBtn) {
    aboutBtn.addEventListener('click', () => {
        window.location.href = "/about";
    });
}

/* ===============================
   9. Navigate to Product Page
=============================== */
const ProductBtn = document.getElementById('productinfo');

if (ProductBtn) {
    ProductBtn.addEventListener('click', () => {
        window.location.href = "/product";
    });
}
});
