function collision(x1, y1, r1, x2, y2, r2){
    let dx = x2 - x1 ;
    let dy = y2 - y1 ;
    let hypo = Math.sqrt(dx * dx + dy * dy) ;
    if((r1 + r2) > hypo){
        return true ; // collision var
    }else{
        return false ;
    }
}

function addEnemy(){
    for(let i = enemies.length; i < maxenemies; i++){

        let x, y ; // enemies'ler sadece kenarlardan gelsin 
        if(Math.random() < .5){
            x = (Math.random() > .5) ? width : 0 ; // ya sağ ya sol
            y = Math.random() * height ;
        }else{
            x = Math.random() * width ;
            y = (Math.random() > .5) ? height : 0 ; // ya üst ya da alt
        }    

        let r = Math.random() * 30 + 10 ;
        let red = Math.random() * 255 ;
        let green = Math.random() * 255 ;
        let blue = Math.random() * 255 ;
        let alpha = Math.random() * 0.5 + .5 ;
        let renk = "rgba("+red+","+green+","+blue+","+alpha+")" ;
        // let speed = .5 + ((20 - ((r / 20) * r)) / 40) * maxenemies ; // büyükler yavaş küçükler hızlı enemies'ler artıkça hızları da artmaktadır. üst levelerde daha hızlı enemies'ler
        let speed = .5 + ((40 - ((r / 40) * r)) / 80) / maxenemies ; // // büyükler yavaş küçükler hızlı enemies'ler artıkça hızları da azalmaktadır. üst levelerde daha hızlı enemies'ler
        enemies.push(new Circle(x, y, player.x, player.y, r, renk, speed)) ;
    }
}