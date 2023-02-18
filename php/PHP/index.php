<?php
require_once("MyClasses/Security.php") ;
?>

<!DOCTYPE html>
<html lang="tr-TR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
    <title>Document</title>
    <style>       
       @import url('css/abc.css');
    </style>
</head>
<body>
<p id="demo"></p>

<?php

function isLetter($text){
    $regExp = "/[^a-zA-ZçğıöşüÇĞIİÖŞÜ]/u" ;
    $result = preg_match($regExp, $text) ? false : true ;
    return $result ;
}
function isNumber($text){
    $regExp = '/[^0-9]/' ;
    $result = preg_match($regExp, $text) ? false : true ;
    return $result ;
}
function isEmail($text){
    $result = filter_var($text, FILTER_VALIDATE_EMAIL) ;
    return $result ;
}    

$text = '2022-11-05' ;

echo var_dump($text) ;

?>


                                        











</body>
</html>