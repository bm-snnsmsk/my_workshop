<?php
$categories = [
    
    [
        'id' => 1 ,
        'parent' => 0 ,
      'name' => "Front - End"
    ], 
    [
        'id' => 2 ,
        'parent' => 0 ,
      'name' => "Back - End"
    ], 
    [
        'id' => 3 ,
        'parent' => 2 ,
      'name' => "PHP"
    ], 
    [
        'id' => 4 ,
        'parent' => 1 ,
      'name' => "VueJs"
    ], 
    [
        'id' => 5 ,
        'parent' => 2 ,
      'name' => "Java"
    ], 
    [
        'id' => 6 ,
        'parent' => 1 ,
      'name' => "Javascript"
    ],
    [
        'id' => 7 ,
        'parent' => 2 ,
      'name' => "NodeJs"
    ], 
    [
        'id' => 8 ,
        'parent' => 3 ,
      'name' => "Laravel"
    ], 
    [
        'id' => 9 ,
        'parent' => 7 ,
      'name' => "ExpressJs"
    ]

] ;

function getCategories($arr, $parent = 0){
    $html = "" ;
    $html .= "<ul>" ;
    foreach($arr as $value){
       if($value['parent'] == $parent){
        $html .= "<li>" ;
        $html .= $value['name'] ;
        $html .= getCategories($arr, $value['id']) ;  // recursive function
        $html .= "</li>" ;
       }
    }
    $html .= "</ul>" ;
    return $html ;
}


?>