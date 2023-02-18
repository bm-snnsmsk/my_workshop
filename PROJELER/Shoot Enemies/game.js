const startbtn = document.querySelector('#start button') ;
const startprgrf = document.querySelector('#start p') ;
const startdiv = document.querySelector('#start') ;
const scorediv = document.querySelector('#score') ;
const killsdiv = document.querySelector('#kills') ;
const canvas = document.querySelector('#canvas') ;
const width = window.innerWidth;
const height = window.innerHeight ;
canvas.width = width ;
canvas.height = height ;
const ctx = canvas.getContext('2d') ; 

ctx.clearRect(0, 0, width, height) ;

// definetion variables START
    let player ;     
    let playing = false ;
    let angle ;
    let bullets ;
    let enemies ;
    let maxenemies;
    let score ;
    let kills  ;
// definetion variables END



function animate(){
    if(playing){
        requestAnimationFrame(animate) ;
        //ctx.clearRect(0, 0, width, height) ; // effect için yoruma alındı
        // effect START
        ctx.fillStyle = "rgba(0, 0, 0, .3)" ;    
        ctx.fillRect(0, 0, width, height) ;    
        ctx.fill() ;
        // effect END
        enemies.forEach((enemy, e) => {  // enemy çiz            
            bullets.forEach((bullet, b) => {  // mermi düşman çarpışması
                if(collision(enemy.x, enemy.y, enemy.radius, bullet.x, bullet.y, bullet.radius)){
                    if(enemy.radius < 10){
                        enemies.splice(e, 1) ;
                        score+=25 ;
                        kills++ ;
                        if(kills % 5 == 0){
                            maxenemies++ ;
                        }
                        addEnemy();
                    }else{
                        enemy.radius -= 7 ;
                        score+=5 ;
                    }
                    bullets.splice(b, 1) ;                    
                }
            }) ; 
                // düşman oyuncu çarpışması için
            if(collision(enemy.x, enemy.y, enemy.radius, player.x, player.y, player.radius)){
                console.log("oyun bitti") ;
                startdiv.classList.remove("hidden") ;
                startbtn.innerHTML = "Tekrar Oyna" ;
                startprgrf.innerHTML = "Oyun Bitti !<br/>Puanınız : " + score ;
                playing = false ;
            }
            if(enemy.remove()){ // dışarı çıkan düşmanlar bellekten çıkarılsın
                enemies.splice(e, 1) ;
                addEnemy();
            }
            enemy.update() ;
            enemy.draw() ;
        //console.log(enemy.c)
        }) ; 
        bullets.forEach((bullet, i) => {  // mermi çiz
            if(bullet.remove()){
                bullets.splice(i, 1) ;
            }
            bullet.update() ;
            bullet.draw() ;
        }) ; 
        player.draw() ; // silahın merkezinden çıkan mermiler lüleden çıkana kadar gözükmüyor
        scorediv.innerHTML = "Puan : "+score ;
        killsdiv.innerHTML = "Etkisiz düşmanlar : "+ kills ;        
    }
}

function init(){
    angle = 0 ;
    bullets = [] ;
    enemies = [] ;
    maxenemies = 1 ;
    score = 0 ;
    kills = 0 ;
    playing = true ;
    startdiv.classList.add("hidden") ;
    player = new Player(width / 2, height / 2, 20, 'rgba(255, 255, 255)') ;
    animate() ; 
    addEnemy() ;
}
//init() ;


