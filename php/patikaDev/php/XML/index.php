<?php
include('../MVC/model/user_model.php') ;
//   header("Content-type: application/xml; charset='utf8'") ;  // my_xml.xml dosyasında ayrıa belirtildiğinden burda belirtilmeye gerek yok.


// örnek çalışma 1  START
/* $kisiler = simplexml_load_file('my_xml.xml') ;

echo "<pre>" ;
print_r($kisiler) ;
echo "</pre>" ; */
// örnek çalışma 1 END 



// örnek çalışma 2  START

// bunu çalıştıramadım

/* header("Content-type: application/xml; charset='utf8'") ;
$xml = new SimpleXMLElement('<KISILER/>') ;


$db = new UserModel() ;
$kisiler = $db->list();

foreach($kisiler as $item){    
    $kisi = $xml->addChild('Kisi') ;
    $kisi->addChild('ad',$item['isim']) ;
    $kisi->addChild('memleket',$item['sehir']) ;
    $kisi->addChild('old',$item['yas']) ;
}

echo $xml->asXml(); */
// örnek çalışma 2 END 

$db = new UserModel() ;
$kisiler = $db->list();

$jsonArr = json_encode($kisiler) ;

echo $jsonArr ;



?>


