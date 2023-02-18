<?php 
include 'header.php' ; 
if(isset($_POST['siparis_id'])){
    $siparisler = $DBConnect->prepare('SELECT * FROM siparis WHERE id= ?') ;
    $siparisler->execute([$_POST['siparis_id']]) ;
    $sipariscek = $siparisler->fetch(PDO::FETCH_ASSOC) ;
}else{
    header('location:index.php ') ;
}
?>


<div class="container">
    <div class="card">
        <div class="card-header">
            <h5 class="card-title">Sipariş Düzenle</h5>
        </div>
        <div class="card-body">
            <form action="islemler/islem.php" method="post">
                <div class="form-row">
                    <div class="col-md-6">
                        <label for="">isim soyisim</label>
                        <input class="form-control" type="text" name="musteri_isim" value="<?= $sipariscek['sip_name'] ?>">
                    </div>
                    <div class="col-md-6">
                        <label for="">mail adresi</label>
                        <input class="form-control" type="text" name="musteri_mail" value="<?= $sipariscek['sip_mail'] ?>">
                    </div>
                </div>    
                <div class="form-row">
                    <div class="col-md-6">
                        <label for="">telefon </label>
                        <input class="form-control" type="text" name="musteri_tel" value="<?= $sipariscek['sip_tel'] ?>">
                    </div>
                    <div class="col-md-6">
                        <label for="">sipariş başlık</label>
                        <input class="form-control" type="text" name="sip_baslik" value="<?= $sipariscek['sip_baslik'] ?>">
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-md-6">
                        <label for="">ücret </label>
                        <input class="form-control" type="number" value="<?= $sipariscek['sip_ucret'] ?>" name="ucret">
                    </div>
                    <div class="col-md-6">
                        <label for="">teslim tarihi</label>
                        <input class="form-control" value="<?= $sipariscek['sip_teslim_tarihi'] ?>" type="date" name="teslim_tarihi">
                    </div>
                </div>
                <button name="siparisduzenle" type="submit" class="btn btn-primary btn-user mt-2 ">Sipariş Düzenle</button>

            </form>
        </div>
    </div>
</div>


<?php include 'footer.php' ; ?>