<?php

/* echo "<pre>";
print_r(curl_version()) ;
echo "</pre>"; */


// örnek  1 START 
       /*  $path = "https://www.google.com" ;
        $my_curl = curl_init($path);
        curl_exec($my_curl);
        curl_close($my_curl);  */
// örnek  1 END 



// örnek  2 START 
     /*   $path = "https://www.patika.dev" ;
        $my_curl = curl_init();
        curl_setopt($my_curl,CURLOPT_URL,$path);
        curl_setopt($my_curl,CURLOPT_RETURNTRANSFER,true);
        $result = curl_exec($my_curl);
        curl_close($my_curl);

        $desen = '@<h2 class="emphasis-small-header bootcamp-card">(.*?)</h2>@';
        preg_match_all($desen,$result,$eslesme);
        $result = 0;
        foreach ($eslesme[1] as $item) {
            echo ++$result.' - '.$item."<br>---<br>";
        }  */
// örnek  2 END 



// örnek  2 START 
$path = "https://www.patika.dev/" ;
$my_curl = curl_init();
curl_setopt_array($my_curl,[
    CURLOPT_URL => 'https://jsonplaceholder.typicode.com/posts' ,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true ,
    CURLOPT_HTTPHEADER => [
        'Content-Type : application/json'
    ] ,
    CURLOPT_POSTFIELDS => json_encode([
        'title' => 'Test title' ,
        'body' => 'Test body' ,
        'UserID' => 12 
    ]) 
]) ;
$result = curl_exec($my_curl);
curl_close($my_curl);

echo "<pre>" ;
print_r(json_decode($result,true));
echo "</pre>" ; 
// örnek  2 END 


?>