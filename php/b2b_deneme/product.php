<?php require_once 'inc/header.php' ;?>

		<!-- WRAPPER START -->
		<div class="wrapper bg-dark-white">

			<!-- HEADER-AREA START -->
			<?php require_once 'inc/menu.php' ;?>
			<!-- HEADER-AREA END -->

			<!-- Mobile-menu start -->
			<?php require_once 'inc/mobile_menu.php' ;?>
			<!-- Mobile-menu end -->


			<?php

			$sef = get('productsef');

			

			if(!$sef){
				go(site) ;
			}

			$products = $db->prepare('SELECT * FROM urunler WHERE urunDurum = ? AND urunSef = ?');
			$products->execute([1, $sef]);

			

			
			if($products->rowCount()){
				$pro = $products->fetch(PDO::FETCH_ASSOC) ;
			}else{
				go(site) ;
			}


			//ürün yprumları start
			$comments = $db->prepare('SELECT * FROM urun_yorumlar WHERE urun_yorumDurum = ? AND urun_yorumUrun = ? ORDER BY urun_yorumTarih DESC') ; 
			$comments->execute([1, $pro['urunKodu']]) ;
		    //ürün yprumları end





            ?>
			<!-- HEADING-BANNER START -->
			<div class="heading-banner-area overlay-bg" style="background:rgba(0,0,0,0) url(<?= site ?>/uploads/product/default.jpg) no-repeat scroll center center / cover ;">
				<div class="container">
					<div class="row">
						<div class="col-md-12">
							<div class="heading-banner">
								<div class="heading-banner-title">
									<h2><?= $pro['urunBaslik']  ?></h2>
								</div>
								<div class="breadcumbs pb-15">
									<ul>
										<li><a href="<?= site ?>">anasayfa</a></li>
										<li>ürün</li>
										<li><?= $pro['urunBaslik']  ?></li>
									</ul>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- HEADING-BANNER END -->

			<!-- PRODUCT-AREA START -->
			<div class="product-area single-pro-area pt-80 pb-80 product-style-2">
				<div class="container">	
					<div class="row shop-list single-pro-info no-sidebar">
						<!-- Single-product start -->
						<div class="col-lg-12">
							<div class="single-product clearfix">
								<!-- Single-pro-slider Big-photo start -->
								<div class="single-pro-slider single-big-photo view-lightbox slider-for">

								<?php 
								
			$pimage = $db->prepare("SELECT * FROM urun_resimler WHERE urun_resimlerDurum = ? AND urun_resimlerUrun = ?  ORDER BY urun_resimlerTarih DESC") ;
			$pimage->execute([1, $pro['urunKodu']]);
									
									if($pimage->rowCount()){
										foreach($pimage as $pim){
										

									
									?>

									<div>
										<img width="370" height="450" src="<?= site.'/uploads/product/'.$pim['urun_resimlerDosya']  ?>" alt="<?= $pro['urunBaslik']  ?>" width="370" height="450" />
										<a class="view-full-screen" href="<?= site.'/uploads/product/'.$pim['urun_resimlerDosya']  ?>"  data-lightbox="roadtrip" data-title="<?= $pro['urunBaslik']  ?>"><i class="zmdi zmdi-zoom-in"></i>
										</a>
									</div>

									<?php }} ?>

									
								</div>	
								<!-- Single-pro-slider Big-photo end -->								
								<div class="product-info">
									
									<div class="fix mb-20">
										<span class="pro-price"><?= $pro['urunFiyat']  ?>  TL | <b>Ürün kodu : </b><?= $pro['urunKodu']  ?></span>
									</div>
									<div class="product-description">
										<p>
											<?= strip_tags(mb_substr($pro['urunDescription'], 0, 500, 'utf8'))."... <br/> <a href='#description'>Tüm açıklamayı oku...</a>" ; ?>

									</p>
									
									</div>
							
									<div class="clearfix">
										<div class="cart-plus-minus">
											<input type="text" value="1" name="qtybutton" class="cart-plus-minus-box">
										</div>
										<div class="product-action clearfix">
											<a href="cart.html" data-bs-toggle="tooltip" data-placement="top" title="Add To Cart"><i class="zmdi zmdi-shopping-cart-plus"></i></a>
										</div>
									</div>

									<div class="single-pro-slider single-sml-photo slider-nav">

								    	<?php 
									$pimag = $db->prepare("SELECT * FROM urun_resimler WHERE urun_resimlerDurum = ? AND urun_resimlerUrun = ? ORDER BY urun_resimlerTarih DESC") ;
									$pimag->execute([1, $pro['urunKodu']]);
										if($pimag->rowCount()){
											foreach($pimag as $pimg){
										?>

											<div>
												<img width="70" height="83" src="<?= site.'/uploads/product/'.$pimg['urun_resimlerDosya'] ?>" alt="<?= $pro['urunBaslik'] ?>">
											</div>

										<?php }} ?>
										
									</div>
								
								</div>
							</div>
						</div>
						<!-- Single-product end -->
					</div>
					<!-- single-product-tab start -->
					<div class="single-pro-tab">
						<div class="row">
							<div class="col-md-3">
								<div class="single-pro-tab-menu">
									<!-- Nav tabs -->
									<ul class="nav d-block">
										<li><a class="active" href="#description" data-bs-toggle="tab">Ürün Açıklaması</a></li>
										<li><a href="#reviews"  data-bs-toggle="tab">Ürün Yorumlar (<?= $comments->rowCount() ?>)</a></li>
										<li><a href="#information" data-bs-toggle="tab">Ürün Özellikler</a></li>
									</ul>
								</div>
							</div>
							<div class="col-md-9">
								<!-- Tab panes -->
								<div class="tab-content">
									<div class="tab-pane active" id="description">
										<div class="pro-tab-info pro-description">
											<h3 class="tab-title title-border mb-30"><?= $pro['urunBaslik']  ?> açıklaması</h3>
											<p><?= $pro['urunIcerik']  ?></p>
										</div>
									</div>

								

									<div class="tab-pane" id="reviews">
										<div class="pro-tab-info pro-reviews">
											<div class="customer-review mb-60">
												<h3 class="tab-title title-border mb-30"><?= $pro['urunBaslik']  ?> yorumları (<?= $comments->rowCount() ?>)</h3>
													<ul class="product-comments clearfix">


													<?php
															if($comments->rowCount()){
																foreach($comments as $comment){
													?>

														<li class="mb-30" style="border-bottom:1px solid #ddd; list-style-type:none">
															
															<div class="pro-reviewer-comment">
																<div class="fix">
																	<div class="floatleft mbl-center">
																		<h5 class="text-uppercase mb-0"><strong><?= $comment['urun_yorumIsim']  ?></strong></h5>
																		<p class="reply-date"><?= dt($comment['urun_yorumTarih']).' - '.dt($comment['urun_yorumTarih'],true)  ?></p>
																	</div>
																	
																</div>
																<p class="mb-0"><?= $comment['urun_yorumIcerik']  ?></p>
															</div>
														</li>

														
													</ul>


													<?php
																}
															}else{
																alert("bu ürüne henüz yorum yapılmamış. İlk yorumu siz yapın... ", 'warning') ;
															}
														?>


											</div>



											<?php  
											
											
											
												if(@$_SESSION['bayi_login'] == @sha1(md5(IP().$bayi_kodu))){ ?>
											
												
												<div class="leave-review">
													<h3 class="tab-title title-border mb-30">yorum yapın</h3>											
													<div class="reply-box">
														<form action="#" id="new_comment_form" onsubmit="return false;">															
															<div class="row">
																<div class="col-md-12">
																	<textarea class="custom-textarea" name="your_comment" placeholder="yorum yap..." ></textarea>
																	<input type="hidden" name="product_code" value="<?= $pro['urunKodu'] ?>">
																	<button onclick="new_comment()" id="new_comment_button" type="submit" class="button-one submit-button mt-20">Yorum yap</button>
																</div>
															</div>
														</form>
													</div>
												</div>

											<?php }else{
												alert('yorum yapmak için giriş yapın. <a href="'.site.'/login.php" >Giriş Yap</a> ','warning');
											} ?>


										
										</div>		
									</div>
									<div class="tab-pane" id="information">
										<div class="pro-tab-info pro-information">
											<h3 class="tab-title title-border mb-30"><?= $pro['urunBaslik']  ?> Özellikleri</h3>
											<div class="table-responsive">
												<table class="table table-hover">
													<?php
														$product_property = $db->prepare('SELECT * FROM urun_ozellik WHERE urun_ozellikDurum = ? AND urun_ozellikUrun = ?') ;
														$product_property->execute([1, $pro['urunKodu']]) ;
														if($product_property->rowCount()){ 
															foreach($product_property as $val){   ?>

															<tr>
																<th><?= $val['urun_ozellikBaslik'] ?></th>
																<td><?= $val['urun_ozellikIcerik'] ?></td>
															</tr>
																
														<?php	}
														}else{
															alert('ürün özelliği eklenmemiştir', 'warning') ;
														}
													?>
												</table>
											</div>
										</div>											
									</div>
									
								</div>									
							</div>
						</div>
					</div>
					<!-- single-product-tab end -->
				</div>
			</div>
			<!-- PRODUCT-AREA END -->

			<!-- FOOTER START -->
			<?php require_once 'inc/footer.php' ;?>
			<!-- FOOTER END -->