// Player Class'ı START
class Player{
    constructor(x, y, radius, color){
        this.x = x ;
        this.y = y ;
        this.radius = radius ;
        this.color = color ;
    }
    draw(){
        ctx.save() ;
        ctx.translate(this.x, this.y) ;
        ctx.rotate(angle * Math.PI / 180) ; // degree to radyan
        //  ctx.rotate(angle) ; // radyan
        ctx.fillStyle = this.color ;
        ctx.beginPath() ;
        ctx.arc(0, 0, this.radius, 0, Math.PI * 2) ;
        ctx.fillRect(0, -(this.radius * .4), this.radius + 15, this.radius * .8) ;
        ctx.fill() ;
        ctx.closePath() ;
        ctx.restore() ;
    }
}
// Player Class'ı END

// Circle Class'ı START
class Circle{
    constructor(bx, by, tx, ty, radius, color, s){
        this.bx = bx ; // begin x
        this.by = by ;
        this.tx = tx ; // target x
        this.ty = ty ;
        this.x = bx ;
        this.y = by ;
        this.radius = radius ;
        this.color = color ;
        this.s = s ; // speed
    }
    draw(){       
        ctx.fillStyle = this.color ;
        ctx.beginPath() ;
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2) ;        
        ctx.fill() ;
        ctx.closePath() ;
    }
    update(){
        let dx = this.tx - this.bx ;
        let dy = this.ty - this.by ;
        let hypo = Math.sqrt(dx * dx + dy * dy) ;
        this.x += (dx / hypo) * this.s ; // bullet / enemy hızı
        this.y += (dy / hypo) * this.s ; // bullet / enemy hızı
    }
    remove(){// canvas dışına çıkan mermileri kaldırmak için
        if((this.x < 0 || this.x > width) || (this.y < 0 || this.y > height)){
            return true ;
        }else{
            return false ;
        }
    }
}
// Circle Class'ı END
