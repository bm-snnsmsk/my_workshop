<?php
//namespace bm_snnsmsk ; // en başa yazılması gerekiyor
libxml_use_internal_errors(true) ;




include("static/header.php") ;
require_once "MyClasses/AllClasses.php" ;



?>    
<!-- body START  -->




<div class="container-fluid">
    <div class="card">
        <div class="card-header">
            <h2>OOP </h2>
        </div>
       <div class="card-body"> 


<?php


$xmlFile = "test.xml" ;
$xml = "<?xml version='1.0' encoding='UTF-8' ?>
    <note> 
    <to>sinan</to>
    <from>emine</from>
    <heading>hatırarıtıcı</heading>
    <body>bu hafta sonu beni unutma</body>
    </note>" ;








?>   



       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>