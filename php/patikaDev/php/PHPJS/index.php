<!DOCTYPE html>
<html lang="tr-TR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP ve JS</title>
</head>
<body>
    <h1><?= "PHP ve JS" ; ?></h1>
    <script>alert("<?= 'burası php ile yazılmıştır' ; ?>") ; </script>


  <div id="app">
    <input type="text" v-model="group_name"><br>
    <button type="button" @click.prevent.stop="ekle">Ekle</button>
    <div>
        <ul>
            <li v-for="eklenen in eklenenler" :key="eklenen.id">{{eklenen.name}}</li>
        </ul>
    </div>
  </div>








    <script src="https://cdn.jsdelivr.net/npm/vue@2.7.8/dist/vue.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.27.2/axios.min.js" integrity="sha512-odNmoc1XJy5x1TMVMdC7EMs3IVdItLPlCeL5vSUPN2llYKMJ2eByTTAIiiuqLg+GdNr9hF6z81p27DArRFKT7A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="app.js"></script>
</body>
</html>