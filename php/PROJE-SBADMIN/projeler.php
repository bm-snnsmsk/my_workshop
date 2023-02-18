<?php include 'header.php' ; ?>


<div class="container">
    <div class="card">
        <div class="card-header">
            <h5 class="card-title">Prpjeler</h5>
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


<?php include 'footer.php' ; ?>