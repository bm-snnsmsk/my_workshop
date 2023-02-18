<?php
namespace bm_snnsmsk ;

class Date{

    public function __construct(){
        if(date_default_timezone_get() != 'Europe/Istanbul'){
            date_default_timezone_set('Europe/Istanbul') ;
            //setlocale(LC_ALL, "tr-TR") ;
        }
    }    
    public static function monthsToTurkish(){
        switch(date('n')){
            case 1 : return 'Ocak' ; break ;
            case 2 : return 'Şubat' ; break ;
            case 3 : return 'Mart' ; break ;
            case 4 : return 'Nisan' ; break ;
            case 5 : return 'Mayıs' ; break ;
            case 6 : return 'Haziran' ; break ;
            case 7 : return 'Temmuz' ; break ;
            case 8 : return 'Ağustos' ; break ;
            case 9 : return 'Eylül' ; break ;
            case 10 : return 'Ekim' ; break ;
            case 11 : return 'Kasım' ; break ;
            case 12 : return 'Aralık' ; break ;
            default : return false ;
        }
    }
    public static function daysToTurkish(){
        switch(date('w')){
            case 0 : return 'Pazar' ; break ;
            case 1 : return 'Pazartesi' ; break ;
            case 2 : return 'Salı' ; break ;
            case 3 : return 'Çarşamba' ; break ;
            case 4 : return 'Perşembe' ; break ;
            case 5 : return 'Cuma' ; break ;
            case 6 : return 'Cumartesi' ; break ;
            default : return false ;
        }
    }
    public static function toTimestamp($date = 'now'){
        return strtotime($date) ;
    }
    public static function timestampToDate($timestamp){
        return date('d.m.Y - H:i:s',$timestamp) ;
    }
}
?>