// Meet the Maestros JavaScript

// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips if any
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Handle navbar collapse on mobile
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    // Close navbar when clicking on a nav link (mobile)
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse.classList.contains('show')) {
                navbarToggler.click();
            }
        });
    });

    // Update active nav link on scroll
    updateActiveNavLink();
    window.addEventListener('scroll', updateActiveNavLink);

    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe composer sections for animation
    document.querySelectorAll('.composer-section').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        observer.observe(section);
    });
});

// Function to scroll to specific composer section
function scrollToComposer(composerId) {
    const element = document.getElementById(composerId);
    if (element) {
        const navbarHeight = document.querySelector('.navbar').offsetHeight;
        const targetPosition = element.offsetTop - navbarHeight - 20;
        
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    }
}

// Function to update active navigation link
function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    let currentSection = '';
    const scrollPosition = window.scrollY + 100;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        
        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            currentSection = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSection}`) {
            link.classList.add('active');
        }
    });
}

// Add loading animation for YouTube videos
document.addEventListener('DOMContentLoaded', function() {
    const iframes = document.querySelectorAll('iframe[src*="youtube"]');
    
    iframes.forEach(iframe => {
        iframe.addEventListener('load', function() {
            this.style.opacity = '1';
        });
        
        iframe.style.opacity = '0';
        iframe.style.transition = 'opacity 0.5s ease';
    });
});

// Enhance composer card interactions
document.addEventListener('DOMContentLoaded', function() {
    const composerCards = document.querySelectorAll('.composer-card');
    
    composerCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
});

// Add keyboard navigation support
document.addEventListener('keydown', function(event) {
    if (event.key === 'ArrowDown') {
        const currentSection = getCurrentSection();
        const nextSection = getNextSection(currentSection);
        if (nextSection) {
            scrollToComposer(nextSection);
        }
    } else if (event.key === 'ArrowUp') {
        const currentSection = getCurrentSection();
        const prevSection = getPrevSection(currentSection);
        if (prevSection) {
            scrollToComposer(prevSection);
        }
    }
});

function getCurrentSection() {
    const sections = ['home', 'mozart', 'beethoven', 'bach', 'tchaikovsky', 'chopin'];
    const scrollPosition = window.scrollY + 100;
    
    for (let i = 0; i < sections.length; i++) {
        const element = document.getElementById(sections[i]);
        if (element) {
            const sectionTop = element.offsetTop;
            const sectionHeight = element.offsetHeight;
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                return sections[i];
            }
        }
    }
    return 'home';
}

function getNextSection(currentSection) {
    const sections = ['home', 'mozart', 'beethoven', 'bach', 'tchaikovsky', 'chopin'];
    const currentIndex = sections.indexOf(currentSection);
    return currentIndex < sections.length - 1 ? sections[currentIndex + 1] : null;
}

function getPrevSection(currentSection) {
    const sections = ['home', 'mozart', 'beethoven', 'bach', 'tchaikovsky', 'chopin'];
    const currentIndex = sections.indexOf(currentSection);
    return currentIndex > 0 ? sections[currentIndex - 1] : null;
}

// Performance optimization: Lazy load YouTube videos
document.addEventListener('DOMContentLoaded', function() {
    const videoContainers = document.querySelectorAll('.video-container');
    
    const videoObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const iframe = entry.target.querySelector('iframe');
                if (iframe && !iframe.src.includes('autoplay=0')) {
                    iframe.src += '&autoplay=0';
                }
                videoObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5
    });

    videoContainers.forEach(container => {
        videoObserver.observe(container);
    });
});
