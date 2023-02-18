<?php
require("config/config.php") ;

?>
<!DOCTYPE html>
<html lang="tr-TR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Güvenlik Deneme</title>
    <link rel="stylesheet" href="public\style.css">
</head>
<body>

<form action="" method="post">
    <input type="text" name="username" id=""><br>
    <textarea name="mesaj" cols="30" rows="5"></textarea><br>
    <button type="submit">Gönder</button>
</form>
<?php
setcookie('my_cookie1','Sinan',time()+86400) ;
setcookie('my_cookie2','simsek',time()+86400) ;

echo strip_tags($_POST['username']) ?? '' ;




$listele = $connect->list() ;
echo "<pre>";
print_r($listele) ;
echo "</pre>";
?>
</body>
</html>