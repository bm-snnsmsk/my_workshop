// for target addEventListener START
canvas.addEventListener('mousemove', (e) => {
    if(playing){ // init() otomatik çalıştırılmadığı zaman hata vermemesi için if(playing yapıldı)
        let dx = e.pageX - player.x ;
        let dy = e.pageY - player.y ;
            //angle = Math.atan2(dy, dx) ; = radyan 
        let tetha = Math.atan2(dy, dx) ;
            angle = tetha * 180 / Math.PI ;  // radyan to degree
    } 
}) ;
// for target addEventListener END

// for shoot addEventListener START
canvas.addEventListener('click', (e) => {
   if(playing){// init() otomatik çalıştırılmadığı zaman hata vermemesi için if(playing yapıldı)
    bullets.push(new Circle(player.x, player.y, e.pageX, e.pageY, 5, 'rgba(255, 255, 255)', 5)) ;
    // console.log(bullets)
    // console.log(enemies)
   }
}) ;
// for shoot addEventListener END

// for shoot addEventListener START
document.body.addEventListener('keydown', (e) => {
    if(playing){// init() otomatik çalıştırılmadığı zaman hata vermemesi için if(playing yapıldı)     
        switch(e.keyCode){
            case 32 : bullets.push(new Circle(player.x, player.y, e.pageX, e.pageY, 5, 'rgba(255, 255, 255)', 5)) ; break ;
            default : break ;
        }    
    }
}) ;
// for shoot addEventListener END
