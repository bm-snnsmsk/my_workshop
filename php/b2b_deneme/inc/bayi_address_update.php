<?php 

require_once '../system/function.php' ;

// if(isset($_SESSION['bayi_login'])){
//     if($_SESSION['bayi_login'] != sha1(md5(IP().$bayi_kodu))){
//         go(site) ;
//     }
// }

if($_POST){
    //print_r($_POST) ; die();
    $adres_id = post('adres_id') ;
    $urun_adresBaslik = post('adres_baslik') ;
    $urun_adresTarif = post('adres_icerik') ;
    $status = post('status') ;

    if(!$urun_adresBaslik || !$urun_adresTarif || !$adres_id){
        echo "empty" ;
    }else{
        $result = $db->prepare("UPDATE urun_adresler SET 
            urun_adresBaslik = ?, 
            urun_adresTarif = ?, 
            urun_adresDurum = ?
            WHERE urun_adresBayi = ? AND urun_adresID = ?") ;
            $result->execute([$urun_adresBaslik, $urun_adresTarif, $status, $bayi_kodu, $adres_id]) ;
            if($result){
                echo "ok" ;
            }else{
                echo "error" ;
        }
    }
}

?>