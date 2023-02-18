<?php
namespace bm_snnsmsk ;

class Cookie{

    public function __construct(){

    }

    public function setCookie($cookieName, $cookieValue, $cookieLiveTime = 0, $cookieActivePath = "/", $cookieSubdomain = null, $cookieHttpsSecure = false, $cookieJustHttp = false){ // son ikisi true olması güvenlik açısından çok önemlidir
        setcookie(Security::security($cookieName), Security::security($cookieValue), Security::security($cookieLiveTime), Security::security($cookieActivePath), Security::security($cookieSubdomain), Security::security($cookieHttpsSecure), Security::security($cookieJustHttp)) ;
    }
    public function getCookie($cookieName){
        return $_COOKIE[Security::security($cookieName)] ;
    }
    public function deleteCookie($cookieName, $cookieValue = "", $cookieLiveTime = 0){
        setcookie(Security::security($cookieName), "", Security::security($cookieLiveTime), "/") ;
    }
    
}
?>