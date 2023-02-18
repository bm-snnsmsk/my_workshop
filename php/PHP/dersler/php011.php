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

           
            $text = "www.want.comgfgfgfg" ;
            
            $regExp = new RegExp() ;         
            
            echo "<br/>----------------<br/>" ;
           if($regExp->isUrl($text)['isUrl']){
            echo "bu bir url " ;
           }else{
            echo "bu bir url adresi değildir..." ;
           }

           echo "<br/>".$regExp->isUrl($text)['urlLength'] ;

          
            
            
          
            


            ?>   
  
       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>