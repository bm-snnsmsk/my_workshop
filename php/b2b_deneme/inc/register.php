<?php 

require_once '../system/function.php' ;



if($_POST){
    $bayi_name = post('bayi_name') ;
    $bayi_email = post('bayi_email') ;
    $bayi_password = post('bayi_password') ;
    $bayi_password_tekrar = post('bayi_password_tekrar') ;
    $bayi_telefon = post('bayi_telefon') ;
    $bayi_vergino = post('bayi_vergino') ;
    $bayi_vergi_dairesi = post('bayi_vergi_dairesi') ;
    $bayi_code = uniqid() ;
    $criptoluPass = sha1(md5($bayi_password)) ;

    if(!$bayi_name || !$bayi_email || !$bayi_password || !$bayi_password_tekrar || !$bayi_telefon || !$bayi_vergino || !$bayi_vergi_dairesi){
        echo "empty" ;
    }else{
        if(!filter_var($bayi_email, FILTER_VALIDATE_EMAIL)){
            echo "format" ;
        }else{
            if($bayi_password != $bayi_password_tekrar){
                echo "match" ;
            }else{
                $already = $db->prepare("SELECT urun_bayiEmail FROM urun_bayiler WHERE urun_bayiEmail = ?") ;
                $already->execute([$bayi_email]) ;
                if($already->rowCount()){
                    echo "already" ;
                }else{
                    $result = $db->prepare("INSERT INTO urun_bayiler (urun_bayiKodu, urun_bayiAdi, urun_bayiEmail, urun_bayiSifre, urun_bayiTelefon, urun_bayiVergino, urun_bayiVergiDairesi 
                    ) VALUES(?, ?, ?, ?, ?, ?, ?)") ;
                    $result->execute([$bayi_code, $bayi_name, $bayi_email, $criptoluPass, $bayi_telefon, $bayi_vergino, $bayi_vergi_dairesi]) ;
                    if($result->rowCount()){
                        echo "ok" ;
                    }else{
                        echo "error" ;
                    }
                }
            }
        }
    }
}

?>