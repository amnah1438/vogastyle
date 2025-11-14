// =============================================
//   1) فتح وإغلاق قائمة الدول (Dropdown)
// =============================================
document.addEventListener("DOMContentLoaded", function () {

    const trigger = document.getElementById("countryTrigger"); // زر الدولة
    const menu = document.getElementById("countryMenu");       // قائمة الدول

    if (trigger && menu) {

        // فتح/إغلاق القائمة عند الضغط على الزر
        trigger.addEventListener("click", function (e) {
            e.stopPropagation();
            menu.classList.toggle("show");
        });

        // إغلاق عند الضغط خارج القائمة
        document.addEventListener("click", function (e) {
            if (!trigger.contains(e.target) && !menu.contains(e.target)) {
                menu.classList.remove("show");
            }
        });

        // منع الإغلاق عند الضغط داخل القائمة
        menu.addEventListener("click", function (e) {
            e.stopPropagation();
        });
    }
});
