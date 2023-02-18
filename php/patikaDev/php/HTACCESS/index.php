<?php

echo "index sayfası</br></br>" ;

if(isset($_GET['route'])){
    echo $_GET['route'].'</br></br>' ?? "route değeri boş</br></br>" ;
}else{
    echo "" ;
}

print_r($_GET) ;
?>