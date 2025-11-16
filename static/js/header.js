document.addEventListener("DOMContentLoaded", function () {

    /* ============================
       قائمة اختيار الدولة (كودك القديم)
    ============================ */
    const trigger = document.getElementById("vgCountryTrigger");
    const menu = document.getElementById("vgCountryMenu");

    if (trigger && menu) {
        trigger.addEventListener("click", function (e) {
            e.stopPropagation();
            menu.classList.toggle("show");
        });

        document.addEventListener("click", function () {
            menu.classList.remove("show");
        });

        menu.addEventListener("click", function (e) {
            e.stopPropagation();
        });
    }


    /* ============================
       SEARCH OVERLAY — NEW
    ============================ */

    // أيقونة البحث الموجودة في الهيدر
    const searchIcon = document.querySelector('.vg-icons img[src*="search.svg"]');

    // الـ Overlay نفسه
    const overlay = document.getElementById('vgSearchOverlay');

    // زر الإغلاق ×
    const closeBtn = document.getElementById('vgSearchClose');

    // فتح البحث عند الضغط على الأيقونة
    if (searchIcon && overlay) {
        searchIcon.addEventListener('click', () => {
            overlay.classList.add("show");
        });
    }

    // إغلاق عند الضغط على ×
    if (closeBtn && overlay) {
        closeBtn.addEventListener('click', () => {
            overlay.classList.remove("show");
        });
    }

    // إغلاق عند الضغط خارج مربع البحث
    if (overlay) {
        overlay.addEventListener("click", (e) => {
            if (e.target === overlay) {
                overlay.classList.remove("show");
            }
        });
    }

});
