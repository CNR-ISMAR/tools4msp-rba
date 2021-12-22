function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("btn1");

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "<i class='fas fa-chevron-right'></i>";
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        btnText.innerHTML = "<i class='fas fa-chevron-left'></i>";
        moreText.style.display = "inline";
    }
}

function myFunction2() {
    var dots2 = document.getElementById("dots2");
    var moreText2 = document.getElementById("more2");
    var btnText2 = document.getElementById("btn2");

    if (dots2.style.display === "none") {
        dots2.style.display = "inline";
        btnText2.innerHTML = "<i class='fas fa-chevron-right'></i>";
        moreText2.style.display = "none";
    } else {
        dots2.style.display = "none";
        btnText2.innerHTML = "<i class='fas fa-chevron-left'></i>";
        moreText2.style.display = "inline";
    }
}

function myFunction3() {
    var dots3 = document.getElementById("dots3");
    var moreText3 = document.getElementById("more3");
    var btnText3 = document.getElementById("btn3");

    if (dots3.style.display === "none") {
        dots3.style.display = "inline";
        btnText3.innerHTML = "<i class='fas fa-chevron-right'></i>";
        moreText3.style.display = "none";
    } else {
        dots3.style.display = "none";
        btnText3.innerHTML = "<i class='fas fa-chevron-left'></i>";
        moreText3.style.display = "inline";
    }
}