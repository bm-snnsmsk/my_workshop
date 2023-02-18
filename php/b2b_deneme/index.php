<?php require_once 'inc/header.php' ;?>


		<!-- WRAPPER START -->
		<div class="wrapper bg-dark-white">

			<!-- HEADER-AREA START -->
			<?php require_once 'inc/menu.php' ;?>
			<!-- HEADER-AREA END -->


			<!-- Mobile-menu start -->
			<?php require_once 'inc/mobile_menu.php' ;?>
			<!-- Mobile-menu end -->

			<!-- HEADING-BANNER START -->
			<div class="heading-banner-area overlay-bg" style="background:rgba(0,0,0,0) url(<?= site ?>/uploads/product/default.jpg) no-repeat scroll center center / cover ;">
				<div class="container">
					<div class="row">
						<div class="col-md-12">
							<div class="heading-banner">
								<div class="heading-banner-title">
									<h2>Ürünler</h2>
								</div>
								<div class="breadcumbs pb-15">
									<ul>
										<li><a href="<?= site ; ?>">anasayfa</a></li>
										<li>ürünler</li>
									</ul>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- HEADING-BANNER END -->
			<!-- PRODUCT-AREA START -->
			<div class="product-area pt-80 pb-80 product-style-2">
				<div class="container">
					<div class="row">
						
					<?php require_once 'inc/sidebar.php' ?>

						<?php

						// sayfalama için start
						$s = get('s');
						if(!$s){
							$s = 1 ;
						}
						// sayfalama için END
						$urunler_list = $db->prepare('SELECT * FROM urunler WHERE urunDurum = ? AND urunVitrin = ? ORDER BY urunDate DESC') ;
						$urunler_list->execute([1, 1]) ;

						$total = $urunler_list->rowCount() ;
						$limit = 9 ;
						$show = $s * $limit - $limit ;

						$urunler_list = $db->prepare('SELECT * FROM urunler WHERE urunDurum = ? AND urunVitrin = ? ORDER BY urunDate DESC LIMIT '.$show.', '.$limit) ;
						$urunler_list->execute([1,1]) ;

						if($s > ceil($total/$limit)){
							$s = 1 ;
						}




						?>


						<div class="col-lg-9 order-1 order-lg-2">
							<!-- Shop-Content End -->
							<div class="shop-content mt-tab-30 mb-30 mb-lg-0">
								<div class="product-option mb-30 clearfix">
								<p class="mb-0">ürün listesi (<?= $total ?>) </p>
								</div>
								<!-- Tab panes -->
								<div class="tab-content">
									<div class="tab-pane active" id="grid-view">							
										<div class="row">

											<?php 
											
											if($urunler_list->rowCount()){ 
												foreach($urunler_list as $urun){
												
											?> 

											<!-- Single-product start -->
											<div class="col-lg-4 col-md-6">
												<div class="single-product">
													<div class="product-img">
													
														<span class="pro-price-2"><?= $urun['urunFiyat'].' TL' ; ?></span>
														<a href="<?= site.'/product.php?productsef='.$urun['urunSef']; ?>"><img width="270" height="270" src="<?= site ?>/uploads/product/<?= $urun['urunKapakresim'] ?>" alt="<?= $urun['urunBaslik'] ; ?>" /></a>
													</div>
													<div class="product-info clearfix text-center">
														<div class="fix">
															<h4 class="post-title"><a href="<?= site.'/product.php?productsef='.$urun['urunSef']; ?>"><?= $urun['urunBaslik'] ; ?></a></h4>
														</div>
														<div class="product-action clearfix">

														
															<a href="" title="ürün detayı"><i class="zmdi zmdi-arrow-right"></i></a>
															<a href="" title="sepete ekle"><i class="zmdi zmdi-shopping-cart-plus"></i></a>
														</div>
													</div>
												</div>
												
											</div>
											<!-- Single-product end -->	
											
											<?php }}else{
												alert('ürün bulunmuyor', 'warning') ;
											} ?> 

										</div>
									</div>
								
								</div>
								<!-- Pagination start -->
								<div class="shop-pagination text-center">
									<div class="pagination">
										<ul>
											<?php 

												if($total > $limit){
													pagination($s, ceil($total/$limit), 'index.php?s=') ;
												}

											?>
										</ul>
									</div>
								</div>
								<!-- Pagination end -->
							</div>
							<!-- Shop-Content End -->
						</div>
					</div>
				</div>
			</div>
			<!-- PRODUCT-AREA END -->
		
			<!-- Footer start -->
			<?php require_once 'inc/footer.php' ;?>
			<!--Footer end -->