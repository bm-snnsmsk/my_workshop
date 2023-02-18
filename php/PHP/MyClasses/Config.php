<?php
namespace bm_snnsmsk ;

class Config{

    private $url = 'http://localhost/apps/PHP' ; // sunucuda /apps/PHP olmayacak
    private $path = $_SERVER['DOCUMENT_ROOT'].'/apps/PHP'; // sunucuda apps/PHP olmayacak

    public function __construct(){
       error_reporting(0) ;
    }

    public static function setUrl($url){
        $this->url = $url ;
    }
    public static function getUrl(){
        return $this->url ;
    }

    public static function setPath($path){
        $this->path = $path ;
    }
    public static function getPath(){
        return $this->path ;
    }



    
}
?>