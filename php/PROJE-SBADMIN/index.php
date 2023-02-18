<?php 
include 'header.php' ; 

$query1 = $DBConnect->prepare('SELECT *,COUNT(id) as toplam_projeler FROM proje') ;
$query1->execute() ;
$toplam_proje = $query1->fetch(PDO::FETCH_ASSOC) ;


$query2 = $DBConnect->prepare('SELECT *,COUNT(id) as toplam_siparisler FROM siparis') ;
$query2->execute() ;
$toplam_siparis = $query2->fetch(PDO::FETCH_ASSOC) ;

?>

<div class="row ">

    <div class="col-xl-3 col-md-6 mb-4">
        <div class="card border-left-primary shadow h-100 py-2">
            <div class="card-body">
                <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                        <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                            Projeler</div>
                        <div class="h5 mb-0 font-weight-bold text-gray-800"><?= $toplam_proje['toplam_projeler'] ; ?></div>
                    </div>
                    <div class="col-auto">
                        <i class="fas fa-calendar-check fa-2x text-gray-300"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <?php 
        $query3 = $DBConnect->prepare('SELECT * FROM proje WHERE proje_durum=?') ;
        $query3->execute(['bitti']) ;
        $biten_proje = $query3->rowcount() ;
    ?>
    <div class="col-xl-3 col-md-6 mb-4">
        <div class="card border-left-primary shadow h-100 py-2">
            <div class="card-body">
                <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                        <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                           Biten projeler</div>
                        <div class="h5 mb-0 font-weight-bold text-gray-800"><?=  $biten_proje ; ?></div>
                    </div>
                    <div class="col-auto">
                        <i class="fas fa-calendar-check fa-2x text-gray-300"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <?php 
        $query4 = $DBConnect->prepare('SELECT * FROM proje WHERE proje_durum=?') ;
        $query4->execute(['devam']) ;
        $devam_proje = $query4->rowcount() ;
    ?>



    <div class="col-xl-3 col-md-6 mb-4">
        <div class="card border-left-primary shadow h-100 py-2">
            <div class="card-body">
                <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                        <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                           Devam eden Projeler</div>
                        <div class="h5 mb-0 font-weight-bold text-gray-800"><?= $devam_proje ; ?></div>
                    </div>
                    <div class="col-auto">
                        <i class="fas fa-calendar-check fa-2x text-gray-300"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <?php 
        $query5 = $DBConnect->prepare('SELECT * FROM proje WHERE proje_durum=?') ;
        $query5->execute(['yeni']) ;
        $yeni_proje = $query5->rowcount() ;
    ?>



    <div class="col-xl-3 col-md-6 mb-4">
        <div class="card border-left-primary shadow h-100 py-2">
            <div class="card-body">
                <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                        <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                           Yeni projeler</div>
                        <div class="h5 mb-0 font-weight-bold text-gray-800"><?= $yeni_proje ; ?></div>
                    </div>
                    <div class="col-auto">
                        <i class="fas fa-calendar-check fa-2x text-gray-300"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>
<div class="row ">



    <div class="col-xl-3 col-md-6 mb-4">
        <div class="card border-left-primary shadow h-100 py-2">
            <div class="card-body">
                <div class="row no-gutters align-items-center">
                    <div class="col mr-2">
                        <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                           Siparişler</div>
                        <div class="h5 mb-0 font-weight-bold text-gray-800"><?= $toplam_siparis['toplam_siparisler'] ; ?></div>
                    </div>
                    <div class="col-auto">
                        <i class="fas fa-calendar fa-2x text-gray-300"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>


