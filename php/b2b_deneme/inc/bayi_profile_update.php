<?php 

require_once '../system/function.php' ;

if(isset($_SESSION['bayi_login'])){
    if($_SESSION['bayi_login'] != sha1(md5(IP().$bayi_kodu))){
        go(site) ;
    }
}

if($_POST){
    //print_r($_POST) ; die();
    $bayi_kodu = post('bayi_kodu') ;
    $bayi_name = post('bayi_name') ;
    $bayi_email = post('bayi_email') ;
    $bayi_telefon = post('bayi_telefon') ;
    $bayi_gift = post('bayi_gift') ;
    $bayi_fax = post('bayi_fax') ;
    $bayi_vergi_no = post('bayi_vergi_no') ;
    $bayi_vergi_dairesi = post('bayi_vergi_dairesi') ;
    $bayi_site = post('bayi_site') ;

    if(!$bayi_name || !$bayi_email || !$bayi_telefon || !$bayi_vergi_no || !$bayi_vergi_dairesi){
        echo "empty" ;
    }else{
        if(!filter_var($bayi_email, FILTER_VALIDATE_EMAIL)){
            echo "format" ;
        }else{
            $already = $db->prepare("SELECT urun_bayiKodu, urun_bayiEmail FROM urun_bayiler WHERE urun_bayiEmail = ? AND urun_bayiKodu = ?") ;
                $already->execute([$bayi_email, $bayi_kodu]) ;
                if($already->rowCount()){
                    echo "already" ;
                }else{
                    $result = $db->prepare("UPDATE urun_bayiler SET 
                    urun_bayiAdi = ?, 
                    urun_bayiEmail = ?, 
                    urun_bayiIndirim = ?, 
                    urun_bayiTelefon = ?, 
                    urun_bayiFax = ?, 
                    urun_bayiVergino = ?, 
                    urun_bayiVergiDairesi = ?, 
                    urun_bayiSite = ? WHERE urun_bayiKodu = ?") ;
                    $result->execute([$bayi_name, $bayi_email, $bayi_gift, $bayi_telefon, $bayi_fax, $bayi_vergi_no, $bayi_vergi_dairesi, $bayi_site, $bayi_kodu]) ;
                    if($result){
                        echo "ok" ;
                    }else{
                        echo "error" ;
                    }
            }
        }
    }
}

?>