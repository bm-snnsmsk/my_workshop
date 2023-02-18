<?php
session_start() ;

if(!isset($_SESSION['login']) || $_SESSION['login'] == false){
    header('Location:login2.php') ;
}

if(file_exists('ddd/'.$_SESSION['k_adi'].'.txt')){
    $icerik = file_get_contents('ddd/'.$_SESSION['k_adi'].'.txt') ;
}else{
    $icerik = "" ;
}

?>



<!DOCTYPE html>
<html lang="tr-TR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Anasayfa</title>
    <style>
        button{
            position:absolute ;
            bottom:15px;
            right:5px;
        }
        form{
            position:relative ;
        }
    </style>
</head>
<body class="bg-dark">

<div class="d-flex align-items-center justify-content-center my-3">
    <img src="kodl.png" alt="logo_resmi">
</div>

<div class="d-flex align-items-center justify-content-center">
<div class="card bg-dark">
  <div class="card-header bg-primary text-warning ">
    <h5 class="card-title ">Hoşgeldiniz <?=  strtoupper($_SESSION['adi']).' '.strtoupper($_SESSION['soyadi']) ?></h5>
    <h6 class="card-subtitle text-muted"><?=  $_SESSION['email']?></h6>
  </div>
  <div class="card-body">   



   <form action="islem2.php?islem=icerik" class="bg-dark" method="post">
  <textarea name="hakkimda" id="" cols="30" rows="10"><?= $icerik ; ?>
  </textarea>
    <button class="btn btn-primary" type="submit">Kaydet</button>
   </form>
   <a href="islem2.php?islem=logout" class="btn btn-success w-100">Oturumu Kapat</a>
  </div>
  <div class="card-footer bg-info d-flex align-items-center justify-content-between">
  <a href="#" class="btn btn-warning">Light Mode</a>
  <a href="#" class="btn btn-danger">Dark Mode</a>
  </div>
</div> 
</div>
</body>
</html>
<?php
$_SESSION["error"] = "" ;
$_SESSION['username'] = "" ;
?>