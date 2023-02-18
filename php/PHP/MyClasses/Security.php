<?php
namespace bm_snnsmsk ;

class Security{    
    public static function security($input){
        $input = htmlspecialchars(stripcslashes(trim($input))) ;
        return $input ;
    }
}
?>