<div class="container">
    <div class="card">
        <div class="card-header">
            <h5 class="card-title">Projeler</h5>
        </div>
        <div class="card-body">
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>No</th>
                        <th>Başlık</th>
                        <th>Bitiş Tarihi</th>
                        <th>Aciliyet</th>
                        <th>Durum</th>
                        <th>İşlem</th>
                    </tr>
                </thead>
                <tbody>
                    <?php 
                        $projeler = $DBConnect->prepare('SELECT * FROM proje') ;
                        $projeler->execute() ;
                        $sayac = 0 ;
                        while($projecek = $projeler->fetch(PDO::FETCH_ASSOC)){
                            echo '
                            <tr> 
                            <td>'.++$sayac.'</td> 
                            <td>'.$projecek['proje_baslik'].'</td> 
                            <td>'.$projecek['proje_teslim'].'</td> 
                            <td>'.$projecek['proje_durum'].'</td> 
                            <td>'.$projecek['proje_aciliyet'].'</td> 
                            <td> 
                                <div class="d-flex justify-content-center">

                                    <form action="projeduzenle.php" method="POST">
                                        <input type="hidden" name="proje_id" value="'.$projecek['id'].'">
                                        <button type="submit" name="duzenleme" class="btn btn-success btn-sm btn-icon-split">
                                            <span class="icon text-white-60">
                                            <i class="fas fa-edit"></i>
                                            </span>
                                        </button>
                                    </form>

                                    <form class="mx-2" action="islemler/islem.php" method="POST">
                                        <input type="hidden" name="proje_id" value="'.$projecek['id'].'">
                                        <button type="submit" name="proje_silme" class="btn btn-danger btn-sm btn-icon-split">
                                            <span class="icon text-white-60">
                                            <i class="fas fa-trash"></i>
                                            </span>
                                        </button>
                                    </form>

                                    <form action="proje.php" method="POST">
                                        <input type="hidden" name="proje_id" value="'.$projecek['id'].'">
                                        <button type="submit" name="proje_bak" class="btn btn-primary btn-sm btn-icon-split">
                                            <span class="icon text-white-60">
                                            <i class="fas fa-eye"></i>
                                            </span>
                                        </button>
                                    </form>


                                </div>
                            </td> 
                            </tr>' ;
                        }
                     ?>
                    
                </tbody>
            </table>
        </div>
    </div>
</div>


<div class="container">
    <div class="card">
        <div class="card-header">
            <h5 class="card-title">Siparişler</h5>
        </div>
        <div class="card-body">
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>No</th>
                        <th>isim</th>
                        <th>email</th>
                        <th>telefon</th>
                        <th>teslim tarihi</th>
                        <th>ücret</th>
                        <th>başlık</th>
                        <th>işlem</th>
                    </tr>
                </thead>
                <tbody>
                    <?php 
                        $siparisler = $DBConnect->prepare('SELECT * FROM siparis') ;
                        $siparisler->execute() ;
                        $sayac = 0 ;
                        while($sipariscek = $siparisler->fetch(PDO::FETCH_ASSOC)){
                            echo '
                            <tr> 
                            <td>'.++$sayac.'</td> 
                            <td>'.$sipariscek['sip_name'].'</td> 
                            <td>'.$sipariscek['sip_mail'].'</td> 
                            <td>'.$sipariscek['sip_tel'].'</td> 
                            <td>'.$sipariscek['sip_teslim_tarihi'].'</td> 
                            <td>'.$sipariscek['sip_ucret'].'</td> 
                            <td>'.$sipariscek['sip_baslik'].'</td> 
                            <td> 
                                <div class="d-flex justify-content-center">

                                    <form action="siparisduzenle.php" method="POST">
                                        <input type="hidden" name="siparis_id" value="'.$sipariscek['id'].'">
                                        <button type="submit" name="duzenleme" class="btn btn-success btn-sm btn-icon-split">
                                            <span class="icon text-white-60">
                                            <i class="fas fa-edit"></i>
                                            </span>
                                        </button>
                                    </form>

                                    <form class="mx-2" action="islemler/islem.php" method="POST">
                                        <input type="hidden" name="siparis_id" value="'.$sipariscek['id'].'">
                                        <button type="submit" name="siparis_silme" class="btn btn-danger btn-sm btn-icon-split">
                                            <span class="icon text-white-60">
                                            <i class="fas fa-trash"></i>
                                            </span>
                                        </button>
                                    </form>

                                    <form action="siparis.php" method="POST">
                                        <input type="hidden" name="siparis_id" value="'.$sipariscek['id'].'">
                                        <button type="submit" name="siparis_bak" class="btn btn-primary btn-sm btn-icon-split">
                                            <span class="icon text-white-60">
                                            <i class="fas fa-eye"></i>
                                            </span>
                                        </button>
                                    </form>


                                </div>
                            </td> 
                            </tr>' ;
                        }
                     ?>
                    
                </tbody>
            </table>
        </div>
    </div>
</div>


<?php include 'footer.php' ; ?>