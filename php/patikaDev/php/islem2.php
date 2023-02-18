<?php
session_start();

function get($get){
    if(isset($_GET[$get])){
        return trim($_GET[$get]) ;
    }else{
        return false ;
    }
}

function post($post){
    if($_POST[$post]){
        return $_POST[$post] ;
    }else{
        return null ;
    }
}

function session($session){
    if($_SESSION[$session]){
        return $_SESSION[$session] ;
    }else{
        return null ;
    }
}


$users = [
    'snnsmsk' => [
        'adi' => 'sinan' ,
        'soyadi' => 'simsek' ,
        'parola' => '123' ,
        'email' => 'snnsmsk@gmail.com'
    ],
    'brnsmsk' => [
        'adi' => 'baran' ,
        'soyadi' => 'simsek' ,
        'parola' => '1234' ,
        'email' => 'brnnsmsk@gmail.com'
    ]
] ;

if(get('islem') == 'login'){
    $_SESSION['username'] = post('username') ;
    if(!post('username') || empty(post('username'))){
        $_SESSION['error'] = "kullanıcı adı boş olamaz" ;
        header("Location:login2.php") ; 
        die();
    }else if(!post('parola') || empty(post('parola'))){
        $_SESSION['error'] = "şifre adı boş olamaz" ;
        header("Location:login2.php") ; 
        die();
    }else{
        if(post('parola') == $users[post('username')]['parola']){
            $_SESSION['login'] = true ;
            $_SESSION['adi'] = $users[post('username')]['adi'] ;
            $_SESSION['soyadi'] = $users[post('username')]['soyadi'] ;
            $_SESSION['email'] = $users[post('username')]['email'] ;
            $_SESSION['k_adi'] = post('username') ;
            header("Location:index2.php") ; 
            die();
        }else{
            $_SESSION['error'] = "Böyle bir kayıt bulunamadı" ;
            header("Location:login2.php") ; 
            die();
        }
    }
}

if(get('islem') == 'logout'){
   session_destroy();
   session_start();
   $_SESSION['error'] = "Oturum başarılı bir şekilde sonlandırıldı" ;
   header("Location:login2.php") ; 

}

if(get('islem') == 'icerik'){

    $icerikk = $_POST['hakkimda'] ;   

    $sonuc = file_put_contents('ddd/'.session('k_adi').'.txt' ,$icerikk) ;

    if($sonuc){
        header("Location:index2.php") ; 
      }else{
        header("Location:index2.php") ; 
      }
  
 
 }

?>




