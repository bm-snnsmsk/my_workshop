<?php

function filtrele($e){
    return is_array($e) ? array_map('filtrele',$e) : strip_tags(htmlspecialchars(trim($e))) ;
}
$security0 = array_map('filtrele' ,$_REQUEST) ;


function security($e){
    return strip_tags(htmlspecialchars(trim($e))) ;
}

?>