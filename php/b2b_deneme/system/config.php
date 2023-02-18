<?php

session_start() ;
ob_start('compress') ; // sayfa kaynağındaki html dökümanını sıkıştırır
date_default_timezone_set("Europe/Istanbul") ;

try{
    $db = new PDO("mysql:host=localhost;dbname=abc_b2b;charset=utf8;","root","") ;
    $db->query("SET CHARACTER SET utf8") ; 
    $db->query("SET NAMES utf8") ; 
}catch(PDOException $e){
    echo($e->getMessage()) ;
    die() ;
}



$query = $db->prepare("SELECT * FROM ayarlar LIMIT :lim") ;
$query->bindValue(":lim",(int) 1, PDO::PARAM_INT) ;
$query->execute() ;
if($query->rowCount()){
    $row = $query->fetch(PDO::FETCH_OBJ) ;
    $site = $row->ayarlarSiteUrl ;
   
    // sabitler START
    define('site',$site);
    define('baslik',$row->ayarlarSiteBaslik);
    // sabitler END
}

// giriş kontrolü START
if(isset($_SESSION['bayi_id']) && isset($_SESSION['bayi_code']) && isset($_SESSION['bayi_login']) && ($_SESSION['bayi_login'] == sha1(md5(IP().$_SESSION['bayi_code'])))){
    $login_control = $db->prepare('SELECT * FROM urun_bayiler WHERE urun_bayiID = ? AND urun_bayiKodu = ?') ;
    $login_control->execute([$_SESSION['bayi_id'], $_SESSION['bayi_code']]) ;
    if($login_control->rowCount()){
        $logined_bayi = $login_control->fetch(PDO::FETCH_OBJ) ;
        if($logined_bayi->urun_bayiDurum == 1){
            $bayi_id = $logined_bayi->urun_bayiID ;
            $bayi_kodu = $logined_bayi->urun_bayiKodu ;
            $bayi_email = $logined_bayi->urun_bayiEmail ;
            $bayi_name = $logined_bayi->urun_bayiAdi ;
            $bayi_gift = $logined_bayi->urun_bayiIndirim ;
            $bayi_phone = $logined_bayi->urun_bayiTelefon ;
            $bayi_fax = $logined_bayi->urun_bayiFax ;
            $bayi_vergi_no = $logined_bayi->urun_bayiVergino ;
            $bayi_vergi_dairesi = $logined_bayi->urun_bayiVergiDairesi ;
            $bayi_site = $logined_bayi->urun_bayiSite ;
            $bayi_durum = $logined_bayi->urun_bayiDurum ;
            $bayi_logo = $logined_bayi->urun_bayiLogo ;
        }else{
            @session_destroy() ;
        }
    }else{
        @session_destroy() ;
    }
}
// giriş kontrolü END


?>