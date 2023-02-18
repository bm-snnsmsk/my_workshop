<?php
require(DIR.'/model/user_model.php') ;
class User
{
    public function list(){
        $user_model = new UserModel();
        $data = $user_model->list() ;
       
        require(DIR.'/view/user_list.php') ;
    }

    public function add(){
        echo "user add";
    }
}



?>