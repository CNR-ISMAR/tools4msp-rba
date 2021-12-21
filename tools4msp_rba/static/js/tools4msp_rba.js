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
