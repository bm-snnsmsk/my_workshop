<?php
// namespace snnsmsk ; // en başa yazılması gerekiyor
require_once("MyClasses/Security.php") ;
require_once("MyClasses/File.php") ;
require_once("MyClasses/RegExp.php") ;

include("static/header.php") ;


?>    
<!-- body START  -->




<div class="container-fluid">
    <div class="card">
        <div class="card-header">
            <h2>Düzenli İfadeler</h2>
        </div>
       <div class="card-body"> 

            <?php

  
$text = "129:0:0:0:e334:1:1:1:3" ;
            
$regExp = new RegExp() ;         

echo "<br/>----------------<br/>" ;
if($regExp->isIP($text)['isIP']){
echo "bu bir IP " ;
}else{
echo "bu bir IP adresi değildir..." ;
}

echo "<br/>".$regExp->isIP($text)['isIP'] ;
echo "<br/>".$regExp->isIP($text)['IPMessage'] ;




          
            


            ?>   
  
       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>