const imageInput = document.getElementById("image");
const previewImg = document.getElementById("previewImg");
const form = document.getElementById("productForm");

imageInput.addEventListener("change", () => {
    const file = imageInput.files[0];
    if (file) {
        previewImg.src = URL.createObjectURL(file);
        previewImg.style.display = "block";
    }
});

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const data = {
        title: document.getElementById("title").value,
        description: document.getElementById("description").value,
        price: document.getElementById("price").value,
        discount: document.getElementById("discount").value,
        category: document.getElementById("category").value,
        is_active: document.getElementById("isActive").checked
    };

    console.log("Mahsulot ma'lumotlari:", data);
    alert("Mahsulot saqlandi (frontend demo) ✅");
});
