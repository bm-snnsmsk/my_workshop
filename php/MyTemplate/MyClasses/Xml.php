<?php
namespace bm_snnsmsk ;

class Xml{
    
    public function __construct(){
        libxml_use_internal_errors(true) ;
    }
    public function getXml($xml){        
        return simplexml_load_string($xml) ;
    }
    public function getXmls($xml){        
        $data = simplexml_load_string($xml) ;
        if($data === false){
            echo "Hatalar : <br/>" ;
            foreach(libxml_get_errors() as $error){
                echo $error->message."<br/>" ;
            }
        }else{
            foreach($data as $key => $value){
                echo $key." : ".$value."<br/>" ;
            }
        }
    }
    public function getXmlFile($xmlPath){        
        $data = simplexml_load_file($xmlPath) ;
        if($data === false){
            echo "Hatalar : <br/>" ;
            foreach(libxml_get_errors() as $error){
                echo $error->message."<br/>" ;
            }
        }else{
            foreach($data as $key => $value){
                echo $key." : ".$value."<br/>" ;
            }
        }
    }
    public function getXmlFileWithDetail($xmlPath){        
        $data = simplexml_load_file($xmlPath) ;
        if($data === false){
            echo "Hatalar : <br/>" ;
            foreach(libxml_get_errors() as $error){
                echo $error->message."<br/>" ;
            }
        }else{
            foreach($data->children() as $key => $value){
                echo $value[0]["category"]." - ".$value->title[0]['lang']." - ".$value->author." - ".$value->year." - ".$value->price."<br/>" ;
            }
        }
    }
    public function getXmlFileWithDetail2($xmlPath){        
        $data = new \DOMDocument() ;
        $data->load($xmlPath) ;
        if($data === false){
            echo "Hatalar : <br/>" ;
            foreach(libxml_get_errors() as $error){
                echo $error->message."<br/>" ;
            }
        }else{
            foreach($data->documentElement->childNodes as $key => $value){
                echo $value->nodeName." - ".$value->nodeValue."<br/>" ;
            }
        }
    }
}
?>

