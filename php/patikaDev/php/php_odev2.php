<?php

$planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "", "", NULL];


function getPlanet($arr, $count = 3 ){
    $boslariSil = array_filter($arr) ;
    $rastgeleArr = array_rand($boslariSil, $count) ;    
    $duzenlenmisArr = array_map(function($e) use ($boslariSil){
        return $boslariSil[$e] ;
    },$rastgeleArr) ;
    return  $duzenlenmisArr ;
}


/* print_r(getPlanet($planets)) ; 
print_r(getPlanet($planets, 2)) ; 
print_r(getPlanet($planets, 3)) ; 
print_r(getPlanet($planets, 5)) ;  */
?>
