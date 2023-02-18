<?php
require("../MVC/model/user_model.php");

$connect = new UserModel();

$islem = $_GET['islem'] ?? null ;

print_r($_POST) ;

?>