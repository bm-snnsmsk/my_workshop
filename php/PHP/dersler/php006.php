<?php
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
           $user = "" ;

            echo $user ?? "kayıt bulunamadı - 1" ;
            echo "<br/>" ;
            echo !empty($user) ? $user : "kayıt bulunamadı - 2" ;

            echo "ieisdsdsdsei" ;



            
        ?>
       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>