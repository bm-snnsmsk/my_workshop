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
        
    // usort()

    $arr = ["bir","iki","yedi","bes","uc","dort","bes","alti","yedi"] ;
    $arr2 = [1,7,2,3,6,4,5,6,7] ;

    function ktob($a, $b){
        /* return $p1 < $p2 ; */
        if ($a==$b) return 0;
        return ($a<$b) ? -1 : 1;
    }

    function btok($p1, $p2){
        return $p1 > $p2 ;
    }
    

    usort($arr,"ktob");
    usort($arr2,"ktob");
    
    for($i=0; $i<count($arr);$i++)
    {
    echo $arr[$i];
    echo "<br>";
    }
  
echo "---------------------<br/>" ;

    for($i=0; $i<count($arr2);$i++)
    {
    echo $arr2[$i];
    echo "<br>";
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