var splide = new Splide( '.splide', {
  type   : 'loop',
  padding: '5rem',
} );

splide.mount();

/* submenu */
// mouseover, click, mousedown, mouseout
document.querySelector("#sistema").addEventListener('click', function(e){
  e.preventDefault();  // Corrige o preventDefault
  
  let sub = document.querySelector('#submenu-empresa');  // Corrige a variável

  // Alterna a visibilidade do submenu
  if (sub.style.display === 'block') {
    sub.style.display = 'none';
  } else {
    sub.style.display = 'block';
  }
});