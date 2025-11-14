// =============================
//   فتح / إغلاق قائمة الدول فقط
// =============================

document.addEventListener("DOMContentLoaded", function () {

    const flagBtn = document.querySelector(".vg-flag-btn"); // زر العلم فقط
    const menu = document.querySelector(".vg-lang-menu");

    if (flagBtn && menu) {

        // فتح/إغلاق القائمة عند الضغط على العلم
        flagBtn.addEventListener("click", function (e) {
            e.stopPropagation();
            menu.style.display = (menu.style.display === "block") ? "none" : "block";
        });

        // إغلاق القائمة عند الضغط خارجها
        document.addEventListener("click", function () {
            menu.style.display = "none";
        });

    }

});


// =============================
//   تبديل اللغة (عربي ↔ English)
// =============================

document.addEventListener("DOMContentLoaded", function () {

    const langText = document.querySelector(".vg-lang-text"); // نص اللغة فقط
    const langForm = document.querySelector(".lang-form");

    if (langText && langForm) {
        langText.addEventListener("click", function (e) {
            e.stopPropagation(); // لا يدخل على قائمة الدول
            langForm.submit();
        });
    }

});


// =============================
//   لمنع إغلاق القائمة عند الضغط داخلها
// =============================

document.addEventListener("DOMContentLoaded", function () {

    const menu = document.querySelector(".vg-lang-menu");

    if (menu) {
        menu.addEventListener("click", function (e) {
            e.stopPropagation(); // يمنع الإغلاق
        });
    }

});
