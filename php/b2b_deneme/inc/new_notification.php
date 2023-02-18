<?php 

require_once '../system/function.php' ;

if(isset($_SESSION['bayi_login'])){
    if($_SESSION['bayi_login'] != sha1(md5(IP().$bayi_kodu))){
        go(site) ;
    }
}

if($_POST){

    $havale_banka_name = post('havale_banka_name') ;
    $havale_date = post('havale_date') ;
    $havale_saat = post('havale_saat') ;
    $havale_tutar = post('havale_tutar') ;
    $havale_description = post('havale_description') ;
    $ip = IP();

    if(!$havale_banka_name || !$havale_date || !$havale_saat || !$havale_tutar || !$havale_description){
        echo "empty" ;
    }else{
        $result = $db->prepare("INSERT INTO urun_havale_bildirim SET 
            urun_havaleBayi = ?, 
            urun_havaleBanka = ?, 
            urun_havaleTarih = ?, 
            urun_havaleSaat = ? ,
            urun_havaleTutar = ?, 
            urun_havaleNot = ?,
            urun_havaleIP = ?
              ") ;
            $result->execute([$bayi_kodu, $havale_banka_name, $havale_date, $havale_saat, $havale_tutar, $havale_description, $ip]) ;
            if($result){
                echo "ok" ;
            }else{
                echo "error" ;
        }
    }
}

?>