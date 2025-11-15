document.addEventListener("DOMContentLoaded", function () {

    const trigger = document.getElementById("countryTrigger");
    const menu = document.getElementById("countryMenu");

    if (trigger && menu) {

        trigger.addEventListener("click", function (e) {
            e.stopPropagation();
            menu.classList.toggle("show");
        });

        document.addEventListener("click", function (e) {
            if (!trigger.contains(e.target)) {
                menu.classList.remove("show");
            }
        });

        menu.addEventListener("click", function (e) {
            e.stopPropagation();
        });
    }
});
