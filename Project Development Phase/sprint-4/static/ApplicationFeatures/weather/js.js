let box1 =document.querySelector('.box_1');
let lat =document.getElementById('lat');
let long =document.getElementById('long');
const KELVIN = 273;
//declare variables 
var  lati = document.getElementById('lat');
var  longi = document.getElementById('long');
var  status = document.querySelector('.status');
var  place = document.getElementById('place');
var  country = document.getElementById('Country');
var  block1 =document.querySelector('.block1');
var  celsius = document.getElementById('celsius');
var  descriptiopn = document.getElementById('descriptiopn');
var  pressure = document.getElementById('pressure');
var  humidity = document.getElementById('humidity');
var  searchText = document.getElementById('search');
var locationLatitude = document.getElementById('locationLatitude');
var locationLongitude = document.getElementById('locationLongitude');
var region = document.getElementById('region');
var zone = document.getElementById('zone');
var lastUpdated = document.getElementById('lastUpdated');
var windDirection =document.getElementById('windDirection');
var country=document.getElementById('country');
var sun=document.getElementById('sun');
//check geolocation 
  if('geolocation' in navigator){
      navigator.geolocation.getCurrentPosition(setPosition,showError);
      console.log("checked ");
  }else{
    swal("Your Browser Doesn't support geolocation");
    }
    //set user's position 
 function setPosition(position){
     let latitude = position.coords.latitude;
     let longitude = position.coords.longitude;  
     console.log(`${latitude} , ${longitude}`);
     lat.innerText =`${latitude}`;
     long.innerText=`${longitude}`; 
 }
 //show error when when there is an occuring issue with geolocation service
 function showError(error){
        console.error(error);
 }
 const weather = {
  temparature:{
    value :18,
    unit: "celsius"
  },
  description : "",
  iconId : "",
  city : "",
  country : "",
  latitude :"",
  longitude :""
}
let gobtn = document.querySelector('.go');
gobtn.addEventListener('click',()=>{
var cityName = document.getElementById('search').value;
fetch(`http://api.weatherapi.com/v1/current.json?key=9bb24752152641ceb73145704221806&q=${cityName}`)
.then(response => response.json())
.then(data =>{
  console.log(data);
  weather.temparature.value = data.current.temp_c;
  weather.image = data.current.condition.icon;
  weather.description = data.current.condition.text;
  weather.windDirection = data.current.wind_dir;
  weather.lastUpdated = data.current.last_updated;
  weather.windSpeed = data.current.wind_mph;
  weather.humidity =data.current.humidity;
  weather.pressure =data.current.pressure_mb;
 //  location data
  weather.locationLatitude =data.location.lat;
  weather.locationLongitude =data.location.lon;
  weather.country =data.location.country;
  weather.placeName =data.location.name;
  weather.region = data.location.region;
  weather.zone = data.location.tz_id;
  // update the HTML page 
  celsius.innerHTML = `<h3>${weather.temparature.value}<sup>o</sup>C</h3>`;
  description.innerText = weather.description;

  locationLatitude.innerHTML=` ${weather.locationLatitude}`;
  locationLongitude.innerHTML=` ${weather.locationLongitude}`;

  region.innerHTML=`<h5 style="color:orange;">Region : ${weather.region}</h5>`;
  zone.innerHTML=`<h3>Zone : ${weather.zone}</h3>`;
  lastUpdated.innerHTML=`Last updated : ${weather.lastUpdated}</h3>`;
  country.innerHTML =`<h3 style="color:orange;">Country :${weather.country}</h3>`;
  windDirection.innerHTML=`<h5>${weather.windDirection}</h5>`;

  pressure.innerHTML =`${weather.pressure} mbar`;
  windspeed.innerHTML =` ${weather.windSpeed} Km/h`;
  humidity.innerHTML =` ${weather.humidity}%`;
});  
});