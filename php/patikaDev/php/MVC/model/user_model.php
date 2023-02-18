<?php

class UserModel{
    public $dbConnect ;
    public $host = 'localhost' ;
    public $dbname = "test" ;
    public $userName = "root" ;
    public $pass = "";
    public $characterSet = "utf8" ;

    public function __construct()
    {  
        try{
            $this->dbConnect = new PDO("mysql:host=".$this->host.";dbname=".$this->dbname.";charset=".$this->characterSet, $this->userName, $this->pass) ;
            $this->dbConnect->query("SET @@lc_time_names = 'tr_TR'") ;
            $this->dbConnect->query("SET CHARACTER SET utf8") ;
            $this->dbConnect->query("SET CHARACTER_SET_CONNECTION=utf8") ;
            $this->dbConnect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION) ;
            if($this->dbConnect){
                echo "" ;
            }else{
                echo "bağlantı hatalı" ;
            }
        }catch(PDOException $e){
            echo $e->getMessage() ;
        }
    }

    public function list(){
        $sorgu = $this->dbConnect->query("SELECT * FROM pdo") ;
        return $sorgu->fetchAll(PDO::FETCH_ASSOC) ;
    }
}

?>