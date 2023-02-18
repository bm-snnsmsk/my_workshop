<?php
include 'baglan.php' ; 
//echo 'bglan test ' ;
ob_start();
session_start() ;

if(isset($_POST['btnkaydet'])){
    $ayarkaydet = $DBConnect->prepare('UPDATE ayarlar SET site_baslik = ?, site_aciklama = ?, site_sahibi = ?') ;
    $ayarkaydet->execute([
        $_POST['baslik'],
        $_POST['aciklama'],
        $_POST['sahibi']
    ]) ;
    if($ayarkaydet == 0){
        echo "email veya şifre yanlış" ;
    }else{
        header('location:../index.php') ; 
    }
}

if(isset($_POST['oturumac'])){
    $kullanicisor = $DBConnect->prepare('SELECT * FROM user WHERE userEmail = ? AND userPassword = ?') ;
    $kullanicisor->execute([
        $_POST['useremail'],
        $_POST['userpass']
    ]) ;
    $sonuc = $kullanicisor->rowCount() ;
   // echo $sonuc ;
    if($sonuc == 0){
        echo "email veya şifre yanlış" ;
    }else{
        header('location:../index.php') ; 
        $_SESSION['kullanici_mail'] = $_POST['useremail'] ;
    }
}

if(isset($_POST['projeekle'])){
    $projeekle = $DBConnect->prepare('INSERT INTO proje (proje_baslik, proje_teslim, proje_durum, proje_aciliyet, proje_detay)
    VALUES (?, ?, ?, ?, ?) ') ;
    $projeekle->execute([
        strip_tags($_POST['proje_baslik']),
        $_POST['proje_teslim_tarihi'],
        $_POST['proje_durum'],
        $_POST['proje_aciliyeti'],
        $_POST['proje_detay']
    ]) ;
   
    if($projeekle){
        echo "kayıt başarılı" ;
        header('refresh:2;url=../projeler.php') ; 
    }else{
        echo "kayıt başarısız" ;
        header('refresh:2;url=../projeekle.php') ; 
    }
}
if(isset($_POST['projeduzenle'])){
    $projeduzenle = $DBConnect->prepare('UPDATE proje SET proje_baslik = ?,  proje_teslim = ?, proje_durum = ?, proje_aciliyet = ?, proje_detay = ? WHERE id = ? ') ;
    $projeduzenle->execute([
        $_POST['proje_baslik'],
        $_POST['proje_teslim_tarihi'],
        $_POST['proje_durum'],
        $_POST['proje_aciliyeti'],
        $_POST['proje_detay'],
        $_POST['projeID']
    ]) ;
   
    if($projeduzenle){
        echo "Düzenleme başarılı" ;
        header('refresh:2;url=../projeler.php') ; 
    }else{
        echo "Düzenleme başarısız" ;
        header('refresh:2;url=../projeduzenle.php') ; 
    }
}
if(isset($_POST['proje_silme'])){
    $projesil = $DBConnect->prepare('DELETE FROM proje WHERE id = ? ') ;
    $projesil->execute([
        $_POST['proje_id']
    ]) ;
   
    if($projesil){
        echo "Silme başarılı" ;
        header('refresh:2;url=../projeler.php') ; 
    }else{
        echo "Silme başarısız" ;
        header('refresh:2;url=../projeler.php') ; 
    }
}
if(isset($_POST['siparisekle'])){
    $siparisekle = $DBConnect->prepare('INSERT INTO siparis (sip_name, sip_mail, sip_tel, sip_teslim_tarihi, sip_ucret, sip_baslik)
    VALUES (?, ?, ?, ?, ?, ?) ') ;
    $siparisekle->execute([
        $_POST['musteri_isim'],
        $_POST['musteri_mail'],
        $_POST['musteri_tel'],
        $_POST['teslim_tarihi'],
        $_POST['ucret'],
        $_POST['sip_baslik']
    ]) ;
    if($siparisekle){
        echo "siparisekle başarılı" ;
        header('refresh:2;url=../siparisler.php') ; 
    }else{
        echo "siparisekle başarısız" ;
        header('refresh:2;url=../siparisekle.php') ; 
    }
}
if(isset($_POST['siparis_silme'])){
    $projesil = $DBConnect->prepare('DELETE FROM siparis WHERE id = ? ') ;
    $projesil->execute([
        $_POST['siparis_id']
    ]) ;
   
    if($projesil){
        echo "Silme başarılı" ;
        header('refresh:2;url=../siparisler.php') ; 
    }else{
        echo "Silme başarısız" ;
        header('refresh:2;url=../siparisler.php') ; 
    }
}

?>