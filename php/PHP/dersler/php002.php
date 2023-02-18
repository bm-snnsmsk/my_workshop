<?php
include("static/header.php") ;
?>    
<!-- body START  -->




<div class="container-fluid">
    <div class="alert alert-danger">
        <?php
            $a = "sinan" ;
            $b = 20 ;
            $c = 3.14 ;
            $d = ["a", "b", 20] ;
            $e = true ;
            $f = null ;
            class Car{
                function Car(){
                    $this->model="audio" ;
                }
            }
            $g = new Car() ; ;

            var_dump($a) ;
            echo "<br/>";
            var_dump($b) ;
            echo "<br/>";
            var_dump($c) ;
            echo "<br/>";
            var_dump($d) ;
            echo "<br/>";
            var_dump($e) ;
            echo "<br/>";
            var_dump($f) ;
            echo "<br/>";
            var_dump($g) ;

        ?>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>