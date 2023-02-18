
// kıvılcımlar START
function createParticles(x,y,m){
    this.x = x || 0 ;
    this.y = y || 0 ;
    this.radius = 1.2;
    this.xh= -1.5+Math.random()*3 ;
    this.yh= m*Math.random()*1.5 ;
}
// kıvılcımlar END

// hız artırma START
function upVelocity(){
    if(totalScore%4 ==0){
        if(Math.abs(ball.ballXVelocity) < 15){
            ball.ballXVelocity+=(ball.ballXVelocity<0) ? -1 : 1 ;
            ball.ballYVelocity+=(ball.ballYVelocity<0) ? -2 : 2 ;
        }
    }
}
// hız artırma END


// blocklar
function blockAttach(pos){
    this.h = 5;
    this.w = 150 ;
    this.x = canvasW / 2 - this.w / 2 ;
    this.y = (pos == 'topSide') ? 0 : (canvasH - this.h) ;
}

// blocklar oluşturuldu
block.push(new blockAttach('bottomSide')) ;
block.push(new blockAttach('topSide')) ;

//tuval çizmek 
function drawCanvas(){
    ctx.fillStyle = "black" ;
      // background color
    ctx.fillRect(0,0,canvasW,canvasH) ;
}

function ciz(){
    drawCanvas() ;
    for(let i = 0 ; i < block.length; i++){
        let p = block[i] ;
        ctx.fillStyle = "white";
        ctx.fillRect(p.x, p.y, p.w, p.h) ;
    }
    ball.ballDraw() ;
    updateGame() ;
}

// animasyonu çalıştır
function animationStart(){        
    canvas.classList.add('cursor_hide'); 
    afr = animationFrameRequest(animationStart) ; 
    ciz() ;    
}
//animationStart();

function startWindow(){
    ciz() ;
    startButton.startBtnDraw(); 
}


// ekrandaki değişikleri updateGame fonksiyonu START
function updateGame(){

    //puan tablosu
    updateScore() ;

    //top hareketi
    ball.ballX += ball.ballXVelocity ;
    ball.ballY += ball.ballYVelocity ;

    // çubuk hareketi
    if(mouse.x && mouse.y){
        for(let i=1; i<block.length; i++){
            let p = block[i];
            p.x = mouse.x - p.w/2 ;
        }
    }  
    
    //  blockları çağırma  
    p1 = block[1] ;
    p2 = block[2] ;
    if(collision(ball, p1)){
        //ball.ballYVelocity = -ball.ballYVelocity ;
        collisionEvent(ball,p1) ;
    }else if(collision(ball, p2)){
        //ball.ballYVelocity = -ball.ballYVelocity ;    // çarpışma anında yön değiştirildiği için bu koda geek kalmadı
        collisionEvent(ball,p2) ; 
    }else{
        //top üst ve alt çubuğa çarparsa
        if(ball.ballY + ball.ballRadius > canvasH){
            ball.ballY = canvasH - ball.ballRadius ;
            gameOver() ;
        }else if(ball.ballY < 0){
            ball.ballY = ball.ballRadius ;
            gameOver() ;
        }

 

     //top sağ ve sol kenara çarparsa
     if(ball.ballX + ball.ballRadius > canvasW){
        ball.ballXVelocity = -ball.ballXVelocity ;
        ball.ballX = canvasW - ball.ballRadius ;
    }else if(ball.ballX - ball.ballRadius < 0){
        ball.ballXVelocity = -ball.ballXVelocity ;
        ball.ballX = ball.ballRadius ;
    }
    }
    // oluşturulmuş parçaları array'e push etme
    if(carpismaDegiskeni ==1){
        for(var i=0;i<carpismaParcacigi;i++){
            parcalar.push(new createParticles(parcaPozisyonu.x, parcaPozisyonu.y,cogalt));
        }
    }    
    // oluşturulmuş parçaları yayma
    parcaciklariYay();
    carpismaDegiskeni =0 ; // bu yapılmazsa parçalar ekrandan kaybolmaz

}
// ekrandaki değişikleri updateGame fonksiyonu END

// mousemove addEventListener fonksiyonu START
function mouseMove(e){
    mouse.x = e.pageX ;
    mouse.y = e.pageY ;
}
// mousemove addEventListener fonksiyonu END


