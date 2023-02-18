let test = document.querySelector("#test") ;
let block = document.querySelector("#block") ;
let character = document.querySelector("#character") ;
let hole = document.querySelector("#hole") ;
let jumping = 0 ;
let counter = 0 ;

hole.addEventListener('animationiteration', () => {
    let random = Math.random() * 3;
    let top = (random * 100) + 150 ;
    hole.style.top = -(top) + "px" ;
    counter++ ;
}) ;

setInterval(() => {
    let cTop = parseInt(getComputedStyle(character).getPropertyValue('top')) ;
   if(jumping == 0){
     character.style.top = (cTop + 3) + 'px'  ;
   }
   let bLeft = parseInt(getComputedStyle(block).getPropertyValue('left')) ;
   let hTop = parseInt(getComputedStyle(hole).getPropertyValue('top')) ;
   let chrTop = -(500 - cTop) ;
   if((cTop > 480) || ((bLeft < 20) && (bLeft > -50) && ((chrTop < hTop) || (chrTop > hTop + 130)))){
    alert("Game Over ! Skorunuz : " + counter) ;
    character.style.top = 100 + 'px'  ;
    counter = 0 ;
   }
   // test.innerHTML = 'cTop : '+cTop + '<br/>bleft : '+ bLeft+'<br/>htop : '+ hTop + '<br/>chrTop : '+ chrTop ;
} ,10) ;
 
function jump(){
    jumping = 1 ;
    let jumpCount = 0 ;
    let jumpInterval = setInterval(() => {
        let cTop = parseInt(getComputedStyle(character).getPropertyValue('top')) ;
       if((cTop > 6) && jumpCount < 15){
            character.style.top = (cTop - 3) + 'px'  ;
       }
       if(jumpCount > 20){
        clearInterval(jumpInterval) ;
        jumping = 0 ;
        jumpCount = 0 ;
    }
    jumpCount++ ;
    },10) ;
    // test.innerHTML = 'jumpCount : '+jumpCount + '<br/>jumping : '+ jumping ;
}




// test alanı
/* setInterval(() => {
    test.innerHTML = getComputedStyle(hole).getPropertyValue('top') ;
},2) ; */