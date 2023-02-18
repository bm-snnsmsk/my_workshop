<?php

    $banks = $db->prepare("SELECT * FROM urun_banka WHERE urun_bankaDurum = ?") ;
    $banks->execute([1]) ;
    echo $banks->rowCount();

    $bankalar = $banks->fetchAll(PDO::FETCH_ASSOC);
    $aa = 0 ;
			

?>




		<?php								
		
			foreach($bankalar as $bank){
				$aa++ ;							
				echo '<li>'.$bank["urun_bankaAdi"].'</li>' ;
			}
		
		?>