// collision fonksiyonu START
function collision(obj1, rect){ // b = top , p = çubuk
    if(obj1.ballX + ball.ballRadius >= rect.x && obj1.ballX - ball.ballRadius <= rect.x + rect.w){
        if(obj1.ballY>=(rect.y-rect.h) && rect.y>0){
            blockCarpisma = 1 ;
            return true ;
        }else if(obj1.ballY <= rect.h && rect.y == 0){
            blockCarpisma = 2 ;
            return true ;
        }else{
            return false ;
        }
    }
}
// collision fonksiyonu END



// collision eylemi START
function collisionEvent(ball, p){ 
    ball.ballYVelocity = -ball.ballYVelocity ;
    if(blockCarpisma == 1){
        ball.ballY = p.y - p.h ;
        parcaPozisyonu.y = ball.ballY - ball.ballRadius ; // sıçrama yönü
        cogalt = -1 ;
    }else if(blockCarpisma == 2){
        ball.ballY = p.h+ball.ballRadius ;
        parcaPozisyonu.y = ball.ballY - ball.ballRadius ; // sıçrama yönü
        cogalt = 1 ;
    }
    totalScore++;
    upVelocity();
    if(carpisma){ // ses efekti için
        if(totalScore>0){
            carpisma.pause(); 
        }
        carpisma.currentTime =0;
        carpisma.play();
       
    }
    parcaPozisyonu.x = ball.ballX ; 
    carpismaDegiskeni =1;
}
// collision eyemi END

// gameOver fonksiyonu START
function gameOver(){
    ctx.fillStyle="white" ;
    ctx.font="30px Arial, sans-serif";
    ctx.textAlign="center" ;
    ctx.textBaseline = "middle" ;
    ctx.fillText('Oyun Bitti. Puanınız : '+totalScore,canvasW/2+20, canvasH/2+25) ;
    animationFrameCancel(afr) ;
    bitti = 1;
    resetButton.resetBtnDraw() ;
    canvas.classList.add('cursor_show');
}
// gameOver fonksiyonu END

// score fonksiyonu START
function updateScore(){
    ctx.fillStyle="white" ;
    ctx.font="30px Arial, sans-serif";
    ctx.textAlign="left" ;
    ctx.textBaseline = "top" ;
    ctx.fillText("Puanınız : "+totalScore,10, 10) ;
}
// score fonksiyonu END

// parçaları dağıtma fonksiyonu START
function parcaciklariYay(){
    for(let i =0;i<parcalar.length;i++){
        let par = parcalar[i] ;
        ctx.beginPath();
        ctx.fillStyle="white";
        if(par.radius>0){
            ctx.arc(par.x,par.y,par.radius,0,Math.PI * 2, false) ;
        }
        ctx.fill();
        par.x += par.xh;
        par.y += par.yh;
        //parçaların kayolması
        par.radius = Math.max(par.radius-0.05,0.0) // parçalar yavaş yavaş kaybolur
    }
}
// parçaları dağıtma fonksiyonu END


// gameOver fonksiyonu START
function clickedButton(e){    
    // mouse pozisyonunu yakala
    let mx = e.pageX;
    let my = e.pageY;
    // başlat butonuna tıkla
    if(mx >= startButton.startBtnX && mx <= startButton.startBtnX+startButton.startBtnW && my >= startButton.startBtnY && my <= startButton.startBtnY+startButton.startBtnH){
        animationStart() ; // animasyonu başlat
        startButton = {} ; // başlat fonksiyonunu sil        
    }
    if(bitti == 1){
        if(mx >= resetButton.resetBtnX && mx <= resetButton.resetBtnX + resetButton.resetBtnW && my >= resetButton.resetBtnY && my <= resetButton.resetBtnY + resetButton.resetBtnH){
            canvas.classList.remove('cursor_show'); 
            canvas.classList.add('cursor_hide'); 
            ball.ballX = 20 ;
            ball.ballY = 20 ; 
            totalScore = 0 ;
            ball.ballXVelocity = 4;
            ball.ballYVelocity = 8;
            bitti = 0 ;     
            animationStart() ; // animasyonu başlat
        }
    }
}
// gameOver fonksiyonu END



