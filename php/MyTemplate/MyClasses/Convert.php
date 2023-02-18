<?php
namespace bm_snnsmsk ;

class Convert{

    
    public function __construct(){
        
    }

    public static function convertLetter($text, $case){        
        $lower = ['ç','ğ','ı','i','ö','ş','ü'] ;
        $upper = ['Ç','Ğ','I','İ','Ö','Ş','Ü'] ;
        $lengthText = mb_strlen($text, "utf-8") ;
        $firstLetter = mb_substr($text, 0, 1, 'utf-8') ;
        $otherLetters = mb_substr($text, 1, $lengthText, 'utf-8') ;
        switch($case){
            case "upper" : 
                           $replace = str_replace($lower, $upper, $text) ;
                           $result = strtoupper($replace) ; 
                           return $result ;
                           break ;
            case "lower" : 
                           $replace = str_replace($upper, $lower, $text) ;
                           $result = strtolower($replace) ;
                           return $result ;
                           break ;  
            case "firstUpper" :
                           $replaceFirst = str_replace($lower, $upper, $firstLetter) ;
                           $replaceOthers = str_replace($upper, $lower, $otherLetters) ;
                           $replaceFirst = strtoupper($replaceFirst) ;
                           $replaceOthers = strtolower($replaceOthers) ;
                           return $replaceFirst.$replaceOthers ;
                           break ;
            case "firstLower" : 
                           $replaceFirst = str_replace($upper, $lower, $firstLetter) ;
                           $replaceOthers = str_replace($lower, $upper, $otherLetters) ;
                           $replaceFirst = strtolower($replaceFirst) ;
                           $replaceOthers = strtoupper($replaceOthers) ;
                           return $replaceFirst.$replaceOthers ;
                           break ;
            case "upperWords" : 
                           $arr = explode(" ", $text) ; // boşluk esas alındı - / gibi seperatorler dikkate alınmadı
                           $txt = "" ;
                           foreach($arr as $key => $value){
                                $firstLetter = mb_substr($value, 0, 1, 'utf-8') ;
                                $otherLetters = mb_substr($value, 1, mb_strlen($value, "utf-8"), 'utf-8') ;
                                $replaceFirst = str_replace($lower, $upper, $firstLetter) ;
                                $replaceOthers = str_replace($upper, $lower, $otherLetters) ;
                                $replaceFirst = strtoupper($replaceFirst) ;
                                $replaceOthers = strtolower($replaceOthers) ;
                                $txt .=   $replaceFirst.$replaceOthers." " ;
                           }
                           return $txt ;
                           break ;   
            default      : 
                           return ; 
                           break ;                      
        }
    }
    
}
?>