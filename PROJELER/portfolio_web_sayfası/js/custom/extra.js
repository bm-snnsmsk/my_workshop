/* navbar START */ 
// html'in DOM içeriği yüklendiğinde
window.addEventListener('DOMContentLoaded',(e) => { 
    // alert("test edildi");


    let navbarMobile = function(){

        //dinamik olarak değişen arkaplan resim yüksekliğine göre değişim istendiği zaman
        // burda da fonksiyon içinde de yazılabilir        
        let el = document.querySelector('.backImage') ;
        let h = parseInt(getComputedStyle(el).getPropertyValue('height')) ;
        //  let h = document.querySelector('.backImage').offsetHeight ;

        const nCollapsible = document.body.querySelector('#mainNavbar') ;
        if(!nCollapsible){
            return ;
        }
        if(window.scrollY === 0){ // window.scrollY < h => dinamik olarak img yüksekliğine göre aksiyon istendiğinde
            nCollapsible.classList.remove("navbar-mobile") ;
           // console.log(h);
        }else{
            nCollapsible.classList.add("navbar-mobile") ;
            //console.log(h);
        }
    }
    navbarMobile() ;
    document.addEventListener("scroll",navbarMobile) ;// scroll olayı varsa
    // navbar ikonlarının seçili olmasını, renkli(atadığımız renk) görünmesini sağlar
    const myNavbar = document.body.querySelector("#mainNavbar") ;
    if(myNavbar){
        new bootstrap.ScrollSpy(document.body,{
            target:"#mainNavbar",
            offset:74
        }) ;
    }
}) ;
let btnCanvas = document.querySelectorAll('.btn-close-canvas') ;
for(let i = 0 ; i < btnCanvas.length ; i++){
    btnCanvas[i].addEventListener('click', () => {
        document.querySelector('[data-bs-dismiss="offcanvas"]').click() ; // data-bs-dismiss="offcanvas" bu özelliğe sahip elementi zorla tıkla
    }) ;
}

/* navbar END */ 

