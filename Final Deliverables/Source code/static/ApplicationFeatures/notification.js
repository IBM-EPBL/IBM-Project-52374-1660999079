function trigger_notification()
{
    //check if browser supports notification API
    if("Notification" in window)
    {
        if(Notification.permission == "granted")
        {
            var notification = new Notification("News Tracker Application", {"body":"Brings you the best location results and mordern UI !", "icon":""});
        }
        else
        {
            Notification.requestPermission(function (permission) {
                if (permission === "granted")
                {
                    var notification = new Notification("Notification API", {"body":"", "icon":"../assets/weathericons/windspeed.png"});
                }
            });
        }
    }    
    else
    {
        alert("Your browser doesn't support notfication API");
    }      
}
trigger_notification();