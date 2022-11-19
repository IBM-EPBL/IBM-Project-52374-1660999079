//check geolocation 
if('geolocation' in navigator){
    navigator.geolocation.getCurrentPosition(setPosition,showError);
    console.log("checked ");
}else{
  alert("Your Browser Doesn't support geolocation");
  }
  //set user's position 
function setPosition(position){
   let latitude = position.coords.latitude;
   let longitude = position.coords.longitude;  
   console.log(`${latitude} , ${longitude}`);
  //  lat.innerText =`${latitude}`;
  //  long.innerText=`${longitude}`; 
}
//show error when when there is an occuring issue with geolocation service
function showError(error){
      console.error(error);
}