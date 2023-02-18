<?php
// namespace snnsmsk ; // en başa yazılması gerekiyor

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
        //namespace snnsmsk ;

       // phpinfo(INFO_ALL) ;


       

        echo __DIR__."<br/>" ;  // C:\xampp\htdocs\apps\PHP        
        echo __FILE__."<br/>";  // C:\xampp\htdocs\apps\PHP\php008.php
        echo __NAMESPACE__."<br/>";  



        $num1 = 25 ; 
        $num2 = 0 ;
        try{
            if($num2 == 0 ){
                throw new Exception("ikinci sayı sıfır olamaz") ;
            }
            echo $num1 / $num2 ;
        }catch(Exception $e) {
           echo $e->getMessage() ;
        }finally{
            echo "<br/>Hata olsa da olmasa da çalışan kodlar...";
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