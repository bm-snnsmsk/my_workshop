<?php 
include 'header.php' ; 
if(isset($_POST['proje_id'])){
    $projesor = $DBConnect->prepare('SELECT * FROM proje WHERE id = ? ') ;
    $projesor->execute([
        $_POST['proje_id']
    ]) ;
    $projecek = $projesor->fetch(PDO::FETCH_ASSOC) ;
}
?>

<div class="container">
    <div class="card">
        <div class="card-header">
            <h3>Proje Düzenle</h3>
        </div>
        <div class="card-body">
            <form action="islemler/islem.php" method="POST">
            <input class="form-control" type="hidden" value="<?= $_POST['proje_id'] ; ?>" name="projeID">
                <div class="form-row mt-2">
                    <div class="col-md-6">
                        <label for="">proje başlığı</label>
                        <input class="form-control" type="text" value="<?= $projecek['proje_baslik'] ; ?>" name="proje_baslik">
                    </div>
                    <div class="col-md-6">
                        <label for="">proje teslim tarihi</label>
                        <input class="form-control" type="date" value="<?= $projecek['proje_teslim'] ; ?>" name="proje_teslim_tarihi">
                    </div>
                </div>

                <div class="form-row mt-2">
                    <div class="col-md-6">
                        <label for="">proje aciliyeti</label>
                        <select name="proje_aciliyeti" id="" class="form-control">
                            <option value="acil" <?= ($projecek['proje_aciliyet'] == "acil") ? 'selected' : '' ; ?>>Acil</option>
                            <option value="acil_degil" <?= ($projecek['proje_aciliyet'] == "acil_degil") ? 'selected' : '' ; ?>>Acelesi yok</option>
                            <option value="normal" <?= ($projecek['proje_aciliyet'] == "normal") ? 'selected' : '' ; ?>>normal</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                    <label for="">proje durumu</label>
                        <select name="proje_durum" id="" class="form-control">
                            <option value="yeni" <?= ($projecek['proje_durum'] == "yeni") ? 'selected' : '' ; ?>>yeni başladı</option>
                            <option value="devam" <?= ($projecek['proje_durum'] == "devam") ? 'selected' : '' ; ?>>devam ediyor</option>
                            <option value="bitti" <?= ($projecek['proje_durum'] == "bitti") ? 'selected' : '' ; ?>>bitti</option>
                        </select>
                    </div>
                </div>

                <div class="form-row mt-2">
                   <div class="col-md-6">
                    <label for="">proje detay</label>
                    <textarea name="proje_detay" id="" class="form-control" cols="20" rows="5"><?= $projecek['proje_detay'] ; ?></textarea>
                   </div>
                </div>

                <button name="projeduzenle" type="submit" class="btn btn-primary btn-user mt-2 ">Düzenle</button>

            </form>
        </div>
    </div>
</div>



<?php include 'footer.php' ; ?>