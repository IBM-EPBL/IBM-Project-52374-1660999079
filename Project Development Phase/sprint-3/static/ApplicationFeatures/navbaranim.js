var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-90px";
    document.getElementById("navbar").style.transition =
      "0.5s ease-in-out";
  }
  prevScrollpos = currentScrollPos;
};