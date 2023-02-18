/*,
for(let i=1;i<7;i++){
    document.writeln("<h"+i+">JS Bu bir h"+i+" başlık örneğidir..</h"+i+">")
}

*/

const alertBtn = document.querySelector("#alertBtn");
const alertDiv = document.querySelector("#myAlert");
alertBtn.addEventListener("click",function(){
    const myAlert = new bootstrap.Alert(alertDiv);
    myAlert.close();
});
alertDiv.addEventListener("close.bs.alert", function(){
    alert("kapatıldı");
});