<?php include 'header.php' ; ?>


<div class="container">
    <div class="card">
        <div class="card-header">
            <h5 class="card-title">Sipariş Ekle</h5>
        </div>
        <div class="card-body">
            <form action="islemler/islem.php" method="post">
                <div class="form-row">
                    <div class="col-md-6">
                        <label for="">isim soyisim</label>
                        <input class="form-control" type="text" name="musteri_isim" placeholder="isim soyisim girin">
                    </div>
                    <div class="col-md-6">
                        <label for="">mail adresi</label>
                        <input class="form-control" type="text" name="musteri_mail" placeholder="mail adresini girin">
                    </div>
                </div>    
                <div class="form-row">
                    <div class="col-md-6">
                        <label for="">telefon </label>
                        <input class="form-control" type="text" name="musteri_tel" placeholder="telefon numarası girin">
                    </div>
                    <div class="col-md-6">
                        <label for="">sipariş başlık</label>
                        <input class="form-control" type="text" name="sip_baslik" placeholder="sipariş için başlık">
                    </div>
                </div>
                <div class="form-row">
                    <div class="col-md-6">
                        <label for="">ücret </label>
                        <input class="form-control" type="number" name="ucret">
                    </div>
                    <div class="col-md-6">
                        <label for="">teslim tarihi</label>
                        <input class="form-control" type="date" name="teslim_tarihi">
                    </div>
                </div>
                <button name="siparisekle" type="submit" class="btn btn-primary btn-user mt-2 ">Sipariş Ekle</button>

            </form>
        </div>
    </div>
</div>


<?php include 'footer.php' ; ?>