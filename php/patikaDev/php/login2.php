<?php
session_start() ;


?>




<!DOCTYPE html>
<html lang="tr-TR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Login</title>
    <style>
      
    </style>
</head>
<body class="bg-dark">

<div class="d-flex align-items-center justify-content-center my-3">
    <img src="kodl.png" alt="logo_resmi">
</div>


<div class="d-flex align-items-center justify-content-center">
<div class="card bg-dark">
  <div class="card-header bg-primary text-white">
  Giriş Yap
  </div>
  <div class="card-body">

  <?php

    if($_SESSION['error']){
        echo '<div class="alert alert-primary" role="alert">'. $_SESSION["error"].'</div>' ;
    }

    ?>




  <form action="islem2.php?islem=login" method="post" >

  <div class="">
    <label for="username" class="form-label text-light">Kullanıcı Adı</label>
    <input type="text" name="username"  class="form-control" id="username" aria-describedby="emailHelp" value="<?= $_SESSION['username'] ?? null ; ?>">
  </div>

  <div class="">
    <label for="parola" class="form-label text-light">Parola</label>
    <input type="password" class="form-control" name="parola"  id="parola">
  </div>
  
  <button type="submit" class="btn btn-primary btn-sm w-100 mt-3">Submit</button>

</form>

  </div>
  <div class="card-footer bg-info d-flex align-items-center justify-content-between">
  <a href="#" class="btn btn-warning">Light Mode</a>
  <a href="#" class="btn btn-danger">Dark Mode</a>
  </div>
</div> 
</div>


</body>
</html>
