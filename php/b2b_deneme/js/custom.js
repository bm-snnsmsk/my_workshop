let SITE_URL = "http://localhost/B2B" ;

function bayi_register(){
    document.querySelector("#bayi_register_button").disabled = true ;
    let form_data = $('#bayi_register_form').serialize() ;
    $.ajax({
        type : "POST",
        url : SITE_URL + "/inc/register.php" ,
        data : form_data ,
        success : function(resultData){
            if($.trim(resultData) == "empty"){
                alert("Lütfen boş alan bırakmayınız !") ;
                document.querySelector("#bayi_register_button").disabled = false ;
            }else if($.trim(resultData) == "format"){
                alert("e-posta formatı hatalı") ;
                document.querySelector("#bayi_register_button").disabled = false ;
            }else if($.trim(resultData) == "match"){
                alert("Şifreler uyuşmuyor") ;
                document.querySelector("#bayi_register_button").disabled = false ;
            }else if($.trim(resultData) == "already"){
                alert("Bu e-posta adına ait bir bayi zaten kayıtlı") ;
                document.querySelector("#bayi_register_button").disabled = false ;
            }else if($.trim(resultData) == "error"){
                alert("Bir hata oluştu...") ;
                document.querySelector("#bayi_register_button").disabled = false ;
            }else if($.trim(resultData) == "ok"){
                alert("Üyeliğiniz başarıyla oluştruldu. Üyeliğiniz, yönetici onayından sonra aktifleşecektir.") ;
                window.location.href = SITE_URL ;
            }
        }
    }) ;
}
function bayi_login(){
    document.querySelector("#bayi_login_button").disabled = true ;
    let form_data = $('#bayi_login_form').serialize() ;
    $.ajax({
        type : "POST",
        url : SITE_URL + "/inc/login.php" ,
        data : form_data ,
        success : function(resultData){
            if($.trim(resultData) == "empty"){
                alert("Lütfen boş alan bırakmayınız !") ;
                document.querySelector("#bayi_login_button").disabled = false ;
            }else if($.trim(resultData) == "error"){
                alert("Bayi kodu, şifre veya e-posta yanlış...") ;
                document.querySelector("#bayi_login_button").disabled = false ;
            }else if($.trim(resultData) == "pasif"){
                alert("Üyeliğiniz pasif durumundadır") ;
                document.querySelector("#bayi_login_button").disabled = false ;
            }else if($.trim(resultData) == "ok"){
                alert("Giriş başarılı") ;
                window.location.href = SITE_URL ;
            }
        }
    }) ;
}
function bayi_profile_update(){
    document.querySelector("#bayi_profile_update_button").disabled = true ;
    let form_data = $('#bayi_profile_form').serialize() ;
    $.ajax({
        type : "POST",
        url : SITE_URL + "/inc/bayi_profile_update.php" ,
        data : form_data ,
        success : function(resultData){
            if($.trim(resultData) == "empty"){
                alert("Lütfen boş alan bırakmayınız !") ;
                document.querySelector("#bayi_profile_update_button").disabled = false ;
            }else if($.trim(resultData) == "format"){
                alert("e-posta formatı hatalı") ;
                document.querySelector("#bayi_profile_update_button").disabled = false ;
            }else if($.trim(resultData) == "already"){
                alert("Bu e-posta adına ait bir bayi zaten kayıtlı") ;
                document.querySelector("#bayi_profile_update_button").disabled = false ;
            }else if($.trim(resultData) == "error"){
                alert("Bir hata oluştu...") ;
                document.querySelector("#bayi_profile_update_button").disabled = false ;
            }else if($.trim(resultData) == "ok"){
                alert("Profil bilileriniz başarıyla güncellendi") ;
                window.location.reload() ;
            }
        }
    }) ;
}
function bayi_password_update(){
    document.querySelector("#bayi_password_update_button").disabled = true ;
    let form_data = $('#bayi_password_update_form').serialize() ;
    $.ajax({
        type : "POST",
        url : SITE_URL + "/inc/bayi_change_password.php" ,
        data : form_data ,
        success : function(resultData){
            if($.trim(resultData) == "empty"){
                alert("Lütfen boş alan bırakmayınız !") ;
                document.querySelector("#bayi_password_update_button").disabled = false ;
            }else if($.trim(resultData) == "match"){
                alert("Şifreler uyuşmuyor") ;
                document.querySelector("#bayi_password_update_button").disabled = false ;
            }else if($.trim(resultData) == "error"){
                alert("Bir hata oluştu...") ;
                document.querySelector("#bayi_password_update_button").disabled = false ;
            }else if($.trim(resultData) == "ok"){
                alert("Şifreniz başarılı bir şekilde güncellendi") ;
                window.location.href = SITE_URL + "/profile.php?process=profil";
            }
        }
    }) ;
}
function bayi_address_update(){
    document.querySelector("#bayi_address_update_button").disabled = true ;
    let form_data = $('#bayi_address_update_form').serialize() ;
    $.ajax({
        type : "POST",
        url : SITE_URL + "/inc/bayi_address_update.php" ,
        data : form_data ,
        success : function(resultData){
            if($.trim(resultData) == "empty"){
                alert("Lütfen boş alan bırakmayınız !") ;
                document.querySelector("#bayi_address_update_button").disabled = false ;
            }else if($.trim(resultData) == "error"){
                alert("Bir hata oluştu...") ;
                document.querySelector("#bayi_address_update_button").disabled = false ;
            }else if($.trim(resultData) == "ok"){
                alert("Adres bilgileriniz başarılı bir şekilde güncellendi") ;
                window.location.href = SITE_URL + "/profile.php?process=profil";
            }
        }
    }) ;
}
function new_notification(){
    document.querySelector("#new_notification_button").disabled = true ;
    let form_data = $('#new_notification_form').serialize() ;
    $.ajax({
        type : "POST",
        url : SITE_URL + "/inc/new_notification.php" ,
        data : form_data ,
        success : function(resultData){
            if($.trim(resultData) == "empty"){
                alert("Lütfen boş alan bırakmayınız !") ;
                document.querySelector("#new_notification_button").disabled = false ;
            }else if($.trim(resultData) == "error"){
                alert("Bir hata oluştu...") ;
                document.querySelector("#new_notification_button").disabled = false ;
            }else if($.trim(resultData) == "ok"){
                alert("Yeni havale bildiriminiz başarılı bir şekilde eklenmiştir") ;
                window.location.href = SITE_URL + "/profile.php?process=profil";
            }
        }
    }) ;
}
function bayi_new_address(){
    document.querySelector("#bayi_new_address_button").disabled = true ;
    let form_data = $('#bayi_new_address_form').serialize() ;
    $.ajax({
        type : "POST",
        url : SITE_URL + "/inc/bayi_new_address.php" ,
        data : form_data ,
        success : function(resultData){
            if($.trim(resultData) == "empty"){
                alert("Lütfen boş alan bırakmayınız !") ;
                document.querySelector("#bayi_new_address_button").disabled = false ;
            }else if($.trim(resultData) == "error"){
                alert("Bir hata oluştu...") ;
                document.querySelector("#bayi_new_address_button").disabled = false ;
            }else if($.trim(resultData) == "ok"){
                alert("Yeni adresiniz başarılı bir şekilde eklenmiştir") ;
                window.location.href = SITE_URL + "/profile.php?process=profil";
            }
        }
    }) ;
}
function new_comment(){
    document.querySelector("#new_comment_button").disabled = true ;
    let form_data = $('#new_comment_form').serialize() ;
    $.ajax({
        type : "POST",
        url : SITE_URL + "/inc/new_comment.php" ,
        data : form_data ,
        success : function(resultData){
            if($.trim(resultData) == "empty"){
                alert("Lütfen boş alan bırakmayınız !") ;
                document.querySelector("#new_comment_button").disabled = false ;
            }else if($.trim(resultData) == "error"){
                alert("Bir hata oluştu...") ;
                document.querySelector("#new_comment_button").disabled = false ;
            }else if($.trim(resultData) == "char"){
                alert("yorumunuz en az 500 karakter olmalı...") ;
                document.querySelector("#new_comment_button").disabled = false ;
            }else if($.trim(resultData) == "ok"){
                alert("Yorumunuz başarılı bir şekilde eklenmiştir") ;
                window.location.reload();
            }
        }
    }) ;
}
function iletisim_form(){
    document.querySelector("#iletisim_form_button").disabled = true ;
    let form_data = $('#iletisim_form').serialize() ;
    $.ajax({
        type : "POST",
        url : SITE_URL + "/inc/iletisim_form.php" ,
        data : form_data ,
        success : function(resultData){
            if($.trim(resultData) == "empty"){
                alert("Lütfen boş alan bırakmayınız !") ;
                document.querySelector("#iletisim_form_button").disabled = false ;
            }else if($.trim(resultData) == "error"){
                alert("Bir hata oluştu...") ;
                document.querySelector("#iletisim_form_button").disabled = false ;
            }else if($.trim(resultData) == "char"){
                alert("mesajınız en az 500 karakter olmalı...") ;
                document.querySelector("#iletisim_form_button").disabled = false ;
            }else if($.trim(resultData) == "ok"){
                alert("mesajınız başarılı bir şekilde eklenmiştir") ;
                window.location.reload();
            }
        }
    }) ;
}