<?php 
include 'header.php' ; 
?>


<div class="container-fluid">
    <div class="card">
        <div class="card-header">
            <h1 class="text-primary font-weight-bold">Ayarlar</h1>
        </div>
        <div class="card-body">
            <form action="islemler/islem.php" method="POST">
                <div class="form-row">
                   <div class="col-md-6">
                   <input type="text" name="baslik" class="form-control" placeholder="site başlığı" value="<?php  echo $ayarcek['site_baslik'] ;  ?>">
                   </div>
                </div>
                <div class="form-row">
                    <div class="col-md-6">
                    <input type="text" name="aciklama" placeholder="site açıklaması" class="form-control" value="<?php  echo $ayarcek['site_aciklama'] ;  ?>">
                    </div>
                </div>
                <div class="form-row">
                   <div class="col-md-6">
                   <input type="text" name="sahibi" placeholder="site sahibi" class="form-control" value="<?php  echo $ayarcek['site_sahibi'] ;  ?>">
                   </div>
                </div>
                <button type="submit" name="btnkaydet" class="btn btn-primary mt-2">Kaydet</button>
            </form>
        </div>
    </div>
</div>



<?php include 'footer.php' ; ?>