
function repition(){
    var div = document.getElementById("div");
        div.innerHTML = '<img src="static/img/about.jpg" alt="img1">';
        setTimeout(function(){
            div.innerHTML = '<img src="static/img/about1.jpg" alt="img2">';
        },3000);
        setTimeout(repition, 6000);
    }
    window.addEventListener("load", repition());
     // Assuming "nbrImages" is a collection of elements

little.onclick = function() {
    about.style.display = "block";
    service.style.display = "block";
    all.style.display = "block";
    little.style.display = "none"; 
    allImage.style.display = "none";
    imgs4.style.display = "block";
}
document.addEventListener('DOMContentLoaded', function() {
    var gallery = document.querySelector(".gallery");
    var about = document.querySelector(".about");
    var service = document.querySelector(".service");
    var contact = document.querySelector(".contacte");
    let all = document.getElementById("all");
    let little = document.getElementById("little");
    let imgs4 = document.getElementById("imgs4");
    let allImage = document.getElementById("al").getElementsByTagName("img");

    document.getElementById("al").style.display = "none";
    var k = 3;
    for (let i = 0; i < k; i++) {
        imgs4.appendChild(allImage[i].cloneNode(true));
    }
    imgs4.style.display = "block";

    all.onclick = function() {
        all.style.display = "none";
        little.style.display = "block";
        document.getElementById("al").style.display = "block";
        imgs4.style.display = "none";
        about.style.display = "none";
        service.style.display = "none";
        contact.style.display = "none";
        gallery.style.inset = "0";
        gallery.style.backdropFilter = "blur(15px)";
    }

    little.onclick = function() {
        all.style.display = "block";
        little.style.display = "none"; 
        document.getElementById("al").style.display = "none";
        imgs4.style.display = "block";
        about.style.display = "block";
        service.style.display = "block";
        contact.style.display = "block";
        gallery.style.inset = "0";
        gallery.style.backdropFilter = "blur(0)";
    }
});
