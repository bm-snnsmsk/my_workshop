<?php
// fonksiyonlar
function security($e){
    return strip_tags(htmlspecialchars(trim($e))) ;
}
error_reporting(0) ;
?>


<!DOCTYPE html>
<html lang="tr-TR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>PHP ÖDEV 3 </title>
</head>
<body>
    
<div class="container mx-auto my-5 " style="width:500px">
<form action="<?php echo($_SERVER['PHP_SELF']) ; ?>" method="get" class="" style="width:500px">

<div class="container mx-auto">
<div class="row">
 <div class="col-3">  
    <label for="sss" class="form-label">Bir sayı giriniz</label></div>
   <div class="col-3">
   <input type="text" class="form-control" id="sss" name="sayi">
   </div>
 </div>
 
<div class="row mt-2">
    <div class="offset-3 col-3">
         <button type="submit" class="btn btn-primary w-100">Hesapla</button>
    </div>
</div>
</div>


<div class="row mt-3">
    <div class="offset-3 col-9">
        <p id="sonuc">
            <?php
                $gelen_sayi = security($_GET['sayi']) ;
               
             
                if($gelen_sayi % 3 == 0){
                    echo $gelen_sayi.", 3 ile tam bölünebilen bir sayıdır." ;
                }else{
                    if($gelen_sayi % 3 == 1){                        
                         echo $gelen_sayi.", 3 ile tam bölünemeyen bir sayıdır. <br/>".($gelen_sayi + 2).", 3 ile tam bölünebilen bir sayıdır." ;
                    }else if($gelen_sayi % 3 == 2){                        
                        echo $gelen_sayi.", 3 ile tam bölünemeyen bir sayıdır. <br/>".($gelen_sayi + 1).", 3 ile tam bölünebilen bir sayıdır." ;
                    }
                }
             
            ?>
        </p>
    </div>
</div>
</div>

 
 
</form>
</div>



</body>
</html>
