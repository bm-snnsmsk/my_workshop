<?php
function ucgen($satir){
    $init = 1 ;
    $result = "" ;
    while($init <= $satir){
        for($j = 0 ; $j < $init ; $j++){
            $result.="0 " ;
        }
        $result.="<br/>" ;
        $init++ ;
    }
    return $result ;
}

//echo ucgen(15) ;

?>