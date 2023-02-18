<?php 

require_once '../system/function.php' ;

if(isset($_SESSION['bayi_login'])){
    if($_SESSION['bayi_login'] != sha1(md5(IP().$bayi_kodu))){
        go(site) ;
    }
}

if($_POST){

    $adres_baslik = post('adres_baslik') ;
    $adres_icerik = post('adres_icerik') ;

    if(!$adres_baslik || !$adres_icerik){
        echo "empty" ;
    }else{
        $result = $db->prepare("INSERT INTO urun_adresler SET 
            urun_adresBaslik = ?, 
            urun_adresTarif = ?, 
            urun_adresDurum = ? ,
            urun_adresBayi = ?  ") ;
            $result->execute([$adres_baslik, $adres_icerik, 1, $bayi_kodu]) ;
            if($result){
                echo "ok" ;
            }else{
                echo "error" ;
        }
    }
}

?>