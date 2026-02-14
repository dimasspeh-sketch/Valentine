// ==================== PASSWORD AND MUSIC CONTROL ====================
// Correct password (can be uppercase or lowercase)
const CORRECT_PASSWORD = 'MEMOVERSE';

// Music control setup
function initializeMusic() {
    const bgMusic = document.getElementById('bg-music');
    const musicToggle = document.getElementById('music-toggle');
    
    if (!bgMusic || !musicToggle) return;
    
    // Set initial volume
    bgMusic.volume = 0.3;
    bgMusic.muted = false;
    
    // Music toggle button
    musicToggle.addEventListener('click', function() {
        if (bgMusic.paused) {
            bgMusic.play();
            musicToggle.textContent = '🔊';
            localStorage.setItem('musicEnabled', 'true');
        } else {
            bgMusic.pause();
            musicToggle.textContent = '🔇';
            localStorage.setItem('musicEnabled', 'false');
        }
    });
    
    // Check localStorage for previous music preference
    const musicEnabled = localStorage.getItem('musicEnabled');
    if (musicEnabled === 'false') {
        bgMusic.pause();
        musicToggle.textContent = '🔇';
    } else {
        // Try to play music immediately
        bgMusic.play().catch(() => {
            // Autoplay might be blocked by browser - that's ok
            musicToggle.textContent = '🔇';
        });
    }
}

function checkPassword() {
    const passwordInput = document.getElementById('password-input');
    const errorMessage = document.getElementById('error-message');
    
    if (!passwordInput || !errorMessage) return;
    
    const enteredPassword = passwordInput.value.toUpperCase().trim();
    
    if (enteredPassword === CORRECT_PASSWORD) {
        // Correct password
        errorMessage.style.display = 'none';
        goToPage(2);
        passwordInput.value = '';
    } else {
        // Wrong password
        errorMessage.textContent = '❌ Password salah! Coba lagi...';
        errorMessage.style.display = 'block';
        passwordInput.focus();
        
        // Clear error message after 3 seconds
        setTimeout(() => {
            errorMessage.style.display = 'none';
        }, 3000);
    }
}

function handlePasswordKeyPress(event) {
    if (event.key === 'Enter') {
        checkPassword();
    }
}

function updatePasswordButtonState() {
    const passwordInput = document.getElementById('password-input');
    const unlockBtn = document.getElementById('unlock-btn');
    
    if (passwordInput && unlockBtn) {
        if (passwordInput.value.length > 0) {
            unlockBtn.disabled = false;
        } else {
            unlockBtn.disabled = true;
        }
    }
}

function showHint() {
    const hintBox = document.getElementById('hint-box');
    if (hintBox) {
        if (hintBox.style.display === 'none') {
            hintBox.style.display = 'block';
        } else {
            hintBox.style.display = 'none';
        }
    }
}

// ==================== FALLING LOVE HEARTS (PAGE 2) ====================
let letterPageHeartInterval = null;

function startLetterPageFallingHearts() {
    const container = document.querySelector('.falling-love-hearts');
    if (!container) return;
    
    container.innerHTML = '';
    
    // Create falling hearts periodically on letter page
    letterPageHeartInterval = setInterval(() => {
        if (document.getElementById('page4').classList.contains('active')) {
            createLetterPageFallingHeart();
        } else {
            clearInterval(letterPageHeartInterval);
            letterPageHeartInterval = null;
        }
    }, 400);
}

function createLetterPageFallingHeart() {
    const container = document.querySelector('.falling-love-hearts');
    if (!container) return;
    
    const heart = document.createElement('div');
    heart.className = 'falling-love-heart';
    heart.textContent = '❤️';
    
    const randomX = Math.random() * window.innerWidth;
    const randomSize = Math.random() * 15 + 15; // 15-30px
    const randomDuration = Math.random() * 1 + 3; // 3-4s
    const randomDelay = Math.random() * 0.5;
    
    heart.style.left = randomX + 'px';
    heart.style.top = '-50px';
    heart.style.fontSize = randomSize + 'px';
    heart.style.animationDuration = randomDuration + 's';
    heart.style.animationDelay = randomDelay + 's';
    
    container.appendChild(heart);
    
    // Remove heart after animation completes
    setTimeout(() => {
        heart.remove();
    }, (randomDuration + randomDelay) * 1000);
}

