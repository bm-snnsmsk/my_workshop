<?php 

require_once('Config/init.php') ;

/* if(ERR_MODE){
    error_reporting(E_ALL) ;
    ini_set('error_reporting',true) ;
}else{
    error_reporting(0) ;
    ini_set('error_reporting',false) ;
}
 */
$route['route'][0] = 'home' ;
$route['lang'] = 'tr' ;

//Helper::test($route) ;
if(isset($_GET['route'])){
    $desen = '@(?<lang>\b[a-z]{2}\b)?/?(?<route>.+)/?@' ; 
    preg_match($desen, $_GET['route'], $result) ;

   // test alanı  
   //Helper::test($_GET['route']) ;
}
if(isset($result['lang'])){
   if(file_exists(BASEDIR.'/Language/'.$result['lang'].'.php')){
       $route['lang'] = $result['lang'] ;
   }else{
       $route['lang'] = 'tr' ;
   }
}

if(isset($result['route'])){
    $route['route'] = explode('/', $result['route']) ;
    // TEST
    //Helper::test($route['route']) ;
}

require(BASEDIR.'/Language/'.$route['lang'].'.php');



if(file_exists(BASEDIR.'/Controller/'.$route['route'][0].'.php')){
    require BASEDIR.'/Controller/'.$route['route'][0].'.php' ;
}else{
    Helper::go(URL."404.html") ;
}



?>
