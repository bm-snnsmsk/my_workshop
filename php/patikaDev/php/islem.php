<?php
include("my_functions.php");
session_start() ;
$user = [
    'snnsmsk' => [
        'eposta' => 'snnsmsk@gmail.com',
        'password' => '123' 
    ],
    'brnsmsk' => [
        'eposta' => 'brnsmsk@gmail.com',
        'password' => '1234' 
    ],
    'tbnrsmsk' => [
        'eposta' => 'tbnrsmsk@gmail.com',
        'password' => '12345' 
    ],
    'emnsmsk' => [
        'eposta' => 'emnsmsk@gmail.com',
        'password' => '123456' 
    ],
    'kndlsmsk' => [
        'eposta' => 'kndlsmsk@gmail.com',
        'password' => '1234567' 
    ]
] ;


if(get('islem') == 'giris'){
    $_SESSION['username'] = post('username') ;
    $_SESSION['password'] = post('password') ;
    if(!post('username')){
        $_SESSION['error'] = "Lütfen kullanıcı alanını doldurunuz ! " ;
        header('Location:login.php') ;
        die();
    }else if(!post('password')){
        $_SESSION['error'] = "Lütfen şifre alanını doldurunuz ! " ;
        header('Location:login.php') ;
        die();
    }else{
        if(array_key_exists(post('username'), $user)){
            if($user[post('username')]['password'] == post('password')){
                $_SESSION['login'] = true ;
                $_SESSION['kullanici_adi'] = post('username') ;
                $_SESSION['eposta'] = $user[post('username')]['eposta'] ;
                header('Location:index.php') ;
                die();
            }else{
                $_SESSION['error'] = "Kayıtlı kullanıcı bulunamadı. " ;
                header('Location:login.php') ;
                die();
            }
        }else{
            $_SESSION['error'] = "Kayıtlı kullanıcı bulunamadı. " ;
            header('Location:login.php') ;
            die();
        }
    }
}

if(get('islem') == 'hakkimda'){
   $hakkimda = post('hakkimda') ;
   $sonuc = file_put_contents('db/'.session('kullanici_adi').'.txt',security($hakkimda)) ;
  if($sonuc){
    header('Location:index.php?islem=ok') ;
  }else{
    header('Location:index.php?islem=hata') ;
  }
}

if(get('islem') == 'oturumu_kapat'){

   session_destroy();
   session_start() ;
   $_SESSION['error'] = 'Oturumu Sonlandırıldı.'  ;
   header('Location:login.php') ;
   die();
 }

 if(get('islem') == 'renk'){    
    setcookie('color', get('color'), time() + 86400) ;  
    header('Location:'.$_SERVER['HTTP_REFERER'] ?? 'index.php') ;
  }
?>