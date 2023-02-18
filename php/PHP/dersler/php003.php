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
            $a = "sinan şimşek bilgisayar mühendisliği" ;
            $a = "sinan simsek '3' bilgisayar muhendisligi" ;
            $num1 = 32 ;
            $num2 = 65 ;
            $num3 = -65 ;
            $char = 65 ;
            $money = 7200.56 ;

            echo "strlen($a) => ".strlen($a) ;
            echo "<br/>str_word_count($a) => ".str_word_count($a) ;
            echo "<br/>strrev($a) => ".strrev($a) ;
            echo "<br/>strpos($a,'bil') => ".strpos($a,"bil") ;
            echo "<br/>str_replace('sinan','baran',$a) => ".str_replace('sinan','baran',$a) ;
            echo "<br/>addcslashes($a,'i') => ".addcslashes($a,'i') ;
            echo "<br/>addslashes($a) => ".addslashes($a) ;
            echo "<br/>bin2hex($a) => ".bin2hex($a) ;
            echo "<br/>bin2hex(1001) => ".bin2hex(1001) ;
            echo "<br/>chop($a,'muhendisligi') => ".chop($a,'muhendisligi') ; // son elemanı siler
            echo "<br/>chr(65) => ".chr(65) ;  // binary
            echo "<br/>chr(065) => ".chr(065) ; // oktal
            echo "<br/>chr(0x65) => ".chr(0x65) ;  // hex
            echo "<br/>chunk_split($a,2,'...') => ".chunk_split($a,2,'...') ;
            $aaa = convert_uuencode($a) ;
            echo "<br/>convert_uuencode($a) => ".$aaa ;
            echo "<br/>convert_uudecode($aaa) => ".convert_uudecode($aaa) ;
            echo "<br/>crc32($a) => ".crc32($a)."<br/>" ;
            print_r(explode(' ',$a)) ; // 0, 1, 2, 6, -1 gibi dizinin eleman sayısı belirlenebilir. -1 son elemanı diziye dahil etmez
            printf('<br/>b = %b',$num1) ;
            printf('<br/>c = %c',$char) ;
            printf('<br/>d = %d',$num1) ;
            printf('<br/>d = %d',$num2) ;
            printf('<br/>e = %e',$num1) ;
            printf('<br/>E = %E',$num1) ;
            printf('<br/>u = %u',$num1) ;
            printf('<br/>u = %u',$num2) ;
            printf('<br/>f = %f',$num1) ; // float
            printf('<br/>F = %F',$num1) ;
            printf('<br/>g = %g',$num1) ;
            printf('<br/>G = %G',$num1) ; 
            printf('<br/>s = %s',$num1) ; // string
            printf('<br/>x = %x',$num1) ; // hexadecimal
            printf('<br/>X = %X',$num1) ; // hexadecimal
            printf('<br/>o = %o',$num1) ; // oktal
            printf('<br/>+d pozitif = %+d',$num1) ; 
            printf('<br/>+d negatif = %+d',$num3) ; 
            
            echo "<br/>".similar_text("sinan","sinanl",$yuzde) ;
            echo "<br/>". $yuzde ;


            
        ?>
       </div>
    </div>
</div>




   
<!-- body END  -->
<!-- footer START -->
<?php
include("static/footer.php") ;
?>