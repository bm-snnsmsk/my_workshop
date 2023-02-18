<?php

if(Helper::route(0) == 'home' &&  !Helper::route(1)){
    Helper::view('home/home') ;
}



?>