<?php
     include("my_functions.php");
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
        body.bg-dark{
            background:#181818!important ;
        }
    </style>
</head>
<body class="<?php echo cookie('color') ? cookie('color') : 'bg-dark'  ?>">
    <div class="d-flex align-items-center justify-content-center p-4"><img src="kodl.png" alt=""></div>
    <div class="container d-flex align-items-center justify-content-center">
        <div class="card <?php echo cookie('color') ? cookie('color') : 'bg-dark'  ?>">
            <div class="card-header bg-primary">Giriş Yap</div>
            <div class="card-body">
               <?php if(session('error')){ ?>
                <div class="alert alert-danger">
                    <?php echo session('error') ? session('error') : null ; ?>
                </div>
                <?php } ?>
                
                <form action="islem.php?islem=giris" method="post">
                    <label for="username" class="text-success">Kullanıcı Adınız  </label>
                    <input type="text" name="username" id="username" class="form-control" value="<?php echo session('username') ; ?>">
                    <label for="password" class="text-success">Şifreniz  </label>
                    <input type="text" name="password" id="password" class="form-control mb-4">
                    <button class="btn btn-success mb-4 w-100">Giriş Yap</button>
                </form>
            </div>
           
            <div class="card-footer bg-info d-flex align-items-center justify-content-between">
                <a href="islem.php?islem=renk&color=bg-light" class="btn btn-sm btn-light">Light Mode</a>
                <a href="islem.php?islem=renk&color=bg-dark" class="btn btn-sm btn-dark">Dark Mode</a>
            </div>            
        </div>
    </div>
 
 <div class="text-light">
 <?php

echo date_default_timezone_get()."<br>";
echo date("d.m.Y - H:i:s" )."<br>";
date_default_timezone_set("Europe/Istanbul") ;
echo date_default_timezone_get()."<br>";
echo date("d.m.Y - H:i:s" );
?>

 </div>

</body>
</html>

