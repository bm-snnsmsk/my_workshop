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
            $a = 360 ;
            $x = 1100 ;
         
            
           
            echo "<br/>".deg2rad($a) ;
            echo "<br/>".rad2deg(6.2831853071796) ;
            echo "<br/>".base_convert($x,2,10) ;
            echo "<br/>".rand() ;
            echo "<br/>".rand(0,49) ;
            echo "<br/>".intdiv(25,4) ;
            echo "<br/>".fmod(25,4) ;
            echo "<br/>".hypot(7,24) ;
            echo "<br/>".getrandmax() ;
            echo "<br/>".mt_getrandmax() ;




            
        ?>
       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>