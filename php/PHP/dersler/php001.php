<?php
include("static/header.php") ;
?>    
<!-- body START  -->




<div class="container-fluid">
    <div class="alert alert-primary">
        <?php
            echo "hello php"."<br/>" ;


            $x = 30 ;
            function test(){
                // global $x ;
                // echo "x  = ".$x."<br/>" ;
                echo "x  = ".$GLOBALS['x']."<br/>" ;
            }
            test() ;
            echo "x  = ".$x."<br/>" ;

            // static
            
            function statik(){
                static $y = 50 ;
                echo $y."<br/>" ;
                $y++ ;
            }
            statik();
            statik();
            statik();

        ?>
    </div>
    <h2><?php echo "again first class" ; ?> </h2>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>