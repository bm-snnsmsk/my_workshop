<?php

const BASEDIR = 'C:\xampp\htdocs\MyTemplate';
const URL = 'http://localhost/MyTemplate/';
const ERR_MODE = true ; // hata ayıklama için
date_default_timezone_set('Europe/Istanbul') ;


// MyClasses için deki tüm .php'ler sayfaya require edildi
foreach(glob(BASEDIR.'/MyClasses/'.'*.php') as $file){
    require $file ;
}



?>