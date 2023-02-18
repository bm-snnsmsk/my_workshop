<?php
namespace bm_snnsmsk ;
use \PDO ;
class Database{

    private $hostName = "localhost"; // sunucuda da  genelde localhost olur
    private $DBName = "todoapp" ;
    // private $DBName2 = "test" ;
    private $userName = "root" ;
    private $password = "" ;
    private $charset = "UTF8" ;
    private $collationCharset = "utf8_general_ci" ;
    private $DBConnect = NULL ;
    private $query = NULL ;
    
    private function DBConnect(){
        $PDO = "mysql:host=".$this->hostName.";dbname=".$this->DBName ;
        // $PDO2 = "mysql:host=".$this->hostName.";dbname=".$this->DBName2 ;
        try{           
            $this->DBConnect = new PDO($PDO, $this->userName, $this->password) ; // connect DB1
            // $this->DBConnect = new \PDO($PDO2, $this->userName, $this->password) ; // connect DB2
            $this->DBConnect->exec("SET NAMES '".$this->charset."' COLLATE '".$this->collationCharset."'") ;
            $this->DBConnect->exec("SET CHARACTER SET '".$this->charset."'") ;
            $this->DBConnect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION) ;
            $this->DBConnect->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_BOTH) ; // default = \PDO::FETCH_BOTH
            // $this->DBConnect->beginTransaction() ; // transaction olayında başlatılmalı
        }catch(PDOException $e){
            die("Veritabanı erişim hatası ".$e->getMessage()) ;
        }
    }
    public function __construct(){
        $this->DBConnect() ;
    }
    public function customQuery($query, $params = NULL){
        try{
            return $this->commonQuery($query, $params)->fetchAll() ;
        }catch(PDOException $e){
            die($e->getMessage()) ;
        }
    }
    public function createDB($DBName){
        $newDB = $this->DBConnect->query('CREATE DATABASE '.$DBName.' CHARACTER SET '.$this->charset.' COLLATE '.$this->collationCharset) ; 
        return $newDB ;
    }
    public function deleteDB($DBName){
        $deleteDB = $this->DBConnect->query('DROP DATABASE '.$DBName) ; 
        return $deleteDB ;
    }
    public function createTable($tableName, $query){
        $newTable = $this->DBConnect->query('CREATE TABLE '.$tableName.'('.$query.') ENGINE=InnoDB DEFAULT CHARACTER SET '.$this->charset.' COLLATE '.$this->collationCharset) ; 
        return $newTable ;
    }
    public function deleteTable($tableName, $DBName = NULL){
        $deleteTable = $this->DBConnect->query('DROP TABLE '.$DBName.".".$tableName) ; 
        return $deleteTable ;
    }
    public function cloneTable($cloneDB, $cloneTable, $originalDB, $originalTable){
        $clone = $this->DBConnect->query('CREATE TABLE '.$cloneDB.".".$cloneTable.' LIKE '.$originalDB.".".$originalTable) ; 
        if($clone){
            $this->DBConnect->query('INSERT INTO '.$cloneDB.".".$cloneTable.' SELECT * FROM '.$originalDB.".".$originalTable) ; 
        }
        return $clone ;
    }
    public function renameTable($tableOldName, $tableNewName, $DBName = NULL){
        $rename = $this->DBConnect->query('RENAME TABLE '.$DBName.".".$tableOldName.' TO '.$DBName.".".$tableNewName) ; 
        return $rename ;
    }
    public function moveTable($tableOldName, $tableNewName, $oldDBName, $newDBName){
        $move = $this->DBConnect->query('RENAME TABLE '.$oldDBName.".".$tableOldName.' TO '.$newDBName.".".$tableNewName) ; 
        return $move ;
    }   
    public function truncateTable($tableName, $DBName){
        $truncate = $this->DBConnect->query('TRUNCATE TABLE '.$DBName.".".$tableName) ; 
        return $truncate ;
    }                         
    public function addColumn($tableName, $columnName, $query){ // default END   // FIRST, AFTER COLUMN_NAME
        $addColumn = $this->DBConnect->query("ALTER TABLE ".$tableName." ADD ".$columnName.' '.$query) ; 
        return $addColumn ;  
    }
    public function renameColumn($tableName, $columnOldName,$columnNewName, $query = NULL){ // default mevut sıra   // FIRST, AFTER COLUMN_NAME
        $addColumn = $this->DBConnect->query("ALTER TABLE ".$tableName." CHANGE ".$columnOldName.' '.$columnNewName." ".$query) ; 
        return $addColumn ;  
    }
    public function deleteColumn($tableName, $columnName){
        $deleteColumn = $this->DBConnect->query("ALTER TABLE ".$tableName." DROP ".$columnName) ; 
        return $deleteColumn ;  
    }
    public function showTables($DB = NULL){
        $showTables = $this->DBConnect->query("SHOW TABLES FROM ".$DB) ; 
        $showTables->setFetchMode(PDO::FETCH_NUM) ;
        return $showTables ;  // array
    }
    public function showColumns($tableName, $DB = NULL){
        $showTables = $this->DBConnect->query("SHOW COLUMNS FROM {$DB}.".$tableName) ; 
        $showTables->setFetchMode(PDO::FETCH_NUM) ;
        return $showTables ;  // array
    }   
    public function transaction($query1, $query2){
        if($query1 && $query2){
             $this->DBConnect->commit() ;
             return true ;
        }else{
             $this->DBConnect->rollback() ;
             return false ;
        }    
    }
    // common function START 
    public function commonQuery($query, $params = NULL){
        if(is_null($params)){
            $this->query = $this->DBConnect->query($query) ;
        }else{
            $this->query = $this->DBConnect->prepare($query) ;
            $this->query->execute($params) ;
        }
        return $this->query ;
    }
    // common function END 
    public function getColumn($query, $params = NULL){ // $item = $DB->getColumn("SELECT todoTitle FROM todo WHERE todoID = ?", [83]) ; echo $item ;
        try{  // $item = $DB->listColumn("SELECT COUNT(todoID) FROM todo") ; echo "$item" ; // = 21 
            return $this->commonQuery($query, $params)->fetchColumn() ;
        }catch(PDOException $e){
            die($e->getMessage()) ;
        }
    }
    public function getRow($query, $params = NULL){ // getRow("SELECT * FROM tableName WHERE id = ?", [5])  // not array
        try{
            return $this->commonQuery($query, $params)->fetch() ;
        }catch(PDOException $e){
            die($e->getMessage()) ;
        }
    }
    public function getRows($query, $params = NULL){ // getRows("SELECT * FROM tableName WHERE id > ? AND id < ?", [5, 12]) // array
        try{
            return $this->commonQuery($query, $params)->fetchAll() ;
        }catch(PDOException $e){
            die($e->getMessage()) ;
        }
    }
    public function getLimitedRows($query, $param1 = 0, $param2 = NULL){ //getLimitedRows("SELECT * FROM todo LIMIT ?", 4) ;
        try{
            $this->query = $this->DBConnect->prepare($query) ;
            $this->query->bindParam(1, $param1, PDO::PARAM_INT) ;
            if(!is_null($param2)){
                $this->query->bindParam(2, $param2, PDO::PARAM_INT) ;
            }
            $this->query->execute() ;
            return $this->query->fetchAll() ;
        }catch(PDOException $e){
            die($e->getMessage()) ;
        }
    }
    public function addRow($query, $params = NULL){
        try{
            $this->commonQuery($query, $params) ;
            return $this->DBConnect->lastInsertId() ; // ekleme yapılmış mı ?
        }catch(PDOException $e){
            die($e->getMessage()) ;
        }
    }
    public function updateRow($query, $params = NULL){
        try{
            return $this->commonQuery($query, $params)->rowCount() ; // güncellenen satır sayısı
        }catch(PDOException $e){
            die($e->getMessage()) ;
        }
    }
    public function deleteRow($query, $params = NULL){
        return $this->updateRow($query, $params) ; 
    }
    public function maintenance($DB = NULL){
        $showTables = $this->DBConnect->query("SHOW TABLES FROM ".$DB) ; 
        $showTables->setFetchMode(PDO::FETCH_NUM) ;
        if($showTables){
            foreach($showTables as $items){
                $check = $this->DBConnect->query("CHECK TABLE ".$items[0]) ;
                $analyze = $this->DBConnect->query("ANALYZE TABLE ".$items[0]) ;
                $repair = $this->DBConnect->query("REPAIR TABLE ".$items[0]) ;
                $optimize = $this->DBConnect->query("OPTIMIZE TABLE ".$items[0]) ;
                if($check == true && $analyze == true && $repair == true && $optimize == true){
                    return ["process" => true, "message" => "Bakım ve Onarım işlemi başarılı bir şekilde yapılmıştır."] ;
                }else{
                    return ["process" => false, "message" => "Bakım ve Onarım işlemi sırasında bir hata meydana geldi."] ;
                }
            }            
        }
    }
    public function __destruct(){
        $this->DBConnect = NULL ;
    }
}
?>