/*  contactForm START  */
(function(){
    'use strict'
    let ch = document.querySelector('#current-character') ;
    let name =  document.querySelector('#name') ;
    let email =  document.querySelector('#email') ;
    let phone =  document.querySelector('#phone') ;
    let message =  document.querySelector('#message') ;
    let btnContact =  document.querySelector('#btnContact') ;

    if(message.value.length == 0 ){
        btnContact.disabled = true ;
    }
 
    const spacePattern = /^\S*$/ ;
    const noNumericPattern = /^([^0-9]*)$/ ;
    const emailPattern = /^([a-zA-Z0-9_\-?\.?]){3,}@([a-zA-Z]){3,}\.([a-zA-Z]){2,5}$/ ;
    const onlyNumberPattern = /^[0-9]*$/ ;
    const phonePattern = /^[0-9]{10,10}$/ ;

    name.addEventListener("keyup",controlName) ;
    email.addEventListener("blur",controlEmail) ;
    phone.addEventListener("blur",controlPhone) ;
    message.addEventListener("blur",controlMessage) ;

    function controlName(){
        let errName =  document.querySelector('#errName') ;
        if(name.value.length == 0){
            name.classList.remove("is-valid") ;
            name.classList.add('is-invalid') ;
            errName.innerHTML = "İsim Alanı boş bırakılamaz !" ;
            return false ;
        }else if(name.value.length < 3){
            name.classList.remove("is-valid") ;
            name.classList.add('is-invalid') ;
            errName.innerHTML = "İsim 3 karakterden az olamaz !" ;
            return false ;
        }else if(name.value.length > 30){
            name.classList.remove("is-valid") ;
            name.classList.add('is-invalid') ;
            errName.innerHTML = "İsim 30 karakterden fazla olamaz !" ;
            return false ;
        }else if(!spacePattern.test(name.value)){
            name.classList.remove("is-valid") ;
            name.classList.add('is-invalid') ;
            errName.innerHTML = "İsimde boşluk olamaz !" ;
            return false ;
        }else if(!noNumericPattern.test(name.value)){
            name.classList.remove("is-valid") ;
            name.classList.add('is-invalid') ;
            errName.innerHTML = "İsimde rakam olamaz !" ;
            return false ;
        }else{
            name.classList.remove("is-invalid") ;
            name.classList.add('is-valid') ;
            return true ;
        }
    }
    function controlEmail(){
        let errEmail =  document.querySelector('#errEmail') ;
        if(email.value.length == 0){
            email.classList.remove("is-valid") ;
            email.classList.add('is-invalid') ;
            errEmail.innerHTML = "Email Alanı boş bırakılamaz !" ;
            return false ;
        }else if(email.value.length < 3){
            email.classList.remove("is-valid") ;
            email.classList.add('is-invalid') ;
            errEmail.innerHTML = "Emailiniz 3 karakterden az olamaz !" ;
            return false ;
        }else if(email.value.length > 30){
            email.classList.remove("is-valid") ;
            email.classList.add('is-invalid') ;
            errEmail.innerHTML = "E-posta 30 karakterden fazla olamaz !" ;
            return false ;
        }else if(!spacePattern.test(email.value)){
            email.classList.remove("is-valid") ;
            email.classList.add('is-invalid') ;
            errEmail.innerHTML = "E-postada boşluk olamaz !" ;
            return false ;
        }else if(!emailPattern.test(email.value)){
            email.classList.remove("is-valid") ;
            email.classList.add('is-invalid') ;
            errEmail.innerHTML = "E-posta yanlış formatta olamaz !" ;
            return false ;
        }else{
            email.classList.remove("is-invalid") ;
            email.classList.add('is-valid') ;
            return true ;
        }
    }
    function controlPhone(){
        let errPhone =  document.querySelector('#errPhone') ;
        if(phone.value.length == 0){
            phone.classList.remove("is-valid") ;
            phone.classList.add('is-invalid') ;
            errPhone.innerHTML = "Telefon Alanı boş bırakılamaz !" ;
            return false ;
        }else if(!spacePattern.test(phone.value)){
            phone.classList.remove("is-valid") ;
            phone.classList.add('is-invalid') ;
            errPhone.innerHTML = "Telefon alanı boşluk içeremez!" ;
            return false ;
        }else if(!phonePattern.test(phone.value)){
            phone.classList.remove("is-valid") ;
            phone.classList.add('is-invalid') ;
            errPhone.innerHTML = "Yanlış telefon formatı!" ;
            return false ;
        }else if(!onlyNumberPattern.test(phone.value)){
            phone.classList.remove("is-valid") ;
            phone.classList.add('is-invalid') ;
            errPhone.innerHTML = "Lütfen sadece rakam giriniz" ;
            return false ;
        }else{
           // phone.value = '+90(' + (phone.value).substr(0,3) +') - '+(phone.value).substr(3,3) + ' - '+(phone.value).substr(6,4,3);
           // phone.setAttribute('readonly','true') ;
            phone.classList.remove("is-invalid") ;
            phone.classList.add('is-valid') ;
            return true ;
        }
    }
    function controlMessage(){
        let errMessage =  document.querySelector('#errMessage') ;
        if(message.value.length == 0){
            message.classList.remove("is-valid") ;
            message.classList.add('is-invalid') ;
            errMessage.innerHTML = "Mesaj Alanı boş bırakılamaz !" ;
            return false ;
        }else if(message.value.length < 10){
            message.classList.remove("is-valid") ;
            message.classList.add('is-invalid') ;
            errMessage.innerHTML = "Mesajınız 10 karakterden az olamaz" ;
            return false ;
        }else{
            message.classList.remove("is-invalid") ;
            message.classList.add('is-valid') ;
            return true ;
        }
    }
    //text-area character control
    message.addEventListener('keyup', () => {//keyup= el tuştan kaldırıldığında // input = karakter girer girmez
        ch.innerHTML = message.value.length ;
        if(message.value.length >= 10 ){
            btnContact.disabled = false ;
        }else{
            btnContact.disabled = true ;
        }
    }) ;

    let form = document.querySelector(".needs-validation") ;
    form.addEventListener("submit",(e)=>{
        if(!form.checkValidity() || !controlName() || !controlEmail() || !controlMessage() || !controlPhone()){  // hata varsa
            e.preventDefault() ; // submit etme
            e.stopPropagation(); // tüm eventleri durdur
        }else{

        }
    }, false) ;

})();
/*  contactForm END  */
















