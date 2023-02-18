<?php
namespace bm_snnsmsk ; // en başa yazılması gerekiyor





include("static/header.php") ;
require_once "MyClasses/Starter.php" ;


?>    
<!-- body START  -->

<div class="body_content">




<div class="container-fluid">
    <div class="card">
        <div class="card-header">
            <h2>CURL </h2>
        </div>
       <div class="card-body"> 

       <?php
       
$db = new Curl();
$db->setUrl('https://www.hepsiburada.com/') ;
echo $db->getImages() ;


?>


       
       </div>
    </div>
</div>






 

<script src="js/jquery-3.6.1.min.js"></script>
<script>
let SITE_URL = "http://localhost/apps/PHP/" ;

</script>
<!-- body END  -->
<!-- footer START -->

<?php
include("static/footer.php") ;
?>