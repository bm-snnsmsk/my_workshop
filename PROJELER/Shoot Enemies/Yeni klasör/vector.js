class Vector{
    x = 1 ; // horizontal length
    y = 0 ; // vertical length
    constructor(x, y){
        this.x = x ;
        this.y = y ;
    }
    setX(val){
        this.x = val ;
    }
    getX(){
        return this.x ;
    }
    setY(val){
        this.y = val ;
    }
    getY(){
        return this.y;
    }
    setLength(length){
        let angle = this.getAngle() ;
        this.x = Math.cos(angle) * length ;
        this.y = Math.sin(angle) * length ;
    }
    getLength(){
        return Math.sqrt(this.x * this.x + this.y * this.y) ;
    }
    setAngle(angle){
        let length = this.getLength() ;
        this.x = Math.cos(angle) * length ;
        this.y = Math.sin(angle) * length ;
    }
    getAngle(){
        return Math.atan2(this.y, this.x) ;
    }
    addTo(vector){
        return this.x += vector.getX(), this.y += vector.getY() ;
    }
    subtractFrom(vector){
        return this.x -= vector.getX(), this.y -= vector.getY() ;
    }
    multiplyBy(val){
        return this.x *= val, this.y *= val ;
    }
    divideBy(val){
        return this.x /= val, this.y /= val ;
    }
}// class Vector END