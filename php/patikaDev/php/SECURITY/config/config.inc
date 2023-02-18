<?php
require("../../MVC/model/user_model.php") ;

$connect = new UserModel() ;
$listele = $connect->list() ;

echo "<pre>";
print_r($listele) ;
echo "</pre>"; 
?>