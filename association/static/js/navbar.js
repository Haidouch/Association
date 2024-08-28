const show = document.querySelector("#nav");
var navMobile = document.querySelector(".desktop");
show.addEventListener('click', () => {
        navMobile.classList.toggle('mobile-menu');
});

