<?php
    include("my_functions.php");
    session_start() ;
if(!isset($_SESSION['login']) || $_SESSION['login'] == false){
        header('Location:login.php') ;
}

if(file_exists('db/'.session('kullanici_adi').'.txt')){
        $hakkimda = file_get_contents('db/'.session('kullanici_adi').'.txt') ; 
}else{
        $hakkimda = "" ;
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
        body.bg-dark{
            background:#181818!important ;
        }
        button{
            position:absolute;
            bottom:8px;
            right:8px;
        }
        form{
            position:relative;
        }
    </style>
</head>
<body class="<?php echo cookie('color') ? cookie('color') : 'bg-dark'  ?>">
    <div class="d-flex align-items-center justify-content-center p-4"><img src="kodl.png" alt=""></div>
    <div class="container d-flex align-items-center justify-content-center">
        <div class="card <?php echo cookie('color') ? cookie('color') : 'bg-dark'  ?>" style="width:18rem">
            <div class="card-header bg-primary">Profilim</div>
            <div class="card-body">
              <h5 class="card-title text-warning"><?php echo session('kullanici_adi') ; ?></h5>
              <h6 class="card-subtitle mb-2 text-muted"><?php echo session('eposta') ; ?></h6>

              <?php
                if(get('islem') == 'ok'){
                    echo "<div class='alert alert-success'>işlem başarılı</div>" ;
                }else if(get('islem') == 'hata'){
                    echo "<div class='alert alert-danger'>işlem hatalı</div>" ;
                }
              ?>
                
                <form action="islem.php?islem=hakkimda" method="post">
                   <textarea class="form-control <?php echo cookie('color') ? cookie('color') : 'bg-dark'  ?> text-primary" name="hakkimda" id="" cols="30" rows="10">
                    <?php
                      echo $hakkimda ;
                    ?>
                   </textarea>
                   <button class="btn btn-sm btn-primary mt-2" type="submit">Kaydet</button>
                </form>
                <a href="islem.php?islem=oturumu_kapat"  class="btn btn-sm btn-success mt-2 w-100">Oturumu Kapat</a>
            </div>
           
            <div class="card-footer bg-info d-flex align-items-center justify-content-between">
                <a href="islem.php?islem=renk&color=bg-light" class="btn btn-sm btn-light">Light Mode</a>
                <a href="islem.php?islem=renk&color=bg-dark" class="btn btn-sm btn-dark">Dark Mode</a>
            </div>            
        </div>
    </div>
    
</body>
</html>
