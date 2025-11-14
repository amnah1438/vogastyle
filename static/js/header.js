// فتح / إغلاق قائمة اللغة
document.addEventListener("DOMContentLoaded", function () {

    const btn = document.querySelector(".vg-lang-btn");
    const menu = document.querySelector(".vg-lang-menu");

    if (btn && menu) {

        btn.addEventListener("click", function (e) {
            e.stopPropagation();
            menu.style.display = (menu.style.display === "block") ? "none" : "block";
        });

        // إغلاق القائمة عند الضغط خارجها
        document.addEventListener("click", function () {
            menu.style.display = "none";
        });
    }

});
