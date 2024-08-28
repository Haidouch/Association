
function repition(){
    var div = document.getElementById("div");
        div.innerHTML = '<img src="static/img/img3.jpg" alt="img1">';
        setTimeout(function(){
            div.innerHTML = '<img src="static/img/img7.jpg" alt="img2">';
        },3000);
        setTimeout(function(){
            div.innerHTML = '<img src="static/img/img8.jpg" alt="img3">';
        },6000);
        setTimeout(repition, 9000);
    }
    window.addEventListener("load", repition());
    
    var all = document.getElementById("all");
    var little = document.getElementById("little");
    var gallery = document.querySelector(".gallery");
    var about = document.querySelector(".about");
    var service = document.querySelector(".service");
    var imgs = document.getElementsByClassName("img");
    var imgs4 = document.getElementById("imgs4");
    document.getElementById("al").style.display = "none";
    document.querySelector(".about").style.background = "#eee5e5";
    document.getElementsByTagName("section")[0].style.backgroundImage = "url('/static/img/img13.jpg')";

    imgs4.innerHTML = "";
    for (let i = 0; i < 4; i++) {
       imgs4.appendChild(imgs[i].cloneNode(true));
    }

all.onclick = function() {
    about.style.display = "none";
    service.style.display = "none";
    all.style.display = "none";
    all.style.display = "none";
    little.style.display = "block";
    gallery.style.inset = "0";
    gallery.style.backdropFilter = "blur(15px)";
    document.getElementById("al").style.display = "block";
    
    imgs4.style.display = "none";
}

little.onclick = function() {
    about.style.display = "block";
    service.style.display = "block";
    all.style.display = "block";
    little.style.display = "none"; 
    gallery.style.inset = "0";
    gallery.style.backdropFilter = "blur(0)";
    document.getElementById("al").style.display = "none";
    imgs4.style.display = "block";
}