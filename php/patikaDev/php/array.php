<?php
$arr = array(100,200,300,400,500,"sinan", "baran","emine","tubanur") ;
// shuffle($arr) ;
$dizi = array_map(function($e){
    if(gettype($e) == "integer"){
        return $e * 100 ;
    }else if(gettype($e) == "string"){
        return $e." 100 " ;
    }
},$arr) ;
?>