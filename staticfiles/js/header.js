document.addEventListener("DOMContentLoaded", function () {
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
});
