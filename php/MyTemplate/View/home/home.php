<?php Helper::view('static/header') ; ?>

<div class="alert alert-success">Bilgilendirme</div>
<div class="text-danger">Sinan şimşek</div>

<div class="container-fluid">
    <div class="row col-md-6">
        <div class="card">
            <?php
                $text = "eşeş ğilş *45" ;
                echo $text."<br/>" ;
                echo Helper::sefLink($text) ;
            ?>
        </div>
    </div>
</div>

<?php Helper::view('static/footer') ; ?>