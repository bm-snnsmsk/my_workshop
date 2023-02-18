<?php 

require_once '../system/function.php' ;




if($_POST){
    $bayi_email_or_bayi_code = post('bayi_email_or_bayi_code') ;
    $bayi_password = post('bayi_password') ;
    $crypto = sha1(md5($bayi_password)) ;

    if(!$bayi_email_or_bayi_code || !$bayi_password){
        echo "empty" ;
    }else{
        $login = $db->prepare("SELECT * FROM urun_bayiler WHERE (urun_bayiKodu = ? AND urun_bayiSifre = ?) OR (urun_bayiEmail = ? AND urun_bayiSifre = ?)") ;
        $login->execute([$bayi_email_or_bayi_code, $crypto, $bayi_email_or_bayi_code, $crypto]) ;
        if($login->rowCount()){
            $logined_bayi = $login->fetch(PDO::FETCH_OBJ) ;
            if($logined_bayi->urun_bayiDurum == 1){
                $encode = sha1(md5(IP().$logined_bayi->urun_bayiKodu)) ;
                $_SESSION['bayi_login'] = $encode ;
                $_SESSION['bayi_id'] = $logined_bayi->urun_bayiID  ;
                $_SESSION['bayi_code'] = $logined_bayi->urun_bayiKodu ;
                echo "ok" ;
            }else{
                echo "pasif" ;
            }
           
        }else{
            echo "error" ;
        }
    }
}

?>