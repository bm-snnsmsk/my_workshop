<?php
// namespace snnsmsk ; // en başa yazılması gerekiyor
require_once("MyClasses/Security.php") ;
require_once("MyClasses/File.php") ;
require_once("MyClasses/RegExp.php") ;
require_once("MyClasses/Cookie.php") ;
require_once("MyClasses/Session.php") ;
require_once("MyClasses/Router.php") ;

include("static/header.php") ;


?>    
<!-- body START  -->




<div class="container-fluid">
    <div class="card">
        <div class="card-header">
            <h2>Düzenli İfadeler</h2>
        </div>
       <div class="card-body"> 

            <?php

  
$name = "brann2" ;
$value = "ayu üniversitesi" ;

            
            
$sess = new Session() ;         
$router = new Router() ;         

 echo "<br/>----------------<br/>" ;
 Session::setSession($name, $value);
 Session::setSession("baran", "1.5 yaşında");
 Session::setSession("tubanur", "ana sınıf öğrencisi");
 Session::setSession("emine", "çocuk gelişimşi");
 Session::setSession("sinan", "Bilgisayar mühendisliği");


/* echo "<br/>----------------<br/>" ;
if($regExp->isIP($text)['isIP']){
echo "bu bir IP " ;
}else{
echo "bu bir IP adresi değildir..." ;
}

echo "<br/>".$regExp->isIP($text)['isIP'] ;
echo "<br/>".$regExp->isIP($text)['IPMessage'] ;

 */

echo "<pre>" ;
print_r($_SESSION) ;
echo "</pre>" ;


echo "<br/>----------------<br/>"  ;

/* Session::deleteAllSessions() ;
echo "<pre>" ;
print_r($_SESSION) ;
echo "</pre>" ;
 */

echo "<br/>----------------<br/>"  ;

echo '<script>
document.write(document.cookie) ;
</script>
';


            ?>   


       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>