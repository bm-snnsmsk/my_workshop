<?php
// namespace snnsmsk ; // en başa yazılması gerekiyor
require_once("MyClasses/Security.php") ;
require_once("MyClasses/FileUpload.php") ;
require_once("MyClasses/RegExp.php") ;
require_once("MyClasses/Cookie.php") ;
require_once("MyClasses/Session.php") ;
require_once("MyClasses/Router.php") ;
require_once("MyClasses/Date.php") ;
require_once("MyClasses/Config.php") ;
require_once("MyClasses/File.php") ;

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
$icerik  =  "  başka bir satıri";
$icerik2 = " yeni  bir satıri";
$path = 'File/test.txt' ;
$p = new File($path) ;
/* 
    $path ='test1' ;


   // $p->addFile($icerik2);
   $p->removeDIR(); */
 /*    echo $p->readFile();

 */

 echo $p->getTotalDiscSpace().'<br/>' ;
 echo $p->getFreeDiscSpace() ;


?>   



       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>