// ==================== PAGE NAVIGATION ====================
function goToPage(pageNumber) {
    // Hide all pages
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });

    // Show selected page
    const selectedPage = document.getElementById(`page${pageNumber}`);
    if (selectedPage) {
        selectedPage.classList.add('active');
    }

    // Special handling for page 2 (Valentine Question Page)
    if (pageNumber === 2) {
        startPage2Hearts();
        manageFocus(pageNumber);
        announcePageChange(pageNumber);
    }

    // Special handling for page 3 (Gallery Page)
    if (pageNumber === 3) {
        startPage4Hearts();
        manageFocus(pageNumber);
        announcePageChange(pageNumber);
    }

    // Special handling for page 4 (Sealed Letter Page)
    if (pageNumber === 4) {
        // Scroll letter to top
        const letterScroll = document.querySelector('.letter-scroll');
        if (letterScroll) {
            letterScroll.scrollTop = 0;
        }
        
        startLetterPageFallingHearts();
        manageFocus(pageNumber);
        announcePageChange(pageNumber);
    }

    // Special handling for page 5 (Sad Ending)
    if (pageNumber === 5) {
        manageFocus(pageNumber);
        announcePageChange(pageNumber);
    }

    // Special handling for page 1 (Welcome/Password)
    if (pageNumber === 1) {
        startFallingHearts();
        // Clear password input when going back
        const passwordInput = document.getElementById('password-input');
        if (passwordInput) {
            passwordInput.value = '';
        }
        manageFocus(pageNumber);
        announcePageChange(pageNumber);
    }

    // Scroll to top
    window.scrollTo(0, 0);
}

// ==================== OPEN SEALED LETTER ==================== 
function openLetter() {
    startLetterPageFallingHearts();
}

function closeLetter() {
    // Navigate back to gallery
    goToPage(3);
}

// ==================== FALLING HEARTS ANIMATION (PAGE 1) ====================
function startFallingHearts() {
    const container = document.getElementById('hearts-container');
    container.innerHTML = '';
    
    // Create falling hearts periodically
    const heartInterval = setInterval(() => {
        if (document.getElementById('page1').classList.contains('active')) {
            createFallingHeart();
        } else {
            clearInterval(heartInterval);
        }
    }, 600);
}

function createFallingHeart() {
    const container = document.getElementById('hearts-container');
    const heart = document.createElement('div');
    heart.className = 'heart';
    heart.textContent = '❤️';
    
    const randomX = Math.random() * window.innerWidth;
    const randomSize = Math.random() * 20 + 20; // 20-40px
    const randomDuration = Math.random() * 2 + 2.5; // 2.5-4.5s
    
    heart.style.left = randomX + 'px';
    heart.style.fontSize = randomSize + 'px';
    heart.style.animation = `fall ${randomDuration}s linear forwards`;
    heart.style.transform = `translateX(${Math.random() * 100 - 50}px)`;
    
    container.appendChild(heart);
    
    // Remove heart after animation completes
    setTimeout(() => {
        heart.remove();
    }, randomDuration * 1000);
}

// ==================== LETTER PAGE ANIMATION ====================
function animateLetterPage() {
    // The CSS animation already handles this with slideUpLetter
    // This function is for any additional interactivity
    console.log('Letter page animated!');
}

// ==================== FLOATING HEARTS ANIMATION (PAGE 3) ====================
function startFloatingHearts() {
    const container = document.getElementById('floating-hearts-container');
    if (!container) return;
    
    container.innerHTML = '';
    
    // Create floating hearts periodically
    const heartInterval = setInterval(() => {
        if (document.getElementById('page3').classList.contains('active')) {
            createFloatingHeart();
        } else {
            clearInterval(heartInterval);
        }
    }, 400);
}

// ==================== PAGE 2 HEARTS ANIMATION ====================
function startPage2Hearts() {
    const container = document.getElementById('page2-hearts-container');
    if (!container) return;
    
    container.innerHTML = '';
    
    const heartInterval = setInterval(() => {
        if (document.getElementById('page2').classList.contains('active')) {
            createPage2FallingHeart();
        } else {
            clearInterval(heartInterval);
        }
    }, 700);
}

function createPage2FallingHeart() {
    const container = document.getElementById('page2-hearts-container');
    if (!container) return;
    
    const heart = document.createElement('div');
    heart.className = 'heart';
    heart.textContent = '❤️';
    
    const randomX = Math.random() * window.innerWidth;
    const randomSize = Math.random() * 20 + 20;
    const randomDuration = Math.random() * 2 + 2.5;
    
    heart.style.left = randomX + 'px';
    heart.style.fontSize = randomSize + 'px';
    heart.style.animation = `fall ${randomDuration}s linear forwards`;
    heart.style.transform = `translateX(${Math.random() * 100 - 50}px)`;
    
    container.appendChild(heart);
    
    setTimeout(() => {
        heart.remove();
    }, randomDuration * 1000);
}

