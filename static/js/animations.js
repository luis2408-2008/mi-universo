// Animations JavaScript file for Explorador Cósmico

document.addEventListener('DOMContentLoaded', function() {
    // Generate more stars dynamically for the background
    generateStars();
    
    // Animate elements with data-animate attribute
    animateElements();
    
    // Add parallax effect to certain elements
    initParallax();
});

// Function to generate more stars for the starry background
function generateStars() {
    const starsContainer = document.getElementById('stars');
    
    if (!starsContainer) return;
    
    // Create a canvas for better performance
    const canvas = document.createElement('canvas');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    starsContainer.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    const starColors = [
        'rgba(255, 250, 227, 0.8)',
        'rgba(255, 250, 227, 0.6)',
        'rgba(255, 250, 227, 0.4)',
        'rgba(181, 101, 167, 0.6)',
        'rgba(123, 40, 125, 0.5)'
    ];
    
    // Generate random stars
    const starCount = Math.floor((canvas.width * canvas.height) / 1000);
    
    for (let i = 0; i < starCount; i++) {
        const x = Math.random() * canvas.width;
        const y = Math.random() * canvas.height;
        const radius = Math.random() * 1.5;
        const color = starColors[Math.floor(Math.random() * starColors.length)];
        
        // Draw the star
        ctx.beginPath();
        ctx.arc(x, y, radius, 0, Math.PI * 2);
        ctx.fillStyle = color;
        ctx.fill();
        
        // Add twinkling effect to some stars
        if (Math.random() > 0.7) {
            const star = document.createElement('div');
            star.className = 'absolute animate-twinkle';
            star.style.left = `${x}px`;
            star.style.top = `${y}px`;
            star.style.width = `${radius * 2}px`;
            star.style.height = `${radius * 2}px`;
            star.style.backgroundColor = color;
            star.style.borderRadius = '50%';
            
            starsContainer.appendChild(star);
        }
    }
    
    // Add a few larger stars with glow effect
    for (let i = 0; i < 20; i++) {
        const x = Math.random() * canvas.width;
        const y = Math.random() * canvas.height;
        const radius = 1.5 + Math.random() * 1.5;
        
        // Create the star with glow
        const star = document.createElement('div');
        star.className = 'absolute animate-pulse-slow';
        star.style.left = `${x}px`;
        star.style.top = `${y}px`;
        star.style.width = `${radius * 2}px`;
        star.style.height = `${radius * 2}px`;
        star.style.backgroundColor = 'rgba(255, 250, 227, 0.9)';
        star.style.borderRadius = '50%';
        star.style.boxShadow = '0 0 10px 2px rgba(255, 250, 227, 0.7)';
        
        starsContainer.appendChild(star);
    }
}

// Function to animate elements as they scroll into view
function animateElements() {
    // Fade-in effect for sections as they scroll into view
    const sections = document.querySelectorAll('section');
    
    const fadeInObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('opacity-100');
                entry.target.classList.remove('opacity-0', 'translate-y-10');
                fadeInObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    sections.forEach(section => {
        // Only add the animation to sections that aren't already visible
        if (!section.classList.contains('animate-float')) {
            section.classList.add('opacity-0', 'translate-y-10', 'transition', 'duration-700');
            fadeInObserver.observe(section);
        }
    });
}

// Function to initialize parallax effects
function initParallax() {
    // Simple parallax effect on scroll
    window.addEventListener('scroll', function() {
        const scrollY = window.scrollY;
        
        // Parallax stars
        const stars = document.getElementById('stars');
        if (stars) {
            stars.style.transform = `translateY(${scrollY * 0.3}px)`;
        }
    });
}
