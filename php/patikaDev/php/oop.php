<?php


class Sayi{
   public $name ;
   public $name2 ;
   public const PI = 3.14 ;

   public function __construct($param1 = 'sinan', $param2 = "emine"){
    $this->name = $param1 ;
    $this->name2 = $param2 ;
    echo "kurucu çalıştı<br/>" ;
   }
   public function setSayi($a, $b){
        $this->a = $a ;
        $this->b = $b ;
        $sonuc = $a * $b ;
        return $this->name." ".$sonuc." ".$this->name2 ;
    }

   
    public function __destruct(){
        echo "<br/>yıkıcı çalıştı" ;
       }
}

 $s1 = new Sayi("baran","tubanur") ;
 echo  $s1->setSayi(200,10)." ".$s1::PI ;
 echo "<br/>--------<br/>" ;
 $s2 = new Sayi() ;
 echo  $s2->setSayi(30,10)." ".$s1::PI ;

?>