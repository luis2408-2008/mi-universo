// Main JavaScript file for Explorador Cósmico

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }
    
    // Flash message close button
    const closeButtons = document.querySelectorAll('.close-flash');
    
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const flashMessage = this.closest('.flash-message');
            if (flashMessage) {
                flashMessage.style.opacity = '0';
                setTimeout(() => {
                    flashMessage.remove();
                }, 300);
            }
        });
    });
    
    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.flash-message');
    
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });
    
    // Poll option selection
    const pollOptions = document.querySelectorAll('.bg-space-purple\\/20.cursor-pointer');
    
    pollOptions.forEach(option => {
        option.addEventListener('click', function() {
            // Remove selection from all options
            pollOptions.forEach(opt => {
                const radio = opt.querySelector('.h-2.w-2');
                if (radio) {
                    radio.classList.add('invisible');
                }
            });
            
            // Select the clicked option
            const radio = this.querySelector('.h-2.w-2');
            if (radio) {
                radio.classList.remove('invisible');
            }
        });
    });
    
    // Poll vote button
    const voteButton = document.querySelector('button[type="button"]');
    
    if (voteButton) {
        voteButton.addEventListener('click', function() {
            let selected = false;
            
            pollOptions.forEach(option => {
                const radio = option.querySelector('.h-2.w-2');
                if (radio && !radio.classList.contains('invisible')) {
                    selected = true;
                }
            });
            
            if (selected) {
                // Flash a "thank you" message
                const pollSection = voteButton.closest('section');
                const thankYouMessage = document.createElement('div');
                thankYouMessage.className = 'mt-4 py-2 px-4 bg-space-accent text-white rounded-lg animate-float';
                thankYouMessage.textContent = '¡Gracias por tu voto!';
                
                if (pollSection) {
                    voteButton.parentNode.appendChild(thankYouMessage);
                    
                    // Disable the button
                    voteButton.disabled = true;
                    voteButton.classList.add('opacity-50', 'cursor-not-allowed');
                    
                    // Remove the message after 3 seconds
                    setTimeout(() => {
                        thankYouMessage.remove();
                    }, 3000);
                }
            }
        });
    }
});
