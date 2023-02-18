<?php include 'header.php' ; ?>


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