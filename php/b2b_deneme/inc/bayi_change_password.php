<?php 

require_once '../system/function.php' ;

if(isset($_SESSION['bayi_login'])){
    if($_SESSION['bayi_login'] != sha1(md5(IP().$bayi_kodu))){
        go(site) ;
    }
}

if($_POST){    
    $bayi_password = post('bayi_password') ;
    $bayi_password_again = post('bayi_password_again') ;
    $criptoluPass = sha1(md5($bayi_password)) ;

    if(!$bayi_password || !$bayi_password_again){
        echo "empty" ;
    }else{
        if($bayi_password != $bayi_password_again){
            echo "match" ;
        }else{
            $result = $db->prepare("UPDATE urun_bayiler SET urun_bayiSifre = ? WHERE urun_bayiKodu = ? AND urun_bayiID = ?") ;
                $result->execute([$criptoluPass, $bayi_kodu, $bayi_id]) ;
                if($result->rowCount()){
                    echo "ok" ;
                }else{
                    echo "error" ;
            }
        }
    }
}

?>