const checkbox = document.getElementById('checkbox');
const card = document.querySelector('.card')
checkbox.addEventListener('change', ()=>{
  document.body.classList.toggle('dark');
  document.body.card.classList.toggle('dark');
  document.body.classList.toggle('');

  function vibrate(ms){
    navigator.vibrate(ms);
  }
vibrate(2000)
})
