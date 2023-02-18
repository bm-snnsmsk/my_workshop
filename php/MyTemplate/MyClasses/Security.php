<?php
//namespace snnsmsk ;

/* class Security{
    
    public function security($input){
        $input = htmlspecialchars(stripcslashes(trim($input))) ;
        return $input ;
    }
    public static function onlyLetters($input){
        $regexp = "/^[a-zA-Z]*$/" ;
        $result = preg_match($regexp, security($input)) ;
        return $result ;
    }
    public static function onlyNumbers($input){
        $regexp = "/^[0-9]*$/" ;
        $result = preg_match($regexp, security($input)) ;
        return $result ;
    }
    public static function emailControl($email){
        $result = filter_var(security($email), FILTER_VALIDATE_EMAIL) ;
        return $result ;
    }
    public static function urlControl($url){
        $regexp = "/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i" ;
        $result = preg_match($regexp,security($url)) ;
        return $result ;
    }
} */

function security($input){
    $input = htmlspecialchars(stripcslashes(trim($input))) ;
    return $input ;
}
function onlyLetters($input){
    $regexp = "/^[a-zA-Z]*$/" ;
    $result = preg_match($regexp, security($input)) ;
    return $result ;
}
function onlyNumbers($input){
    $regexp = "/^[0-9]*$/" ;
    $result = preg_match($regexp, security($input)) ;
    return $result ;
}
function emailControl($email){
    $result = filter_var(security($email), FILTER_VALIDATE_EMAIL) ;
    return $result ;
}
function urlControl($url){
    $regexp = "/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i" ;
    $result = preg_match($regexp,security($url)) ;
    return $result ;
}








?>