<?php
// namespace snnsmsk ; // en başa yazılması gerekiyor
require_once("MyClasses/Security.php") ;
require_once("MyClasses/File.php") ;
include("static/header.php") ;


?>    
<!-- body START  -->




<div class="container-fluid">
    <div class="card">
        <div class="card-header">
            <h2>File Load</h2>
        </div>
       <div class="card-body">

       <h1>tek dosya</h1>
       <form action="<?= Security::security($_SERVER['PHP_SELF']); ?>" method="POST" enctype="multipart/form-data">
  <div class="mb-3 form-group">
    <input type="file" class="form-control" id="myfile" name="myfile" multiple>
  </div>

  <button type="submit" name="control0" class="btn btn-primary">Submit</button>
</form>


<h1>çoklu dosya</h1>
 <form action="<?= Security::security($_SERVER['PHP_SELF']); ?>" method="POST" enctype="multipart/form-data">
  <div class="mb-3 form-group">
    <input type="file" class="form-control" id="myFile" name="myFile[]" multiple>
  </div>

  <button type="submit" name="control" class="btn btn-primary">Submit</button>
</form>


       <?php
       
       

       
      if(isset($_FILES['myfile']) && isset($_POST['control0'])){
        $file = new File('myfile', 'upload') ;
        $result = $file->fileLoad() ;
        if($result){
          echo '<pre>' ;
          print_r($result) ;
          echo '</pre>' ;
          echo "<img src='".$result['filePath']."'>" ;  
        }else{
          echo $result['message'] ;
        }
     

      }




      if(isset($_FILES['myFile']) && isset($_POST['control'])){
        $file = new File('myFile', 'upload') ;
        $result = $file->multipleFileLoad() ;
        if($result){
          echo '<pre>' ;
          print_r($result) ;
          echo '</pre>' ;
         // echo "<img src='".$result['filePath']."'>" ;  
        }else{
         // echo $result['message'] ;
        }
     

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