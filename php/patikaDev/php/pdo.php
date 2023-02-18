<?php

$host = 'localhost' ;
$dbname = "test" ;
$userName = "root" ;
$pass = "";
$characterSet = "utf8" ;

try{
    $dbConnect = new PDO("mysql:host=".$host.";dbname=".$dbname.";charset=".$characterSet, $userName, $pass) ;
    $dbConnect->query("SET @@lc_time_names = 'tr_TR'") ;
    $dbConnect->query("SET CHARACTER SET utf8") ;
    $dbConnect->query("SET CHARACTER_SET_CONNECTION=utf8") ;
    $dbConnect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION) ;
    if($dbConnect){
        echo "bağlantı başarılı" ;
    }else{
        echo "bağlantı hatalı" ;
    }
}catch(PDOException $e){
    echo $e->getMessage() ;
}

// query()
/*  $sorgu =  $dbConnect->query("SELECT * FROM pdo LIMIT 5") ;
$kayitlar = $sorgu->fetchAll(PDO::FETCH_ASSOC) ; */
$sql = "SELECT * FROM pdo WHERE isim LIKE 'b%'" ;
$sql2 = "SELECT MAX(yas) as en_yasli, MIN(yas) as en_genc, COUNT(id) as toplam_kayit, SUM(yas) as toplam_yas, (SUM(yas) / COUNT(id)) as yas_ortalamasi  FROM pdo" ;
$sql3 = "SELECT sehir, COUNT(sehir) AS toplam_kayit FROM pdo GROUP BY sehir HAVING toplam_kayit > 1" ;
$sql4 = "SELECT * FROM pdo WHERE sehir IN('mardin','batman','siirt')" ;
//$sql4 = "SELECT * FROM pdo WHERE sehir NOT IN('mardin','batman','siirt')" ;
$sql5 = "SELECT *,REPLACE(grup,' ','') AS new_grup  FROM pdo WHERE FIND_IN_SET('D',REPLACE(grup,' ',''))" ;
$sql6 = "SELECT * FROM pdo WHERE id BETWEEN  5 AND 8 " ;

/* 
// tablo oluşturma sorgusu
$sorgu2 =  $dbConnect->query("CREATE TABLE IF NOT EXISTS group (
    groupID INT(1) AUTO_INCREMENT,
    group_name VARCHAR(50),
    PRIMARY_KEY(groupID)
)") ; */
/*

$sorgu2 =  $dbConnect->query("UPDATE pdo SET isim='süleyman' WHERE id=4 ") ;
$sorgu3 =  $dbConnect->query("DELETE FROM pdo WHERE id=4 ") ;
$sorgu4 =  $dbConnect->query("INSERT INTO  pdo (isim) VALUES ('mehmet')") ; 
*/

// prepare()
/* $sorgu2 =  $dbConnect->prepare("UPDATE pdo SET isim=? WHERE id= ? ") ;
$sorgu2->execute(['sinan',7]) ;
$sorgu3 =  $dbConnect->prepare("DELETE FROM pdo WHERE id= ? ") ;
$sorgu3->execute([8]) ;
$sorgu4 =  $dbConnect->prepare("INSERT INTO  pdo (isim) VALUES (?)") ;
$sorgu4->execute(['binefş']) ; */

$sorgu =  $dbConnect->query($sql) ;
$kayitlar = $sorgu->fetchAll(PDO::FETCH_ASSOC) ;
$sorgu2 =  $dbConnect->query($sql2) ;
$kayitlar2 = $sorgu2->fetch(PDO::FETCH_ASSOC) ;
$sorgu3 =  $dbConnect->query($sql3) ;
$kayitlar3 = $sorgu3->fetchAll(PDO::FETCH_ASSOC) ;
$sorgu4 =  $dbConnect->query($sql4) ;
$kayitlar4 = $sorgu4->fetchAll(PDO::FETCH_ASSOC) ;
$sorgu5 =  $dbConnect->query($sql5) ;
$kayitlar5 = $sorgu5->fetchAll(PDO::FETCH_ASSOC) ;
$sorgu6 =  $dbConnect->query($sql6) ;
$kayitlar6 = $sorgu6->fetchAll(PDO::FETCH_ASSOC) ;

echo "<ul>" ;
foreach($kayitlar as $key => $value){
    echo "<li>".$value['id']." - ".$value['isim']." - ".$value['sehir']." - ".$value['yas']."</li>" ;
}
echo "</ul>" ;

echo "<pre>" ;
print_r($kayitlar2) ;
echo "</pre>" ;

echo "<pre>" ;
print_r($kayitlar3) ;
echo "</pre>" ;

echo "<ul>" ;
foreach($kayitlar4 as $key => $value){
    echo "<li>".$value['id']." - ".$value['isim']." - ".$value['sehir']." - ".$value['yas']."</li>" ;
}
echo "</ul>" ;

echo "<pre>" ;
print_r($kayitlar5) ;
echo "</pre>" ;
echo "<ul>" ;
foreach($kayitlar5 as $key => $value){
    echo "<li>".$value['id']." - ".$value['isim']." - ".$value['sehir']." - ".$value['grup']."</li>" ;
}
echo "</ul>" ;


echo "<ul>" ;
foreach($kayitlar6 as $key => $value){
    echo "<li>".$value['id']." - ".$value['isim']." - ".$value['sehir']." - "."</li>" ;
}
echo "</ul>" ;



?>