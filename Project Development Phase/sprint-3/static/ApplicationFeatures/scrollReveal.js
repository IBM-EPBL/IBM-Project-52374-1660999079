ScrollReveal().reveal('.news-container', { delay: 300 ,duration: 300,
    reset: true });

// progress bar 
let prog = document.getElementById('progress');

let body = document.body,
    html = document.documentElement;

let height = Math.max(
    body.scrollHeight,
    body.offsetHeight,
    html.clientHeight,
    html.scrollHeight,
    html.offsetHeight
);

const setProgress = () => {
    let scrollFromTop = (html.scrollTop || body.scrollTop) + html.clientHeight;
    let width = (scrollFromTop / height) * 100 + '%';

    prog.style.width = width;
};

window.addEventListener('scroll', setProgress);

setProgress();

// Scroll to top btn
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}