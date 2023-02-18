<?php
require_once "config.php" ;

function compress($buffer){
    $buffer = preg_replace('!/\*[^*]*\*+([^/][^*]*\*+)*/!','',$buffer) ;
    $buffer = str_replace(array("\r\n","\r","\n","\t"),"",$buffer) ;
    return $buffer ;
}
function mobilecontrol(){    
    return preg_match("/(android|avantgo|blackberry|bolt|boost|cricket|docomo|fone|hiptop|iemobile|ip(hone|od)|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)|iris|mini|mobi|palm|symbian|vodafone|wap|windows (ce|phone)|xda|phone|pie|tablet|up\.browser|up\.link|webos|wos)/i",$_SERVER["HTTP_USER_AGENT"]) ;
}
function sef_link($str){
    $preg = array("Ç","Ş","Ğ","Ü","İ","Ö","ç","ş","ğ","ü","ö","ı","+","#",".") ;
    $match = array("c","s","g","u","i","o","c","s","g","u","o","i","plus","sharp","") ;
    $perma = strtolower(str_replace($preg, $match, $str)) ;
    $perma = preg_replace("@['A-Za-z0-9\-_\.\+]@i"," ",$perma) ;
    $perma = trim(preg_replace("/\s/+"," ",$perma)) ;
    $perma = preg_replace(" ","-",$perma) ;
    return $perma ;
}
function loc(){ // current sayfanın URL'i
    $loc = "http://localhost".$_SERVER["REQUEST_URI"] ;
    return $loc ;
}
function IP(){
    if(getenv("HTTP_CLIENT_IP")){
        $ip = getenv("HTTP_CLIENT_IP") ;
    }else if(getenv("HTTP_X_FORWARDED_FOR")){
        $ip = getenv("HTTP_X_FORWARDED_FOR") ;
        if(strstr($ip, ",")){
            $tmp = explode(",",$ip) ;
            $ip = trim($tmp[0]) ;
        }
    }else{
        $ip = getenv("REMOTE_ADDR") ;
    }
    return $ip ;
}
function post($par){
    return strip_tags(trim($_POST[$par])) ;
}
function get($par){
    if(isset($_GET[$par])){
        return strip_tags(trim($_GET[$par])) ;
       }else{
        return false ;
       }
}
function go($url, $time = false){
    if($time == false){
        return header('Location:'.$url) ;
    }else{
        return header('refresh:'.$time.';url='.$url) ;
    }
}
function alert($msg, $alert){
    echo '<div class="alert alert-'.$alert.'">'.$msg.'</div>' ;
}
function dt($par, $status = false){
    if($status == false){
        return date("d.m.Y", strtotime($par)) ;
    }else{
        return date("H:i", strtotime($par)) ;
    }
    
}
function pagination($s, $ptotal, $url){
   // global site ;

  
    $forlimit = 3 ;
    if($ptotal < 2){
        NULL ;       
    }else{
        if($s > 4){
           $prev = $s - 1 ;
           echo '<li><a href="'.site.'/'.$url.'1"><i class="zmdi zmdi-long-arrow-left"></i></a></li>' ;
           echo '<li><a href="'.site.'/'.$url.($s-1).'"> << </a></li>' ;          
        }   
        for($i = $s - $forlimit ; $i < $s + $forlimit + 1 ; $i++){
             if($i > 0 && $i <= $ptotal){
                 if($i == $s){
                     echo '<li><a class="active" href="#">'.$i.'</a></li>' ;
                 }else{
                     echo '<li><a href="'.site.'/'.$url.$i.'">'.$i.'</a></li>' ;
                 }
             }
         }
         if($s <= $ptotal - 4){
             $next = $s + 1 ;
             echo '<li><a href="'.site.'/'.$url.$next.'"><i class="zmdi zmdi-long-arrow-right"></i></a></li>' ;
             echo '<li><a href="'.site.'/'.$url.$ptotal.'"> >> </a></li>' ;
         }
        
    }
   
   
}

?>