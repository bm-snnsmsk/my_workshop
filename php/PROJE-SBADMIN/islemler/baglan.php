<?php

$host = 'localhost' ;
$dbname = "abc-kurs" ;
$username = "root" ;
$pass = "" ;

try{
    $DBConnect = new PDO('mysql:host='.$host.';dbname='.$dbname.';charset=utf8',$username, $pass) ;
    if($DBConnect){
        //echo "bağlantı başarılı" ;
    }else{
        //echo "bağlantı başarısız" ;
    }
}catch(PDOException $e){
    echo $e->getMessage() ;
}









?>

