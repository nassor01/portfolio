/**
 * Masculine Tech Portfolio - Interactivity
 */

document.addEventListener('DOMContentLoaded', () => {
    // Particle Generator
    const particlesContainer = document.getElementById('particles');
    const particleSymbols = ['{ }', '[ ]', '</>', '01', '10', '&&', '||', '=>', '++'];

    const createParticle = () => {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.textContent = particleSymbols[Math.floor(Math.random() * particleSymbols.length)];

        const size = Math.random() * 20 + 10;
        particle.style.fontSize = `${size}px`;
        particle.style.left = `${Math.random() * 100}%`;
        particle.style.animationDuration = `${Math.random() * 10 + 10}s`;
        particle.style.animationDelay = `${Math.random() * 5}s`;

        particlesContainer.appendChild(particle);

        // Remove after animation
        setTimeout(() => {
            particle.remove();
        }, 20000);
    };

    // Initial particles
    for (let i = 0; i < 20; i++) {
        createParticle();
    }

    // Continuous generation
    setInterval(createParticle, 2000);

    // Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Dynamic Tech-Greeting
    const updateGreeting = () => {
        const greetingElement = document.getElementById('dynamic-greeting');
        if (!greetingElement) return;

        const hour = new Date().getHours();
        let cmd = "> Hello, I'm";

        if (hour >= 5 && hour < 12) cmd = "> morning.booting --user";
        else if (hour >= 12 && hour < 18) cmd = "> active.afternoon --user";
        else if (hour >= 18 && hour < 22) cmd = "> evening.compiling --user";
        else cmd = "> midnight.kernel --user";

        greetingElement.innerHTML = `<span style="opacity: 0.5;">${cmd}</span> ${document.querySelector('.hero-name').textContent.split(' ')[0]}`;
    };

    updateGreeting();

    // Smooth Scrolling for Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Contact Form Simulation
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = contactForm.querySelector('button');
            const originalText = submitBtn.textContent;

            submitBtn.textContent = "[ TRANSMITTING... ]";
            submitBtn.style.opacity = "0.7";

            setTimeout(() => {
                submitBtn.textContent = "[ DATA RECEIVED ]";
                submitBtn.style.background = "#22c55e"; // Success green
                contactForm.reset();

                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.style.background = "";
                    submitBtn.style.opacity = "";
                }, 3000);
            }, 1500);
        });
    }
});
