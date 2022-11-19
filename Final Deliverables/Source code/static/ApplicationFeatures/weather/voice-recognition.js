let mic = document.getElementById("weathermic");
let searchinput = document.getElementById("search");

mic.addEventListener('click',SpeechRecognition) 
function SpeechRecognition() {
  function vibrate(ms) {
    navigator.vibrate(ms);
  }
  vibrate(2000);

  let recognition = new webkitSpeechRecognition();
  // let recognition = new SpeechRecognition();
  recognition.onstart = () => {
      // toast
  Toastify({
    text: "We are listening you !",
    duration: 2000,
    newWindow: true,
    gravity: "top", // `top` or `bottom`
    position: "center", // `left`, `center` or `right`
    stopOnFocus: true, // Prevents dismissing of toast on hover
    style: {
      background: "linear-gradient(to right, #00b09b, #96c93d)",
    },
    onClick: function(){} // Callback after click
  }).showToast();
  };

  recognition.onresult = (event) => {
    var transcripts = event.results[0][0].transcript;
    console.log(transcripts);
    searchinput.value = "";
    searchinput.value = transcripts;
  };

  recognition.onspeechend = () => {
    recognition.stop();
             // toast
  Toastify({
    text: "Speech recognition ended",
    duration: 4000,
    newWindow: true,
    gravity: "top", // `top` or `bottom`
    position: "center", // `left`, `center` or `right`
    stopOnFocus: true, // Prevents dismissing of toast on hover
    style: {
      background: "red",
    },
    onClick: function(){} // Callback after click
  }).showToast();          
  };

  recognition.start();

}


searchinput.addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    // code for enter
    if(!navigator.onLine){
        Toastify({
          text: "You are offline",
          duration: 4000,
          newWindow: true,
          gravity: "bottom", // `top` or `bottom`
          position: "center", // `left`, `center` or `right`
          stopOnFocus: true, // Prevents dismissing of toast on hover
          style: {
            background: "red",
          },
          onClick: function(){} // Callback after click
        }).showToast(); 
      }
  }
});