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
          $cars = [
            "dog",
            "cat",
            "rabbit",
            "zebra",
            "bear",
            "bird",
            "horse"
          ] ;



          
    // array_multisort()
    array_multisort($cars,SORT_DESC) ;
 
    echo "<ul>" ;
    foreach($cars as $key => $value){
      echo "<li><i>".$value."</i></li>" ;
    }
    echo "</ul>" ;


     // array_pad()
    $cars2 = array_pad($cars, -15, "---") ;
    echo "<ul>" ;
    foreach($cars2 as $key => $value){
      echo "<li><i>".$value."</i></li>" ;
    }
    echo "</ul>" ;


    // array_reduce()
    $arr = ["bir","iki","uc","dort","bes","alti","yedi"] ;
    $arr2 = [1,2,3,4,5,6,7] ;
    function f($p1, $p2){
        return $p1." - ".$p2 ;
    }
    function f2($p1, $p2){
        return $p1 + $p2 ;
    }

    echo array_reduce($arr, "f")."<br/>" ; // sağdan birleştirme yapar
    echo array_reduce($arr, "f","sifir")."<br/>"  ; // sağdan birleştirme yapar
    echo array_reduce($arr2, "f2","10")."<br/>"  ; // sağdan toplama yapar
    

            
        ?>
       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>