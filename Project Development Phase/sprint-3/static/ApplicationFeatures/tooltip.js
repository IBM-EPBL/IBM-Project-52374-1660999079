$(document).ready(function(){
    $('[data-bs-toggle="tooltip"]').tooltip();   
  });

  $(document).ready(function(){
  $('[data-bs-toggle="popover"]').popover();   
  });

  var myModalEl = document.getElementById('myModal')
myModalEl.addEventListener('click', function () {
  // do something...
  myModalEl.show()
})
  

$(document).ready(function(){
  $('[data-bs-toggle="modal"]').show();   
  });