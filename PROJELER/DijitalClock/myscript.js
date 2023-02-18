let panel = document.querySelector('#panel') ;

setInterval(() => {
    let time = new Date() ;
    panel.innerHTML = time ;
}, 1000) ;

