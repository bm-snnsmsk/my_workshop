<?php

// güvenli input START
function filtrele($e){
    return is_array($e) ? array_map('filtrele',$e) : strip_tags(htmlspecialchars(trim($e))) ;
}
$security0 = array_map('filtrele' ,$_REQUEST) ;
// güvenli input END

// güvenli input START
function security($e){
    return strip_tags(htmlspecialchars(trim($e))) ;
}
// güvenli input END


// dizin listeleme START
function listAll($dir){
    $files = scandir($dir) ;
    echo "<ul>" ;
    foreach($files as $file){
        if($file !='.' && $file != '..'){
            echo "<li>" ;
            echo $file ;
            if(is_dir($dir.'/'.$file)){
                listAll($dir.'/'.$file) ;
            }
            echo "</li>" ;
        }
    }
    echo "</ul>" ;
}
// dizin listeleme END

// get START
function get($get){
   if(isset($_GET[$get])){
    return trim($_GET[$get]) ;
   }else{
    return false ;
   }
}
// get END

// post START
function post($post){
    if(isset($_POST[$post])){
    return trim($_POST[$post]) ;
    }else{
     return false ;
    }
 }
 // post END

 // _SESSION START
function session($session){
    if(isset($_SESSION[$session])){
    return trim($_SESSION[$session]) ;
    }else{
     return false ;
    }
 }
 // _SESSION END

  // _COOKIE START
function cookie($cookie){
    if(isset($_COOKIE[$cookie])){
    return trim($_COOKIE[$cookie]) ;
    }else{
     return false ;
    }
 }
 // _COOKIE END



// oturum açma START    
   /*  session_start() ;
    if(isset($_SESSION['session_name'])){
        echo 'Merhaba '.$_SESSION['session_name'].' hoş geldiniz.' ;
    }else{
        echo 'Lütfen oturum açınız.' ;
    }  */
// oturum açma END

// oturum kapatma START    
   // unset($_SESSION['session_name']); 
// oturum kapatma END

?>