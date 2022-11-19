window.addEventListener('online',deviceStatus);
window.addEventListener('offline',deviceStatus);
function deviceStatus() {
if (navigator.onLine){
swal({
    title: "We are back !",
    text: "Good to go",	
    icon: "success",
    button: "continue",
    });
}
else{
swal({
    title: "Internet not connected!",
    text: "Some features are may not work so please connect to the internet",
    icon: "warning",
    button: "continue",
    });
}
}