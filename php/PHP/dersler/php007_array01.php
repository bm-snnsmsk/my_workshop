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
            ["skoda", 2, 21 ],
            ["nissan", 1, 22 ],
            ["bmw", 3, 15 ],
            ["tofaş", 4, 5 ],
            ["fiat", 8, 3 ]
          ] ;

        /*   for($i = 0 ; $i < count($cars); $i++){
            echo "<p><strong>Satır numarası : ".$i."</p></strong>" ;
            echo "<ul>" ;
            for($j = 0 ; $j < count($cars[$i]); $j++){
                echo "<li><i>".$cars[$i][$j]."</li></i>" ;
            }
            echo "</ul>" ;
          }
 */

 $i = 0 ;
foreach($cars as $key => $value){
    echo "<p><strong>Satır numarası : ".++$i."</p></strong>" ;
    echo "<ul>" ;
    foreach($value as $key2 => $value2){
        echo "<li><i>".$value2."</li></i>" ;
    }
    echo "</ul>" ;
  }



            
        ?>
       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>