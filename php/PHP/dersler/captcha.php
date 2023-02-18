<!DOCTYPE html>
<html lang="tr-TR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
    <title>Document</title>
    <style>
       
    </style>
</head>
<body onload="yukle()">


<div class="container">
    <div class="row text-center mt-3">
        <div class="col-md-6 offset-3 bg-dark text-light">
            <div id="result">sdsdsd</div>
        </div>
    </div>
    <div class="row text-center">
        <div class="col-md-6 offset-3 bg-dark text-light">
            <button class="btn btn-warning" onclick="yukle()">Değiştir</button>
        </div>
    </div>
</div>


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>


 <script>
    let output = document.querySelector('#result') ;
function yukle(){
            let text = "" ;
            for(let i = 0 ; i < 6 ; i++){
                text += Math.round(Math.random()*6)+"" ;
            }
            output.innerHTML = text;
}
 </script>   
</body>
</html>