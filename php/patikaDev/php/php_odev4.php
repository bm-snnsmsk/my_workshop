<?php

interface Sekil{
    function alan();
    function cevre();
    function yazdir();
}

class Dikdortgen implements Sekil{
    private $kenar1 ;
    private $kenar2 ;
    public function __construct($kenar1, $kenar2){
        $this->kenar1 = $kenar1 ;
        $this->kenar2 = $kenar2 ;
    }
    public function alan(){
        return $this->kenar1 * $this->kenar2 ;
    }
    public function cevre(){
        return 2 * ($this->kenar1 + $this->kenar2) ;
    }
    public function yazdir(){
        echo "Dikdörtgen'in 1. kenarı : ".$this->kenar1."</br>" ;
        echo "Dikdörtgen'in 2. kenarı : ".$this->kenar2."</br></br>" ;
        echo "Dikdörtgen'nin Alanı : ".$this->alan()."</br>" ;
        echo "Dikdörtgen'nin Çevresi : ".$this->cevre()."</br>" ;
        echo "-------------------------------------</br>" ;
    }
}
class Ucgen implements Sekil{
    private $kenar1 ;
    private $kenar2 ;
    private $kenar3 ;
    public function __construct($kenar1, $kenar2, $kenar3){
        $this->kenar1 = $kenar1 ;
        $this->kenar2 = $kenar2 ;
        $this->kenar3 = $kenar3 ;
    }
    public function alan(){
        $u = ($this->kenar1 + $this->kenar2 + $this->kenar3) / 2 ;
        return sqrt($u * ($u - $this->kenar1) * ($u - $this->kenar2) * ($u - $this->kenar3)) ;
    }
    public function cevre(){
        return $this->kenar1 + $this->kenar2 + $this->kenar3 ;
    }
    public function yazdir(){
        echo "Üçgen'in 1. kenarı : ".$this->kenar1."</br>" ;
        echo "Üçgen'in 2. kenarı : ".$this->kenar2."</br>" ;
        echo "Üçgen'in 3. kenarı : ".$this->kenar3."</br></br>" ;
        echo "Üçgen'in Alanı : ".$this->alan()."</br>" ;
        echo "Üçgen'in Çevresi : ".$this->cevre()."</br>" ;
        echo "-------------------------------------</br>" ;
    }
}
class Kare implements Sekil{
    private $kenar1 ;
    private $kenar2 ;
    public function __construct($kenar1, $kenar2){
        $this->kenar1 = $kenar1 ;
        $this->kenar2 = $kenar2 ;
    }
    public function alan(){
        return $this->kenar1 * $this->kenar2 ;
    }
    public function cevre(){
        return 2 * ($this->kenar1 + $this->kenar2) ;
    }
    public function yazdir(){
        echo "Kare'nin 1. kenarı : ".$this->kenar1."</br>" ;
        echo "Kare'nin 2. kenarı : ".$this->kenar2."</br></br>" ;
        echo "Kare'nin Alanı : ".$this->alan()."</br>" ;
        echo "Kare'nin Çevresi : ".$this->cevre()."</br>" ;
        echo "-------------------------------------</br>" ;
    }
}



$sekil1 = new Dikdortgen(5, 10) ;
$sekil2 = new Ucgen(3, 4, 5) ;
$sekil3 = new Kare(4, 5) ;


echo $sekil1->yazdir() ;
echo $sekil2->yazdir() ;
echo $sekil3->yazdir() ;

?>