<?php

require_once "MyClasses/Starter.php" ;
$DB = new bm_snnsmsk\Database() ;

$process = $_GET['page'] ;
$path = "upload" ;
switch($process){
    case 'insertMember' : //sleep(3) ;


        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            $name = $_POST['ad'] ;
            $lastname = $_POST['lastname'] ;


          
            
            $file = new bm_snnsmsk\FileUpload('myfile', $path) ;
            $filename = $file->getFileName() ;  
            $file->fileLoad() ;


            $process = $DB->addRow('INSERT INTO yeni(userProfile, yeniname, yenilastname) VALUES
            (?, ?, ?)', [$filename, $name, $lastname]) ;

           

            if($process > 0){
                $message = "kayıt eklendi:::success" ;
            }else{
                $message = "kayıt eklemede bir hata meydana geldi:::warning" ;
            }
        }else{
            $message = "hatalı giriş:::danger" ;
        }
        echo $message ;
       /*  return ['process' => true, 'message' => "başarılı", 'type'=>'success'] ; */
        break ;

    case 'deleteMember' :  
        
        $ID = $_GET['ID'] ;           
        $process = $DB->deleteRow('DELETE FROM yeni WHERE yeniID = ? ', [$ID]) ;
        if($process){
            
            $message = "kayıt silindi:::success" ;
        }else{
            $message = "kayıt silmede bir hata meydana geldi:::warning" ;
        }
        echo $message ;
       /*  return ['process' => true, 'message' => "başarılı", 'type'=>'success'] ; */
        break ;    
    case 'getTowns' :  
    
        $ID = $_POST['myID'] ;  
        $myOption = '<option value="0">İlçe seçiniz : </option>'  ;  
        $cities = $DB->getRows("SELECT * FROM town WHERE cityID = ?", [$ID]) ;
        foreach($cities as $items){
            $myOption .= '<option value="'.$items['townID'].'">'.$items['townName'].'</option>'  ; 
        }
        echo $myOption ;
        break ; 

    case 'fillForm' :             


            if($_SERVER['REQUEST_METHOD'] == 'POST'){
                $name = $_POST['ad'] ;
                $lastname = $_POST['lastname'] ;
    
    
              
                $message = "" ;
    
                $process = $DB->addRow('INSERT INTO yeni(yeniname, yenilastname) VALUES
                (?, ?)', [$name, $lastname]) ;
    
               
    
                if($process > 0){
                    
$datas = $DB->getRows("SELECT * FROM yeni ORDER BY yeniID DESC") ;
$counter = 0 ;
foreach($datas as $item){
 $message .= '
 <tr  id="'.$item["yeniID"].'">
 <th scope="row">'.++$counter.'</th>
 <td> <img src="upload/'.$item["userProfile"].'" width="40" height="40" alt="user.png"> </td>
 <td>'.$item["yeniName"].'</td>
 <td>'.$item["yeniLastname"].'</td>
 <td><a href="javascript:void(0)" onclick="editMember("editMember","'.$item["yeniID"].'") class="text-warning"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
<path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
</svg> </a> </td>
 <td> <a href="javascript:void(0)" onclick="removeMember(\'deleteMember\','.$item['yeniID'].')" class="text-danger"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
<path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
</svg> </a> </td>
</tr>' ;
}



                    $message .= ":::kayıt eklendi:::success" ;
                }else{
                    $message .= ":::kayıt eklemede bir hata meydana geldi:::warning" ;
                }
            }else{
                $message .= ":::hatalı giriş:::danger" ;
            }
            echo $message ;
           /*  return ['process' => true, 'message' => "başarılı", 'type'=>'success'] ; */
            break ;
}



?>