<?php
namespace bm_snnsmsk ;

class Curl{
    private $url ;
    private $curl = NULL ;
    public function __construct(){
        
    }
    
    public function getUrl($url){
        return $url ;
    }
    public function setUrl($url){
        $this->url = $url ;
    }
    public function startCurl(){
        $this->curl = curl_init() ;
        curl_setopt_array($this->curl, [
            CURLOPT_URL => $this->url,
            CURLOPT_RETURNTRANSFER => true, // datalar return edilsin mi
            CURLOPT_TIMEOUT_MS => 15000,
            CURLOPT_FOLLOWLOCATION => true  // curl edilen sayfanın takip ettiği bir sayfayı da takip etmek istenirse
            // CURLOPT_NOBODY => false,  // body istenmiyorsa
            // CURLOPT_HEADER => true,   // header isteniyorsa
            // CURLOPT_POST => true,   
            // CURLOPT_POSTFIELDS => []   // gönderilecek input değerleri
        ]) ;
        $data = curl_exec($this->curl) ;
        return $data ;
    }
    
    public function getImages(){         // img' ler için BOT
        preg_match_all('/src="(.*?)"/', self::startCurl(), $images) ; 
        $txt = "" ;
        foreach($images[1] as $items){
            $txt .= $items.' ' ;
        }
        $images = "" ;
        $img = explode(' ', $txt) ;
        foreach($img as $src){
            $ext = pathinfo($src, PATHINFO_EXTENSION) ;
            if($ext == "png" || $ext == "jpg" || $ext == "jpeg" || $ext == "gif"){ 
            $images .= '<img src="'.$src.'" width=100 height="100" />'.'<br/>' ;
            }
        }
        return $images ;
    }

    public function __destruct(){          
        curl_close($this->curl) ;
    }
}

?>