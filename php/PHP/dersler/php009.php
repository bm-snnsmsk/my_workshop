<?php
// namespace snnsmsk ; // en başa yazılması gerekiyor
require_once("MyClasses/Security.php") ;
include("static/header.php") ;


?>    
<!-- body START  -->




<div class="container-fluid">
    <div class="card">
        <div class="card-header">
            <h2>string metotlar</h2>
        </div>
       <div class="card-body">


<?php 

// if(!$_POST){
?>
 <form action="<?= Security::security($_SERVER['PHP_SELF']); ?>" method="POST">
  <div class="mb-3">
    <label for="name" class="form-label">Adı</label>
    <input type="text" class="form-control" id="name"  name="name" aria-describedby="emailHelp">
  </div>

  <div class="form-check">
  <input class="form-check-input" type="checkbox" value="css" id="css" name="diller[]">
  <label class="form-check-label" for="css">
   css
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="asp" id="asp" name="diller[]">
  <label class="form-check-label" for="asp">
   asp
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="js" id="js" name="diller[]">
  <label class="form-check-label" for="js">
   js
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="html" id="html" name="diller[]">
  <label class="form-check-label" for="html">
   html
  </label>
</div>
  
  <button type="submit" class="btn btn-primary">Submit</button>
</form>


       <?php
       
      /*  $a = "25" ;
       echo gettype($a)."<br/>" ;
       $b = (int)$a ;
       echo gettype($b)."<br/>" ;

 */
// }else{
// print_r($_POST) ;

if($_POST){
  $name = $_POST['name'] ;
$diller = $_POST['diller'] ;
$txt = "";
foreach($diller as $value){
    $txt.=$value." " ;
}



echo  "merhaba ".$name."<br/>Seçtiğiniz diller : ".$txt;


}






//}


        ?>
            
   
  
       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>