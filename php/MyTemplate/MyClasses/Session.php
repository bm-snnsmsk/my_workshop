<?php

namespace bm_snnsmsk ;

class Session{

    private $host = 'localhost' ;
    public function __construct(){
        session_set_cookie_params(null, '/', $this->host, false, true) ; // JS ile yetkisiz erişmeyi engellemek için // 4. paramtre https sertifikası alındığında true yapılmalı
        session_start() ;
    }

    public function setSession($sessionName, $sessionValue){
        session_regenerate_id(true) ; // oturum sabitleme için
        $_SESSION[Security::security($sessionName)] =  Security::security($sessionValue) ;
        $_SESSION['loginIP'] = $_SERVER['REMOTE_ADDR'] ;  // client IP
        $_SESSION['userAgent'] = $_SERVER['HTTP_USER_AGENT'] ; // client browser
    }
    public function getSession($sessionName){
        if(isset($_SESSION[Security::security($sessionName)])){
            return  $_SESSION[Security::security($sessionName)] ;
           }else{
            return false ;
           }
    }
    public function getSessions(){
        return $_SESSION ;
    }
    public function deleteSession($sessionName){
        if(isset($sessionName)){
            unset($_SESSION[Security::security($sessionName)]) ;
        }else{
            return 0 ;
        }
    }
    public function deleteAllSessions(){
        session_unset() ;
        session_destroy() ;
    }    
}
// session_regenerate_id(true) ; giriş yapıldığı an ile geçerli zamanki sessionlar aynı olmasın
// $_SESSION['logIn'] = true ;
// $_SESSION['username'] = $username ;
// $_SESSION['loginIP'] = $_SERVER['REMOTE_ADDR] ; // DB'de saklanabilir // sıkıntılı olabilir ağ değişse telefondan pc'den girse IP değişir bunu gözönünde bulundur
// $_SESSION['userAgent'] = $_SERVER['HTTP_USER_AGENT] ; //browser bilgisi // DB'de saklanabilir
?>