// ==================== PAGE 3 HEARTS ANIMATION ====================
function startPage3Hearts() {
    const container = document.getElementById('letter-hearts-container');
    if (!container) return;
    
    container.innerHTML = '';
}

// ==================== PAGE 4 GALLERY HEARTS ANIMATION ====================
function startPage4Hearts() {
    const container = document.getElementById('gallery-hearts-container');
    if (!container) return;
    
    container.innerHTML = '';
    
    const heartInterval = setInterval(() => {
        if (document.getElementById('page4').classList.contains('active')) {
            createGalleryFloatingHeart();
        } else {
            clearInterval(heartInterval);
        }
    }, 500);
}

function createGalleryFloatingHeart() {
    const container = document.getElementById('gallery-hearts-container');
    if (!container) return;
    
    const heart = document.createElement('div');
    heart.className = 'floating-heart';
    heart.textContent = '❤️';
    
    const randomX = Math.random() * window.innerWidth;
    const randomSize = Math.random() * 20 + 15;
    const randomDuration = Math.random() * 2 + 3;
    const randomDirection = Math.random() * 100 - 50;
    
    heart.style.left = randomX + 'px';
    heart.style.bottom = '-50px';
    heart.style.fontSize = randomSize + 'px';
    heart.style.animation = `float ${randomDuration}s ease-in forwards`;
    heart.style.setProperty('--tx', randomDirection + 'px');
    
    container.appendChild(heart);
    
    setTimeout(() => {
        heart.remove();
    }, randomDuration * 1000);
}

function createFloatingHeart() {
    const container = document.getElementById('floating-hearts-container');
    if (!container) return;
    
    const heart = document.createElement('div');
    heart.className = 'floating-heart';
    heart.textContent = '❤️';
    
    const randomX = Math.random() * window.innerWidth;
    const randomSize = Math.random() * 20 + 15; // 15-35px
    const randomDuration = Math.random() * 2 + 3; // 3-5s
    const randomDirection = Math.random() * 100 - 50; // -50 to 50
    
    heart.style.left = randomX + 'px';
    heart.style.bottom = '-50px';
    heart.style.fontSize = randomSize + 'px';
    heart.style.animation = `float ${randomDuration}s ease-in forwards`;
    
    // Custom animation with random horizontal movement
    heart.style.setProperty('--tx', randomDirection + 'px');
    
    container.appendChild(heart);
    
    // Remove heart after animation completes
    setTimeout(() => {
        heart.remove();
    }, randomDuration * 1000);
}

