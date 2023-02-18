<?php
namespace bm_snnsmsk ; // en başa yazılması gerekiyor





include("static/header.php") ;
require_once "MyClasses/Starter.php" ;
$DB = new Database() ;
$datas = $DB->getRows("SELECT * FROM yeni ORDER BY yeniID DESC") ;
$cities = $DB->getRows("SELECT * FROM cities") ;
// echo md5(uniqid(time())) ;
// die();
?>    
<!-- body START  -->

<div class="body_content">


<div class="container-fluid">
    <div class="card">
        <div class="card-header">
            <h2>Ajax </h2>
        </div>
       <div class="card-body"> 

       <form id="formID" enctype="multipart/form-data">

  <div class="mb-3 row">
        <div class="col-sm-2">
            <label for="ad" class="form-label">isim</label>
        </div>
        <div class="col-sm-10">
            <input type="text" class="form-control" id="ad" name="ad">
        </div> 
  </div>

  <div class="mb-3 row">
        <div class="col-sm-2">
            <label for="lastname" class="form-label">Soyisim</label>
        </div>
        <div class="col-sm-10">
            <input type="text" class="form-control" id="lastname" name="lastname">
        </div> 
  </div>
  

  <div class="mb-3 row">
        <div class="col-sm-2">
            <label for="lastname" class="form-label">İl</label>
        </div>
        <div class="col-sm-10">
        <select class="form-select form-select-sm mb-3" aria-label=".form-select-lg example" id="cityName" name="cityName">
                <option value="0">İlinizi seçiniz : </option>
                
                <?php 
               
                foreach($cities as $c){
                ?>
                    <option value="<?= $c['cityID'] ; ?>"> <?= $c['cityName'] ; ?> </option>
                <?php
                }
                ?>
                </select>

<select class="form-select form-select-sm mb-3" aria-label=".form-select-lg example" id="townName" name="townName">
<option value="0">İlçe seçiniz : </option>
                
                
</select>


        </div> 
  </div>

  <div class="mb-3 row">
        <div class="col-sm-2">
        <label for="myfile" class="form-label"> Profile resmi seçiniz </label>
        </div>
        <div class="col-sm-10">
        <input class="form-control" type="file" id="myfile" name="myfile">
        </div> 
  </div>



  

  <div class="row">
        <div class="col-sm-10 offset-sm-2">
            <p id="result"> </p>
        </div> 
  </div>

  <div class="mb-3 row">
        <div class="col-sm-10 offset-sm-2">
        <!-- <button type="submit" class="btn btn-primary" id="mysubmit" onclick="sendForm('frmAddMember','insertMember','admin.php')">Kaydet <span class="myload"></span> -->
        <button type="submit" class="btn btn-primary" id="mysubmit">Kaydet <span class="myload"></span>
        </button>
        </div> 
  </div>

 
</form>
       </div>
    </div>
</div>

<div class="container mt-3">
    <div class="row">
    <table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Profile</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Düzenle</th>
      <th scope="col">Sil</th>
    </tr>
  </thead>
  <tbody>

  <?php  
  $counter = 0 ;
  foreach($datas as $item){
?>
    <tr  id='<?= $item['yeniID'] ; ?>'>
      <th scope="row"> <?= ++$counter ;  ?> </th>
      <td> <img src="upload/<?= $item['userProfile'] ;  ?>" width="40" height="40" alt="user.png"> </td>
      <td> <?= $item['yeniName'] ;  ?> </td>
      <td> <?= $item['yeniLastname'] ; ?> </td>
      <td> <a href="javascript:void(0)" onclick="editMember('editMember','<?= $item['yeniID'] ; ?>')" class="text-warning"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
  <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
  <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
</svg> </a> </td>
      <td> <a href="javascript:void(0)" onclick="removeMember('deleteMember','<?= $item['yeniID'] ; ?>')" class="text-danger"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
  <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
  <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
</svg> </a> </td>
    </tr>
    <?php 
  }
  ?>
  </tbody>
</table>
    </div>
</div>
</div>


 

