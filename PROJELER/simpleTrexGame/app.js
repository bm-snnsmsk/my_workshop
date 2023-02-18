let chr = document.querySelector('#character');
let blc = document.querySelector('#block');

function jump(){
    if(chr.classList != 'animate'){
        chr.classList.add('animate') ;
    }
    setTimeout(function(){
       chr.classList.remove('animate') ;
    },500)
}

let gameOver = setInterval(function(){
    let cTop = parseInt(window.getComputedStyle(chr).getPropertyValue('top'));
    let bLeft = parseInt(window.getComputedStyle(blc).getPropertyValue('left'));
    // console.log("cTop : " + cTop + " --- bLeft : " + bLeft) ;
    if(bLeft < 20 && bLeft > 0 && cTop >= 130){
        blc.style.animation = "none" ;
        blc.style.display = "none" ;
        alert("Game Over !") ;
    }
},10) ;

function startGame(){
    if(blc.style.display = "none"){
        blc.style.display = "block" ;
    }
        blc.classList.add('game') ;
}


setInterval(() => {
    let birTop = parseInt(getComputedStyle(chr).getPropertyValue('top'));
    let ikiLeft = parseInt(getComputedStyle(blc).getPropertyValue('left'));
    let ikiTop = parseInt(getComputedStyle(blc).getPropertyValue('top'));
    demo.innerHTML = "top : " + birTop + " - " + ikiTop +"<br/>left : "+ ikiLeft +'<br/><br/>' ;
},1) ;