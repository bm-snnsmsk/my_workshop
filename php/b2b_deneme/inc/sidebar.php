<?php  
    $categoriler = $db->prepare('SELECT * FROM urun_kategoriler WHERE urun_kategoryDurum = ?') ;
    $categoriler->execute([1]) ; 
 ?>

<div class="col-lg-3 order-2 order-lg-1">
	<!-- Widget-Search start -->
	<aside class="widget widget-search mb-30">
		<form action="#">
			<input type="text" placeholder="ürün arama..." />
			<button type="submit">
				<i class="zmdi zmdi-search"></i>
			</button>
		</form>
	</aside>
	<!-- Widget-search end -->
	<!-- Widget-Categories start -->
	<aside class="widget widget-categories  mb-30">
		<div class="widget-title">
			<h4>kategoriler (<?= $categoriler->rowCount() ?>)</h4>
		</div>
		<div id="cat-treeview"  class="widget-info product-cat boxscrol2">
			<ul>
			<?php 
                
                if($categoriler->rowCount()){
                    foreach($categoriler as $cat){
                        echo '<li><a href="category.php?catsef='.$cat['urun_kategorySef'].'"><span>'.$cat['urun_kategoryBaslik'].'</span></a></li>' ;
                    }
                }
            ?>
			</ul>
		</div>
	</aside>
	<!-- Widget-categories end -->
	<!-- Shop-Filter start -->
	<aside class="widget shop-filter mb-30">
		<div class="widget-title">
			<h4>fiyat</h4>
		</div>
		<div class="widget-info">
			<div class="price_filter">
				<div class="price_slider_amount">
					<input type="submit"  value="You range :"/> 
					<input type="text" id="amount" name="price"  placeholder="Add Your Price" /> 
				</div>
				<div id="slider-range"></div>
			</div>
		</div>
	</aside>
	<!-- Shop-Filter end -->




</div>