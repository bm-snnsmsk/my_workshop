<?php

$arr = [
    "isim"=>"sinan",
    "yas"=>"37",
    "bolum"=>"bilgisayar muhendisligi"
    ] ;
// echo json_encode($arr) ;

$json = file_get_contents('kisiler.json') ;

$obj = json_decode($json) ;
echo "<pre>" ;
print_r($obj) ;
echo "</pre>" ;

$arr = json_decode($json, true) ;
echo "<pre>" ;
print_r($arr) ;
echo "</pre>" ;


$count = 0 ;

foreach($arr as $key=>$item){
    echo "<ul>" ;
   if(is_array($item)){
    foreach($item as $k=>$i){
        echo "<li>" ;
        echo $i ;
        echo "</li>" ;
    }
   }
   echo "</ul>" ;
}

?>
