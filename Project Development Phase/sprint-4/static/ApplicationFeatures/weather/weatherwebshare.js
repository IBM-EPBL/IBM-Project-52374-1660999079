var TitleHeading ="Weather by News Tracker";
var url =window.href;
var shareBtn =document.getElementById('share-btn');
        
        shareBtn.addEventListener('click',()=>{
            if(navigator.share){
                navigator.share({
                    title :`${TitleHeading}`,
                    url :`${url}`
                }).then(()=>{
                    console.log("share finished successfully");
                }).catch(console.error)
            }else{
                // alert("Share failed webshare API does not support");
                swal({
                    title: "Share failed webshare API does not support",
                    icon: "warning",
                    button: "continue",
                    });
            }
        })
        