<script src="js/jquery-3.6.1.min.js"></script>
<script>
let SITE_URL = "http://localhost/apps/PHP/" ;
// ekleme
function sendForm(formID, process, redirect=""){
    $(".myload").html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>') ;
    $('#mysubmit').prop('disabled', true) ;
    let myData = $('form#'+formID).serialize() ;
    /* let name = document.querySelector('#ad') ;
    let lastname = document.querySelector('#lastname') ; */
    $.ajax({
        type:'post',
        url: SITE_URL+"ajax.php?page="+process,
        data:myData,
        success:function(resultData){          
            $(".myload").html('') ;
            $('#mysubmit').prop('disabled', false) ;
            resultData = resultData.split(':::',2) ;
            let message = resultData[0] ; 
            let mistake = resultData[1] ;
            if(mistake == 'warning'){
               //alert("warning") ;
                $('#result').html('<div class="alert alert-warning" role="alert">'+message+'</div>') ;
            }else if(mistake == 'danger'){
                //alert("danger") ;
                $('#result').html('<div class="alert alert-danger" role="alert">'+message+'</div>') ;
            }else if(mistake == 'success'){
               //alert("success ") ;
                $('form').trigger('reset') ; // form boşaltılıyor
                $('#result').html('<div class="alert alert-success" role="alert">'+message+'</div>') ;
                setTimeout(function(){
                    window.location.href=SITE_URL+redirect ;
                    // $('#ad').focus() ; çalışmıyor 
                }, 1500) ;
            }else{
               alert("en son else bloğu" + resultData) ;
            }
        }
    }) ;
}
// delete 
function removeMember(process, deleteID){   
    if(confirm("Silmek istediğinize emin misiniz ?")){
        $.get(SITE_URL+"ajax.php?page="+process, {'ID':deleteID}, function(resultData){
            resultData = resultData.split(':::',2) ;
            let message = resultData[0] ; 
            let mistake = resultData[1] ;
            alert(message) ;
            if(mistake == 'success'){
                $('#'+deleteID).remove() ;
            }
        }) ;
    }
}
function editMember(process, editID){ 
    $.get(SITE_URL+"ajax.php?page="+process, {'ID':deleteID}, function(resultData){
        resultData = resultData.split(':::',2) ;
        let message = resultData[0] ; 
        let mistake = resultData[1] ;
        alert(message) ;
        if(mistake == 'success'){
                $('#'+deleteID).remove() ;
        }
    }) ;
}

$(function(){
    // il ilçe START
    $('#cityName').change(function(){         
        let myValue = $(this).val() ;
        //alert(myValue) ; 
        $.ajax({
            type:'post',
            url: SITE_URL+"ajax.php?page=getTowns",
            data:{'myID':myValue},
            dataType :'text',
            success:function(resultData){   
                //alert("test") ;       
                $("#townName").html(resultData) ;
            }
        });       
    }) ;
    // il ilçe END

   $('#formID').on('submit', function(e){
    e.preventDefault() ; // sayfa yenilenmesine gerek yok
    $(".myload").html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>') ;
    $('#mysubmit').prop('disabled', true) ;
    $.ajax({
        type:'post',
        url: SITE_URL+"ajax.php?page=insertMember",
        data:new FormData(this), // formun tüm bilgileri input + file upload ...
        contentType :false,
        processData:false,
        cashe:false,
        success:function(resultData){          
            $(".myload").html('') ;
            $('#mysubmit').prop('disabled', false) ;
            resultData = resultData.split(':::',2) ;
            let message = resultData[0] ; 
            let mistake = resultData[1] ;
            if(mistake == 'warning'){
               //alert("warning") ;
                $('#result').html('<div class="alert alert-warning" role="alert">'+message+'</div>') ;
            }else if(mistake == 'danger'){
               // alert("danger") ;
                $('#result').html('<div class="alert alert-danger" role="alert">'+message+'</div>') ;
            }else if(mistake == 'success'){
               // alert("success ") ;
                $('form').trigger('reset') ; // form boşaltılıyor
                $('#result').html('<div class="alert alert-success" role="alert">'+message+'</div>') ;
                setTimeout(function(){
                    window.location.href=SITE_URL+'admin.php' ;
                  // $('#ad').focus() ; çalışmıyor 
                }, 1500) ;
            }else{
               alert("en son else bloğu" + resultData) ;
            }
        }
    }) ;
   }) ;    
}) ;



</script>
<!-- body END  -->
<!-- footer START -->

<?php
include("static/footer.php") ;
?>