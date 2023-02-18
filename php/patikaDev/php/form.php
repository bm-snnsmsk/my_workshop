<!DOCTYPE html>
<html lang="tr-TR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
</head>
<body>
<form action="index.php?islem=ekle" method="get">
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="k_adi">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" name="sifre">
  </div>

  
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1" name=diller[]>
    <label class="form-check-label" for="exampleCheck1">html</label>
  </div>

  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1" name=diller[]>
    <label class="form-check-label" for="exampleCheck1">php</label>
  </div>

  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1" name=diller[]>
    <label class="form-check-label" for="exampleCheck1">js</label>
  </div>

  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1" name=diller[]>
    <label class="form-check-label" for="exampleCheck1">css</label>
  </div>
  
  
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
</body>
</html>