class Particle extends Vector{

    position = new Vector(0,0) ;
    velocity = new Vector(0,0) ;
    gravity = new Vector(0,0) ;
    radius = 0 ;
    mass = 1 ;
    bounce = -1 ;
    friction = 1 ; // = friction yok 
  
    constructor(x, y, speed, direction, grav){ // x coordinat, y coordinat, direction=angle, , grav bu parametre gravitateTo() sondra çıkarıldı
       super(x,y) ;
       this.position.x = x ;
       this.position.y = y ;
       this.velocity.setLength(speed) ;
       this.velocity.setAngle(direction) ;
       this.gravity.x = 0 ;
       this.gravity.y = grav || 0 ;
       return this ;    // olsa da olur olmasa da
    }
    accelerate(accel){
        this.velocity.addTo(accel) ;
    }
    update(){        
        this.velocity.multiplyBy(this.friction) ; 
        this.velocity.addTo(this.gravity) ;
        this.position.addTo(this.velocity) ;
    }
    angleTo(p2){
        return Math.atan2(p2.position.getY() - this.position.getY(), p2.position.getX() - this.position.getX()) ;
    }
    distanceTo(p2){
        let dx = p2.position.getX() - this.position.getX() ;
        let dy = p2.position.getY() - this.position.getY() ;
        return Math.sqrt(dx * dx + dy * dy) ;
    }
    gravitateTo(p2){
        let grav = new Vector(0,0) ;
        let dist = this.distanceTo(p2) ;
        grav.setLength(p2.mass / (dist * dist)) ;
        grav.setAngle(this.angleTo(p2)) ;
        this.velocity.addTo(grav) ;
    }
}


/* 
function  removeDeadParticles(){
    for(let i = particlesArr.length - 1 ; i >= 0 ; i--){
        let p = particlesArr[i] ;
        if(p.position.getX() - p.radius > width || 
           p.position.getX() + p.radius < 0 || 
           p.position.getY() - p.radius > height || 
           p.position.getY() + p.radius < 0){
           p.splice(i, 1) ; 
        }
    }
} */