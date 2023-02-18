<?php
error_reporting(E_ALL);
require('config.php') ;
require(DIR.'/helpers/app.php') ;
require(DIR.'/controller/user.php') ;



$route = get('route');
$route = explode('@',$route) ;

$class_name = $route[0] ;
$method_name = $route[1] ;


$run = new User() ;
$run->$method_name() ;   // = $run->add() ;
// print_r($route);
?>