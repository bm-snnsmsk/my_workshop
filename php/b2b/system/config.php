<?php 

session_start();
ob_start('compress');
date_default_timezone_set('Europe/Istanbul');


try{

    $db = new PDO("mysql:host=localhost;dbname=b2b;charset=utf8;","root","");
    $db->query("SET CHARACTER SET utf8");
    $db->query("SET NAMES utf8");

}catch(PDOException $e){
    print_r($e->getMessage());
    die();
}


$query = $db->prepare("SELECT * FROM ayarlar LIMIT :lim");
$query->bindValue(':lim',(int) 1,PDO::PARAM_INT);
$query->execute();
if($query->rowCount()){

    $arow       = $query->fetch(PDO::FETCH_OBJ);
    $site       = $arow->siteurl;
    $sitebaslik = $arow->sitebaslik;
    $sitekeyw   = $arow->sitekeyw;
    $sitedesc   = $arow->sitedesc;
    $sitelogo   = $arow->sitelogo;

    
    #sabitler
    define('site',$site);
    define('baslik',$arow->sitebaslik);
    #sabitler
}


##giriş kontrolleri yani giriş yaptıysa kullanılaviblecek tüm bilgilerine ulaşmak için

function IP2(){ // logout.php'de function.php çağrılmasında problem olduğu için burda da IP() fonksiyonu IP2() olarak yeniden yazıldı  

    if(getenv("HTTP_CLIENT_IP")){
        $ip = getenv("HTTP_CLIENT_IP");
    }elseif(getenv("HTTP_X_FORWARDED_FOR")){
        $ip = getenv("HTTP_X_FORWARDED_FOR");
        if (strstr($ip, ',')) {
            $tmp = explode (',', $ip);
            $ip = trim($tmp[0]);
        }
    }else{
        $ip = getenv("REMOTE_ADDR");
    }
    return $ip;
}


if( @$_SESSION['login'] == @sha1(md5(IP2().$_SESSION['code'])) ){ // kullanıcı giriş yaptıysa şayet şu atamaları yap ve istediğin yerde kullan


$logincontrol = $db->prepare("SELECT * FROM bayiler WHERE id=:id AND bayikodu=:k");
$logincontrol->execute([':id' => @$_SESSION['id'],':k'=> @$_SESSION['code']]);
if($logincontrol->rowCount()){

    $par   = $logincontrol->fetch(PDO::FETCH_OBJ);  

    if($par->bayidurum == 1){

        $bid   = $par->id;
        $blogo = $par->bayilogo;
        $bcode = $par->bayikodu;
        $bmail = $par->bayimail;
        $bname = $par->bayiadi;
        $bgift = $par->bayiindirim;
        $bphone= $par->bayitelefon;
        $bfax  = $par->bayifax;
        $bvno  = $par->bayivergino;
        $bvd   = $par->bayivergidairesi;
        $bweb  = $par->bayisite;
        $bstatus = $par->bayidurum;

    }else{
        @session_destroy();
    }

}else{
    @session_destroy();
}


}

?>