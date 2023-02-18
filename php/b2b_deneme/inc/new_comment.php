<?php 

require_once '../system/function.php' ;

if(isset($_SESSION['bayi_login'])){
    if($_SESSION['bayi_login'] != sha1(md5(IP().$bayi_kodu))){
        go(site) ;
    }
}

if($_POST){

    $your_comment = post('your_comment') ;
    $product_code = post('product_code') ;

    if(!$your_comment || !$product_code){
        echo "empty" ;
    }else{
        if(strlen($your_comment) > 500){
            echo 'char';
        }else{
            $result = $db->prepare("INSERT INTO urun_yorumlar SET 
            urun_yorumBayi = ?, 
            urun_yorumUrun = ?, 
            urun_yorumIsim = ? ,
            urun_yorumIP = ? ,
            urun_yorumDurum = ? ,
            urun_yorumIcerik = ?  ") ;
            $result->execute([$bayi_kodu, $product_code,  $bayi_name, IP(), 0, $your_comment]) ;
            if($result){
                echo "ok" ;
            }else{
                echo "error" ;
            }
        }       
    }
}

?>