<?php
namespace bm_snnsmsk ;

class RegExp{
    private $regExp ;
    private $text ;
    private $case ;
    
    public function __construct(){

    }    
    public function getRegExp(){
        return $this->regExp ;
    }  
    public function setRegExp($regExp){
        return $this->regExp = Security::security($regExp) ;
    }
    public function getText(){
        return $this->text ;
    }  
    public function setText($text){
        return $this->text = Security::security($text) ;
    }
    public function getCase(){
        return $this->case ;
    }  
    public function setCase($case){
        return $this->case = Security::security($case) ;
    }
    public function inRegExp($regExp, $text, $case = false){
        $case == true ? $regExp = '/'.$regExp.'/xi' : $regExp = '/'.$regExp.'/x';
        $result = preg_match($regExp, Security::security($text)) ; //preg_match($regExp, $text, $result) 3. parametre gerek yok. sonuç kullnıuldı sadece
        return $result ;
    }
    public function inRegExpAll($regExp, $text, $case = false){
        $case == true ? $regExp = '/'.$regExp.'/xi' : $regExp = '/'.$regExp.'/x';
        preg_match_all($regExp, Security::security($text), $result) ;
        return $result ;
    }
    public function onlyConsonant($text){
        $regExp = '/[^aeıioöuüAEIİOÖUÜ]/u' ;
        preg_match_all($regExp, Security::security($text), $result) ;
        $txt = "" ;
        foreach($result[0] as $key => $value){
            $txt .= $value ;
        }
        return $txt ;
    }
    public function isLetter($text){
        $regExp = "/[^a-zA-ZçğıöşüÇĞIİÖŞÜ]/u" ;
        $result = preg_match($regExp, Security::security($text)) ? false : true ;
        return $result ;
    }
    public function isNumber($text){
        $regExp = '/^[0-9]*$/' ;
        $result = preg_match($regExp, Security::security($text)) ;
        return $result ;
    }
    public function isEmail($text){
        $result = filter_var(Security::security($text), FILTER_VALIDATE_EMAIL) ;
        return $result ;
    }
    public function isIP($text){
        if(filter_var(Security::security($text), FILTER_VALIDATE_IP, FILTER_FLAG_IPV4)){
            $isIP = true ;
            $IPMessage = "Bu bir IPV4 adresidir." ;
        }else if(filter_var(Security::security($text), FILTER_VALIDATE_IP, FILTER_FLAG_IPV6)){
            $isIP = true ;
            $IPMessage = "Bu bir IPV6 adresidir." ;
        }else{
            $isIP = false ;
            $IPMessage = "Bu bir IP adresi değildir." ;
        }
        return ['isIP' => $isIP, 'IPMessage' => $IPMessage, 'IPAddress' => $text, 'IPLength' => strlen($text)] ; 
    }
    public function isUrl($text){
        $regExp = '/^\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]$/i' ;
        $isUrl = preg_match($regExp, Security::security($text)) ;
        return ['isUrl' => $isUrl, 'urlLength' => strlen($text)] ; 
    }
    public function isPhone($text){
        $regExp1 = '/^\s*\+?\s*\d{0,2}\s*\(?5\d{2}\)?\s*-?\s*\d{3}\s*-?\s*[0-9]{2}\s*-?\s*[0-9]{2}\s*$/' ; // for isPhone (mobile phone)
        $regExp2 = '/^\s*\+?\s*\d{0,2}\s*\(?\d{3}\)?\s*-?\s*\d{3}\s*-?\s*[0-9]{2}\s*-?\s*[0-9]{2}\s*$/' ; // for isPhone (home phone)
        $isMobilePhone = preg_match($regExp1, Security::security($text)) ;
        $isHomePhone = preg_match($regExp2, Security::security($text)) ;
        $regExp3 = '/[-\(\) ]/' ; // for to Phone
        $replace = "" ;
        $toPhone = preg_filter($regExp3, $replace, Security::security($text)) ;
        return ['isMobilePhone' => $isMobilePhone, 'isHomePhone' => $isHomePhone,'toPhone' => $toPhone, 'phoneLength' => strlen($toPhone)] ;
    }
    public function isBornDate($text){
        $regExp = '/^\s*[0-9]{1,2}\s*(\.|-|\/)\s*[0-9]{1,2}\s*(\.|-|\/)\s*[0-9]{4}\s*$/' ; // for isBornDate 02.05.1985 formatında
        $isBornDate = preg_match($regExp, Security::security($text)) ;
        $regExp2 = '/[ ]/' ; // for to isBornDate
        $replace = "" ;
        $toBornDate = preg_filter($regExp2, $replace, Security::security($text)) ;
        return ['isBornDate' => $isBornDate, 'toBornDate' => $toBornDate, 'bornDateLength' => strlen($toBornDate)] ;
    }
    // functions
    public function myStripTags($text){ // = strip_tags()
        $regExp = '/<\/?[^>]+>/' ; // önce < sonra 0 veya bir tane / sonra > harici herşey(bir ve daha fazla olabilir) sonra > 
        $replace = "" ;
        $result = preg_filter($regExp, $replace, $text) ;
        return $result ;
    }
}

?>
