<?php
namespace bm_snnsmsk ; // en başa yazılması gerekiyor





include("static/header.php") ;
require_once "MyClasses/Starter.php" ;



?>    
<!-- body START  -->




<div class="container-fluid">
    <div class="card">
        <div class="card-header">
            <h2>OOP </h2>
        </div>
       <div class="card-body"> 


<?php
$DB = new Database() ;


$name = "emine";
$lastname = "şimşek" ;
$item = $DB->customQuery("DELETE FROM uyeler100 WHERE testID = ?", [6]) ;


if($item > 0){
    echo "işlem başarılı ";
}else{
    echo "işlem başarısız" ;
} 

echo "<pre>" ;

    print_r($item) ;

echo "</pre>" ; 


/* echo "<pre>" ;
foreach($item as $items){
    echo $items."<br/>" ;
}
echo "</pre>" ;  */


?>   


       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>