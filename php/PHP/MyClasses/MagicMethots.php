<?php
namespace bm_snnsmsk ;

class MagicMethots{

    private static $counter = 0 ;
    
    public function __construct(){
       echo "Nesne oluşturulduğu an çalışan metot" ;
    } 

    public function __call($name, $par=""){
        echo "<div class='alert alert-danger'><mark>".__CLASS__."</mark> isimli class içinde, <mark>".$name."</mark> isimli bir metot bulunmamaktadır.</div>" ;
        if(!empty($par)){
            echo "<div class='alert alert-danger'>Ayrıca <mark>".implode(" - ",$par)."</mark> parametreler de mevcut değildir...</div>" ;
        }
    } 
    public static function __callStatic($name, $par=""){
        echo "<div class='alert alert-danger'><mark>".__CLASS__."</mark> isimli class içinde, <mark>".$name."</mark> isimli bir static metot bulunmamaktadır.</div>" ;
        if(!empty($par)){
            echo "<div class='alert alert-danger'>Ayrıca <mark>".implode(" - ",$par)."</mark> parametreler de mevcut değildir...</div>" ;
        }
    } 
    public function __get($name){
        echo "<div class='alert alert-danger'><mark>".__CLASS__."</mark> isimli class içinde, <mark>".$name."</mark> isimli bir property erişilemiyor veya bulunmamaktadır.</div>" ;
    }
    public function __set($name, $value){
        echo "<div class='alert alert-danger'><mark>".__CLASS__."</mark> isimli class içinde, <mark>".$name."</mark> isimli bir property erişilemediği için veya bulunmadığı için <mark>".$value."</mark> değerini atamayamazsınız</div>" ;
    }
    public function __isset($name){
        echo "<div class='alert alert-danger'><mark>".__CLASS__."</mark> isimli class içinde, <mark>".$name."</mark> isimli bir property erişilemediği için veya bulunmadığı için <mark> isset </mark> metodu ile sınayamazsınız</div>" ;
    }
    public function __unset($name){
        echo "<div class='alert alert-danger'><mark>".__CLASS__."</mark> isimli class içinde, <mark>".$name."</mark> isimli bir property erişilemediği için veya bulunmadığı için <mark> unset </mark> metodu ile yok edemezsiniz</div>" ;
    }
    // HATA VERDİ
 /*    public function __sleep(){
        echo "<div class='alert alert-danger'>Nesne arraye dönüştürülmeye çalışılıyor...</div>" ;
    } */
  /*   public function __wakeup(){
        echo "<div class='alert alert-danger'>Array nesneye dönüştürülmeye çalışılıyor...</div>" ;
    } */
    public function __toString(){
        return "<div class='alert alert-danger'>Nesne yazdırılmaya çalışılıyor...</div>" ;
    }
    public function __invoke($par){
        echo "<div class='alert alert-danger'>Nesne Method olarak çalıştırılmaya çalışılıyor...</div>" ;
    }
    public function __clone(){
        self::$counter++  ;
    }
    public static function printCloneCount(){
        echo "<div class='alert alert-danger'><mark>".__CLASS__."</mark> isimli class, <mark>".self::$counter."</mark> kere klonlandı...</div>" ;
    }
    

    public function __destruct(){
        echo "Nesne işlemi bittiği an çalışan metot" ;
    } 
}
?>