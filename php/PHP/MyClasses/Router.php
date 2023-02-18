<?php
namespace bm_snnsmsk ;

class Router{

    public function __construct(){

    }

    public static function go($url, $time = 0){
        if($time != 0){
            header("Refresh:".$time.";url=".$url) ;
        }else{
            header("Location:".$url) ;
        }
    }
    public static function comeBack($time = 0){
        $url = $_SERVER["HTTP_REFERER"] ;
        if($time != 0){
            header("Refresh:".$time.";url=".$url) ;
        }else{
            header("Location:".$url) ;
        }
    }

    
}
?>