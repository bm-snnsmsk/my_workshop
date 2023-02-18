<?php include 'header.php' ; ?>

<div class="container">
    <div class="card">
        <div class="card-header">
            <h3>Proje Ekle</h3>
        </div>
        <div class="card-body">
            <form action="islemler/islem.php" method="POST">

                <div class="form-row mt-2">
                    <div class="col-md-6">
                        <label for="">proje başlığı</label>
                        <input class="form-control" type="text" placholder="proje başlığı" name="proje_baslik">
                    </div>
                    <div class="col-md-6">
                        <label for="">proje teslim tarihi</label>
                        <input class="form-control" type="date" placholder="proje teslim tarihi" name="proje_teslim_tarihi">
                    </div>
                </div>

                <div class="form-row mt-2">
                    <div class="col-md-6">
                        <label for="">proje aciliyeti</label>
                        <select name="proje_aciliyeti" id="" class="form-control">
                            <option value="acil">Acil</option>
                            <option value="acil_degil">Acelesi yok</option>
                            <option value="normal">normal</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                    <label for="">proje durumu</label>
                        <select name="proje_durum" id="" class="form-control">
                            <option value="yeni">yeni başladı</option>
                            <option value="devam">devam ediyor</option>
                            <option value="bitti">bitti</option>
                        </select>
                    </div>
                </div>

                <div class="form-row mt-2">
                   <div class="col-md-6">
                    <label for="">proje detay</label>
                    <textarea name="proje_detay" id="" class="form-control" cols="20" rows="5"></textarea>
                   </div>
                </div>

                <button name="projeekle" type="submit" class="btn btn-primary btn-user mt-2 ">Kaydet</button>

            </form>
        </div>
    </div>
</div>



<?php include 'footer.php' ; ?>