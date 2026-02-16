document.addEventListener("DOMContentLoaded", () => {
    
    // ============================================
    // 1. LIGHT/DARK MODE LOGIKASI
    // ============================================
    const themeBtn = document.getElementById('themeSwitch');
    
    // Agar tugma sahifada bor bo'lsa (xatolikni oldini olish uchun)
    if (themeBtn) {
        const icon = themeBtn.querySelector('i');

        // 1. Sayt yuklanganda xotiradagi (localStorage) rejimni o'qish
        const savedTheme = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-theme', savedTheme);

        // Ikonkani to'g'irlash (Dark = Oy, Light = Quyosh)
        if (savedTheme === 'light') {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }

        // 2. Tugma bosilganda rejimni o'zgartirish
        themeBtn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            // HTML atributini va xotirani yangilash
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);

            // Ikonkani almashtirish
            if (newTheme === 'light') {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            } else {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            }
        });
    }


});