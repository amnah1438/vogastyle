// =============================
//   فتح / إغلاق قائمة اللغة
// =============================

document.addEventListener("DOMContentLoaded", function () {

    const btn = document.querySelector(".vg-lang-btn");
    const menu = document.querySelector(".vg-lang-menu");

    if (btn && menu) {

        // فتح/إغلاق القائمة عند الضغط على زر اللغة
        btn.addEventListener("click", function (e) {
            e.stopPropagation();   // منع انتشار الحدث
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

    const langText = document.querySelector(".vg-lang-text");
    const langForm = document.querySelector(".lang-form");

    if (langText && langForm) {
        langText.addEventListener("click", function () {
            langForm.submit();   // إرسال فورم تغيير اللغة
        });
    }

});


// =============================
//   إغلاق القائمة عند الضغط خارج زر العلم
// =============================

document.addEventListener("click", function (e) {

    const container = document.querySelector(".vg-language-dropdown");
    const menu = document.querySelector(".vg-lang-menu");

    if (container && menu) {
        if (!container.contains(e.target)) {
            menu.style.display = "none";
        }
    }

});
