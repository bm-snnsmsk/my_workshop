<?php
namespace bm_snnsmsk ;

class File{

    private $path ;
    private $freeDiscSpace ;
    private $totalDiscSpace ;

    public function __construct($path){
       $this->path = $path ;
       $this->freeDiscSpace = disk_free_space('C:') ;
       $this->totalDiscSpace = disk_total_space('C:') ;
    } 
    public function getFreeDiscSpace(){
        return $this->freeDiscSpace ;
    }
    public function getTotalDiscSpace(){
        return $this->totalDiscSpace ;
    }
    public function deleteFile(){ //dosya siler
        if(!file_exists($this->path)){
            return ;
        }else{
            return unlink($this->path) ;
        }
    }
    public function copyFile($fromPath, $toPath){
        return copy($fromPath, $toPath) ;
    }
    public function renameFile($oldPathName, $newPathName){
        return rename($oldPathName, $newPathName) ;
    }
    public function makeDIR($chmode = 0644){ // klasor oluşturur
        if(file_exists($this->path)){
            return ;
        }else{
            return mkdir($this->path, $chmode) ;
        }
    }
    public function removeDIR(){ // klasor siler
        if(!file_exists($this->path)){
            return ;
        }else{
            return rmdir($this->path) ;
        }
    }
    public function readFile(){
        if(file_exists($this->path)){
            $file = fopen($this->path, 'r') ;
            $content = "" ;
            while(!feof($file)){
                $content .= fgets($file).'<br/>' ;
            }
            return $content ;    
            fflush($file) ;        
            fclose($file) ;
        }else{
            return 0 ;
        }
    }
    public function writeFile($content){
        $file = fopen($this->path, 'w') ;
        fwrite($file, $content) ;    
        fflush($file) ;       
        fclose($file) ;
    }
    public function addFile($content){
        $content .= PHP_EOL ;
        $file = fopen($this->path, 'a') ;
        fwrite($file, $content) ;    
        fflush($file) ;       
        fclose($file) ;
    }
    public function readCSVFile(){
        if(file_exists($this->path)){
            $file = fopen($this->path, 'r') ;
            $content = "" ;
            while(!feof($file)){
                $content .= iconv("LATIN5","UTF-8",fgetcsv($file)[0]).'<br/>' ;
            }
            return $content ; 
            fflush($file) ;           
            fclose($file) ;
        }else{
            return 0 ;
        }
    }
    public function addCSVFile($arrContent){
        if(file_exists($this->path)){
            $file = fopen($this->path, 'a') ;
            $content = "" ;
            foreach($arrContent as $value){
                fputcsv($file, iconv('UTF-8', 'LATIN5', $value), ';') ;
            }
            return $content ;   
            fflush($file) ;     
            fclose($file) ;
        }else{
            return 0 ;
        }
    }
    public function downloadFile($filePath, $fileName){
        if(file_exists($filePath)){
            header("Content-Description: File Transfer") ;
            header("Content-Type: application/octet-stream") ;
            header("Content-Disposition: attachment; filename=".uniqid()."_".$fileName) ;
            header("Content-Transfer-Encoding:binary") ;
            header("Expires:0") ;
            header("Cache-Control: must-revalidate, post-check=0, pre-check=0") ;
            header("Pragma: public") ;
            header("Content-Length:".filesize($filePath)) ;
            ob_clean() ;
            flush() ;
            readfile($filePath) ;
            return ['process'=>true, 'type'=>'success', 'message'=>'Dosya başarılı bir şekilde indirildi.'] ;
        }else{
            return ['process'=>false, 'type'=>'success', 'message'=>'Dosya indirme esnasında bir hata meydana geldi.'] ;
        }
    }
    

    public function __destruct(){
        clearstatcache() ;
    } 
}
?>