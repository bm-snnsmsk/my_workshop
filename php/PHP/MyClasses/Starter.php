<?php

// namespace bm_snnsmsk ; class A{}
// namespace bm_snnsmsk/Database ; class B{}
// namespace bm_snnsmsk/View/Home ; class C{}

spl_autoload_register(function($class){
    $namespace = "bm_snnsmsk\\" ;
    $baseDIR = __DIR__."/" ;
    $length = strlen($namespace) ;
    if(strncmp($namespace, $class, $length) != 0){
        return ;
    } 
    $path = $baseDIR.str_replace("\\","/",substr($class, $length)).".php" ;
    if(file_exists($path)){
        require_once($path) ;
    }
}) ;



?>