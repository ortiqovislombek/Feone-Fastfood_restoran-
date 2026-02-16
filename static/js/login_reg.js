document.addEventListener("DOMContentLoaded", () => {
    // 1. Sliding Logic (O'zgarmadi)
    const wrapper = document.getElementById('formWrapper');
    const toggleBtn = document.getElementById('toggleBtn');
    const toggleHeading = document.getElementById('toggleHeading');
    const toggleText = document.getElementById('toggleText');

    toggleBtn.addEventListener('click', () => {
        wrapper.classList.toggle('active');

        if(wrapper.classList.contains('active')){
            toggleHeading.textContent = "Already have an account?";
            toggleText.textContent = "Login to your account!";
            toggleBtn.textContent = "Login";
        } else {
            toggleHeading.textContent = "Don't have an account?";
            toggleText.textContent = "Sign up to get started!";
            toggleBtn.textContent = "Sign Up";
        }
    });

    // 2. Theme Switcher Logic (Yangi qo'shildi)
    const themeSwitch = document.getElementById('themeSwitch');
    const icon = themeSwitch.querySelector('i');

    // Xotiradan o'qish
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    icon.className = savedTheme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';

    themeSwitch.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        icon.className = newTheme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
    });
});