// Add custom property for horizontal movement
const style = document.createElement('style');
style.textContent = `
    @keyframes float {
        to {
            transform: translateY(-100vh) translateX(var(--tx, 0)) rotate(360deg);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ==================== CLOSE APP ====================
function closeModal() {
    const modal = document.getElementById('modal');
    if (modal) {
        modal.style.display = 'none';
    }
}

function closeApp() {
    // You can customize this behavior:
    // Option 1: Show final message
    // alert('Terima kasih telah menggunakan Valentine\'s Day Adventure App 💕');

    // Option 2: Reload page
    location.reload();

    // Option 3: Go back to page 1
    // goToPage(1);

    // For deployed websites, you might want to close the tab:
    // window.close(); // (only works if opened via javascript)
}

// ==================== ACCESSIBILITY ENHANCEMENTS ====================

// Focus management for modal
function manageFocus(pageNumber) {
    if (pageNumber === 1) {
        // Focus on password input
        const passwordInput = document.getElementById('password-input');
        if (passwordInput) {
            setTimeout(() => passwordInput.focus(), 100);
        }
    } else if (pageNumber === 2) {
        // Focus on Valentine question button
        const firstButton = document.querySelector('#page2 .valentine-buttons .btn');
        if (firstButton) {
            setTimeout(() => firstButton.focus(), 100);
        }
    } else if (pageNumber === 3) {
        // Focus on messenger bubble
        const messengerBubble = document.getElementById('messenger-bubble');
        if (messengerBubble) {
            setTimeout(() => messengerBubble.focus(), 100);
        }
    } else if (pageNumber === 4) {
        // Focus on letter title
        const letterTitle = document.querySelector('#page4 .letter-title');
        if (letterTitle) {
            setTimeout(() => letterTitle.focus(), 100);
        }
    } else if (pageNumber === 5) {
        // Focus on sad message
        const sadMessage = document.querySelector('#page5 .sad-message');
        if (sadMessage) {
            setTimeout(() => sadMessage.focus(), 100);
        }
    }
}

// Announce page changes to screen readers
function announcePageChange(pageNumber) {
    const announcement = document.createElement('div');
    announcement.setAttribute('role', 'status');
    announcement.setAttribute('aria-live', 'polite');
    announcement.setAttribute('aria-atomic', 'true');
    announcement.className = 'sr-only';
    
    let pageTitle = '';
    if (pageNumber === 1) pageTitle = 'Password entry page';
    if (pageNumber === 2) pageTitle = 'Valentine question page';
    if (pageNumber === 3) pageTitle = 'Gallery page';
    if (pageNumber === 4) pageTitle = 'Love letter page';
    if (pageNumber === 5) pageTitle = 'Sad ending page';
    
    announcement.textContent = `Navigated to ${pageTitle}`;
    document.body.appendChild(announcement);
    
    setTimeout(() => announcement.remove(), 1000);
}

// ==================== KEYBOARD NAVIGATION ====================
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        // Go back to page 1 on Escape
        goToPage(1);
    }
    
    // Tab navigation (automatic by browser)
    // Arrow keys for page navigation (optional)
    if (event.key === 'ArrowRight') {
        const currentPage = parseInt(document.querySelector('.page.active').id.replace('page', ''));
        if (currentPage < 3) {
            event.preventDefault();
            goToPage(currentPage + 1);
        }
    }
    
    if (event.key === 'ArrowLeft') {
        const currentPage = parseInt(document.querySelector('.page.active').id.replace('page', ''));
        if (currentPage > 1) {
            event.preventDefault();
            goToPage(currentPage - 1);
        }
    }
});

// ==================== INITIALIZATION ====================
document.addEventListener('DOMContentLoaded', function() {
    // Initialize music control
    initializeMusic();
    
    // Initialize password button state
    updatePasswordButtonState();
    
    // Start on page 1
    goToPage(1);
    
    console.log('Valentine\'s Day Adventure App Started! 💕');
    console.log('Password hint: C.I.N.T.A');
});

// ==================== TOUCH/MOBILE SUPPORT ====================
let touchStartY = 0;

document.addEventListener('touchstart', function(e) {
    touchStartY = e.touches[0].clientY;
}, false);

document.addEventListener('touchend', function(e) {
    let touchEndY = e.changedTouches[0].clientY;
    
    // Swipe up: go to next page
    if (touchStartY - touchEndY > 50) {
        const currentPage = parseInt(document.querySelector('.page.active').id.replace('page', ''));
        if (currentPage < 4) {
            // Only auto-advance with button clicks, not swipes
        }
    }
}, false);

// ==================== SMOOTH SCROLLING ====================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// ==================== UTILITY: Detect Page Change ====================
const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        const activePage = document.querySelector('.page.active');
        if (activePage) {
            console.log('Current page:', activePage.id);
        }
    });
});

// Optional: uncomment to enable page change logging
// observer.observe(document.body, {
//     subtree: true,
//     attributes: true,
//     attributeFilter: ['class']
// });

// ==================== DEBUGGING ====================
window.debugInfo = function() {
    console.log('=== Valentine\'s Day Adventure - Debug Info ===');
    console.log('Current Pages:', document.querySelectorAll('.page').length);
    console.log('Active Page:', document.querySelector('.page.active').id);
    console.log('Window Size:', window.innerWidth + 'x' + window.innerHeight);
    console.log('Viewport:', {
        width: window.innerWidth,
        height: window.innerHeight
    });
};

// ==================== PERFORMANCE OPTIMIZATION ====================
// Reduce animation complexity on low-end devices
function detectPerformance() {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) {
        document.body.style.setProperty('--animation-duration', '0s');
    }
}

detectPerformance();

// ==================== ACCESSIBILITY ====================
// Add focus management for keyboard navigation
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('focus', function() {
        this.style.outline = '2px solid #FFD700';
    });
    
    button.addEventListener('blur', function() {
        this.style.outline = 'none';
    });
});

// ==================== RESPONSIVE =================
window.addEventListener('resize', function() {
    // Handle window resize if needed
    console.log('Window resized:', window.innerWidth + 'x' + window.innerHeight);
});

// ==================== PAGE TRANSITIONS ====================
// Add smooth transitions between pages
function transitionToPage(pageNumber) {
    const currentPage = document.querySelector('.page.active');
    if (currentPage) {
        currentPage.style.transition = 'opacity 0.8s ease-out';
    }
    
    setTimeout(() => {
        goToPage(pageNumber);
    }, 50);
}

// Export for console use
window.goToPage = goToPage;
window.transitionToPage = transitionToPage;
