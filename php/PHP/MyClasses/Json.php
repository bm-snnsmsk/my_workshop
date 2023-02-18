<?php
namespace bm_snnsmsk ;

class Json{
    
    public function __construct(){
        
    }

    public function arrayToJson($arr){        
        return json_encode($arr) ;
    }
    public function jsonToObject($json, $isArr = false){
        if(is_file($json)){
            return json_decode(file_get_contents($json), $isArr) ;
        }else{
            return json_decode($json, $isArr) ; 
        }
    }
    public function printJson($json, $isArr = false){ // object
        $data = json_decode(file_get_contents($json), true) ; // array
        function readJSON($text){
            foreach($text as $key => $value){                
                if(!is_array($value)){
                    echo $key." : ".$value."<br/>";
                }else{
                    readJSON($value) ; 
                }
            }     
        }   
        readJSON($data) ;           
    }
}
?>

