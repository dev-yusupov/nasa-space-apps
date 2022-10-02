const headerToggle = document.querySelector("#");
const haederMenu = document.querySelector(".header-menu");

headerToggle.addEventListener("click", function (e) {
    e.preventDefault();
    haederMenu.classList.toggle("menu-active");
});
