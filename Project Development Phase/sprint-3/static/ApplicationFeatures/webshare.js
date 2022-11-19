var TitleHeading ="News Tracker Application";
var url =window.href;
var shareBtn =document.getElementById('tabsharebtn');
        
        shareBtn.addEventListener('click',()=>{
            if(navigator.share){
                navigator.share({
                    title :`${TitleHeading}`,
                    url :`${url}`
                }).then(()=>{
                    console.log("share finished successfully");
                }).catch(console.error)
            }else{
                alert("Share failed webshare API does not support");
            }
        })
        