document.addEventListener("DOMContentLoaded", function () {
    
    /* ------------------------------------------------
       1. THEME SWITCHER (Dark/Light Mode)
    ------------------------------------------------ */
    const themeBtn = document.getElementById("themeSwitch");
    const themeIcon = themeBtn.querySelector("i");
    const htmlTag = document.documentElement;

    // Saqlangan mavzuni tekshirish
    const currentTheme = localStorage.getItem("theme") || "dark";
    applyTheme(currentTheme);

    themeBtn.addEventListener("click", () => {
        const newTheme = htmlTag.getAttribute("data-theme") === "dark" ? "light" : "dark";
        applyTheme(newTheme);
        localStorage.setItem("theme", newTheme);
    });

    function applyTheme(theme) {
        if (theme === "light") {
            htmlTag.setAttribute("data-theme", "light");
            themeIcon.classList.remove("fa-moon");
            themeIcon.classList.add("fa-sun");
        } else {
            htmlTag.setAttribute("data-theme", "dark");
            themeIcon.classList.remove("fa-sun");
            themeIcon.classList.add("fa-moon");
        }
    }

});

/* ------------------------------------------------
   2. IMAGE PREVIEW (Modalda rasm ko'rsatish)
------------------------------------------------ */
function previewFile() {
    const preview = document.getElementById('previewImg');
    const fileInput = document.getElementById('productImage');
    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    } else {
        // Agar fayl tanlanmasa, standart rasmga qaytish
        preview.src = "https://via.placeholder.com/300x300?text=Rasm+Tanlash";
    }
}