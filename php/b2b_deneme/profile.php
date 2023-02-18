<?php 
	require_once 'inc/header.php' ;

	if(isset($_SESSION['bayi_login'])){
		if($_SESSION['bayi_login'] != sha1(md5(IP().$bayi_kodu))){
			go(site) ;
		}
	}


	// print_r($_SESSION) ;
?>




<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.css">
  






		<!-- WRAPPER START -->
		<div class="wrapper bg-dark-white">

			<!-- HEADER-AREA START -->
			<?php require_once 'inc/menu.php' ;?>
			<!-- HEADER-AREA END -->


			<!-- Mobile-menu start -->
			<?php require_once 'inc/mobile_menu.php' ;?>
			<!-- Mobile-menu end -->

			<!-- HEADING-BANNER START -->
			<div class="heading-banner-area overlay-bg">
				<div class="container">
					<div class="row">
						<div class="col-md-12">
							<div class="heading-banner">
								<div class="heading-banner-title">
									<h2>PROFİL</h2>
								</div>
								<div class="breadcumbs pb-15">
									<ul>
										<li><a href="#">Anasayfa</a></li>
										<li>PROFİL</li>
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
						<div class="col-lg-3 order-2 order-lg-1">
						
							<!-- Widget-Categories start -->
							<aside class="widget widget-categories  mb-30">
								<div class="widget-title">
									<h4>MENÜ</h4>
								</div>
								<div id="cat-treeview"  class="widget-info product-cat boxscrol2">
									<ul>
										<li><a href="<?php echo site.'/profile.php?process=profil' ?>"><span>PROFİL BİLGİLERİ</span></a></li> 
										<li><a href="<?php echo site.'/profile.php?process=changepassword' ?>"><span>ŞİFRE DEĞİŞTİR</span></a></li> 
										<li><a href="<?php echo site.'/profile.php?process=logo' ?>"><span>LOGO DEĞİŞTİR</span></a></li> 
										<li><a href="<?php echo site.'/profile.php?process=address' ?>"><span>ADRESLERİM</span></a></li> 
										<li><a href="<?php echo site.'/profile.php?process=notification' ?>"><span>HAVALE BİLDİRİM</span></a></li> 
										<li><a href="<?php echo site.'/profile.php?process=order' ?>"><span>SİPARİŞLERİM</span></a></li> 
										<li><a href="<?php echo site.'/cart.php' ?>"><span>SEPETİM</span></a></li> 
										<li><a onclick="return confirm('Onaylıyor musunuz ');" href="<?php echo site.'/logout.php' ?>"><span>ÇIKIŞ</span></a></li> 

									</ul>
								</div>
							</aside>
							<!-- Widget-categories end -->							
						</div>
						
						<div class="col-lg-9 order-1 order-lg-2">
							
							<?php 

								$process = "" ;
								if(isset($_GET['process'])){
									$process = get("process") ;
								}else{
							?>
							<div class="shop-content mt-tab-30 mb-30 mb-lg-0">
								<div class="product-option mb-30 clearfix">
									<!-- Nav tabs -->
									<ul class="nav d-block shop-tab">
										<li>PROFİL BİLGİLERİ</li>
									</ul>
								</div>
								<!-- Tab panes -->
								<div class="tab-content">
									<div class="tab-pane active" id="grid-view">							
										<div class="row">
											<!-- Single-product start -->
											<div class="login-area">
												<div class="container">
													<div class="row">	
														<form action="" method="post" onsubmit="return false ;" id="bayi_profile_form">
															<div class="customer-login">

																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Kodu</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_kodu ; ?>" readonly name="bayi_kodu"></div>
																</div>
																
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi e-posta</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_email ; ?>" name="bayi_email"></div>
																</div>
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Adı</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_name ; ?>" name="bayi_name"></div>
																</div>
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi İndirim Oranı</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_gift ; ?>" name="bayi_gift"></div>
																</div>
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Telefon Numarası</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_phone ; ?>" name="bayi_telefon"></div>
																</div>
																
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Fax Numarası</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_fax ; ?>" name="bayi_fax"></div>
																</div>
																
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Vergi Numarası</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_vergi_no ; ?>" name="bayi_vergi_no"></div>
																</div>
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Vergi Dairesi</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_vergi_dairesi ; ?>" name="bayi_vergi_dairesi"></div>
																</div>
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Web Site Adresi</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_site ; ?>" name="bayi_site"></div>
																</div>
																																
																<button id="bayi_profile_update_button" onclick="bayi_profile_update() ;" type="submit" class="button-one submit-button mt-15">PROFİLİMİ GÜNCELLE</button>
															</div>
														</form>	
													</div>			
												</div>
											</div>
											<!-- Single-product end -->
										</div>
									</div>	
								</div>								
							</div>
							<?php
								}							
								switch($process){

									case 'logo' : 
									
										if(isset($_POST['logo_update'])){
											$bayi_logo_guncelle = $_FILES['bayi_logo_guncelle'] ;
											$bayi_logo_name = $bayi_logo_guncelle['name'] ;
											$bayi_logo_type = $bayi_logo_guncelle['type'] ;
											$bayi_logo_tmp_name = $bayi_logo_guncelle['tmp_name'] ;
											$bayi_logo_size = $bayi_logo_guncelle['size'] ;
											$bayi_logo_error = $bayi_logo_guncelle['error'] ;
											$bayi_logo_full_path = $bayi_logo_guncelle['full_path'] ;

											

											

											$bayi_logo_name = $bayi_kodu.'-'.uniqid() ;
											$bayi_logo_name = $bayi_logo_name.'.'.pathinfo($bayi_logo_full_path, PATHINFO_EXTENSION) ;
											$yuklemeYeri = __DIR__ .'/uploads/customer/'.$bayi_logo_name ;
											// echo($bayi_logo_name."<br/>");
											// echo($yuklemeYeri."<br/>");
											

											if($bayi_logo_error != 4){											
												if(move_uploaded_file($bayi_logo_tmp_name, $yuklemeYeri)){													
													$logo_guncelle = $db->prepare('UPDATE urun_bayiler SET urun_bayiLogo = ? WHERE urun_bayiKodu = ?') ;
													$logo_guncelle->execute([$bayi_logo_name, $bayi_kodu]) ;
													if($logo_guncelle){
														alert('resim başarıyla yüklendi', 'success') ;
														go(site.'/profile.php?process=logo') ;
													}else{
														alert('resim yükleme hatası', 'danger') ;
													}
												}else{
													alert('Olası dosya yükleme saldırısı!\n', 'danger') ;
												}
											}else if($bayi_logo_error == 4){
												alert('resim seçiniz..', 'warning') ;
											}
										}

									?>
									
									<form action="" method="post" enctype="multipart/form-data">
						<div class="customer-login text-left">

							<h4 class="title-1 title-border text-uppercase mb-30">LOGO GÜNCELLE</h4>

							<img src="<?= site.'/uploads/customer/'.$bayi_logo; ?>" alt="<?= $bayi_kodu ; ?>" width="100" height="100">
							<input type="file" name="bayi_logo_guncelle" class="form-control">
							
							<button type="submit" name="logo_update" class="button-one submit-button mt-15">logo güncelle</button>
						</div>
					</form>		

								<?php	break ;

									
									case 'notification' :
										$havale_bildirimleri = $db->prepare("SELECT * FROM urun_havale_bildirim INNER JOIN urun_banka ON urun_havale_bildirim.urun_havaleBanka = urun_banka.urun_bankaID WHERE urun_havaleBayi = ?") ;
										$havale_bildirimleri->execute([$bayi_kodu]) ;
										?>
							<div class="shop-content mt-tab-30 mb-30 mb-lg-0">
								<div class="product-option mb-30 clearfix">
									<!-- Nav tabs -->
									<ul class="nav d-block shop-tab">
										<li>HAVALE BİLDİRİMLERİ ( <?= $havale_bildirimleri->rowCount() ?> )</li>
										<li><a href="<?= site ; ?>/profile.php?process=new_notification" >[Yeni Bildirim Ekle]</a></li>
									</ul>
								</div>
								<!-- Tab panes -->
								<div class="tab-content">
									<div class="tab-pane active" id="grid-view">							
										<div class="row">
											<!-- Single-product start -->
											<div class="login-area">
												<div class="container">
													<div class="row">	

													<div class="table-responsive">
														<?php 
															
															if($havale_bildirimleri->rowCount()){
																
															

														?>
														<table class="table table-hover" id="myTable">
																<thead>
																	<th>HAVALE ID</th>
																	<th>HAVALE TARİH</th>
																	<th>HAVALE TUTAR</th>
																	<th>HAVALE BANKA</th>
																	<th>HAVALE NOT</th>
																</thead>
																<tbody>
																	<?php
																	foreach($havale_bildirimleri as $bildirim){ ?>
																		<tr>
																			<td><a href="" title="havale bildirim detayı">#<?= $bildirim['urun_havaleID'] ; ?></a></td>
																			<td><?= dt($bildirim['urun_havaleTarih'])." - ".dt($bildirim['urun_havaleSaat'], true) ; ?></td>
																			<td><?= $bildirim['urun_havaleTutar'] ; ?> TL</td>
																			<td><?= $bildirim['urun_bankaAdi'] ; ?></td>
																			<td><?= $bildirim['urun_havaleNot'] ; ?></td>
																		</tr>
                                                                    <?php	} ?>
																</tbody>
														</table>

														<?php }else{ 

														alert("KAYITLI havale bildiriminiz bulunmuyor !", "danger") ;
														} ?>
													</div>
														
													</div>			
												</div>
											</div>
											<!-- Single-product end -->
										</div>
									</div>	
								</div>								
							</div>
							<?php
										break ;


										case 'new_notification' :
											$banks = $db->prepare("SELECT * FROM urun_banka WHERE urun_bankaDurum = ?") ;
											$banks->execute([1]) ;
											

											//  $bankalar = $banks->fetchAll(PDO::FETCH_ASSOC);
								
											
										?>
							<form action="" method="post" onsubmit="return false;" id="new_notification_form">
						<div class="customer-login text-left">

							<h4 class="title-1 title-border text-uppercase mb-30">YENİ HAVALE BİLDİRİMİ</h4>
						
							<select name="havale_banka_name" id="" class="form-control">
							<option value="0">Banka Seçiniz</option>
								<?php								
								
									foreach($banks as $bank){		
										echo '<option value="'.$bank["urun_bankaID"].'">'.$bank["urun_bankaAdi"].'</option>' ;
									}
								
								?>
							</select>

							<input type="date" name="havale_date" class="form-control">
							<input type="time" name="havale_saat" class="form-control">
							<input type="text" name="havale_tutar" class="form-control" placeholder="havale ücreti giriniz...">
							<textarea name="havale_description" cols="5" rows="4" placeholder="havale açıklaması giriniz..." class="form-control"></textarea>



							<button type="submit" onclick="new_notification()" id="new_notification_button" class="button-one submit-button mt-15">HAVALE BİLDİRİMİ EKLE</button>
						</div>
					</form>		



								<?php
								
								break ;





									case 'order' :
										$orders = $db->prepare("SELECT * FROM siparisler INNER JOIN durumkodlari ON durumkodlari.durumkodlariKodu = siparisler.siparislerDurum WHERE siparislerBayi = ?") ;
															$orders->execute([$bayi_kodu]) ;
										?>
							<div class="shop-content mt-tab-30 mb-30 mb-lg-0">
								<div class="product-option mb-30 clearfix">
									<!-- Nav tabs -->
									<ul class="nav d-block shop-tab">
										<li>SİPARİŞLERİM ( <?= $orders->rowCount() ?> )</li>
									</ul>
								</div>
								<!-- Tab panes -->
								<div class="tab-content">
									<div class="tab-pane active" id="grid-view">							
										<div class="row">
											<!-- Single-product start -->
											<div class="login-area">
												<div class="container">
													<div class="row">	

													<div class="table-responsive">
														<?php 
															
															if($orders->rowCount()){
																
															

														?>
														<table class="table table-hover" id="myTable">
																<thead>
																	<th>KOD</th>
																	<th>DURUM</th>
																	<th>TUTAR</th>
																	<th>ÖDEME TÜRÜ</th>
																	<th>TARİH</th>
																</thead>
																<tbody>
																	<?php
																	foreach($orders as $order){ ?>
																		<tr>
																			<td><a href="" title="sipariş detayı"><?= $order['siparislerKodu'] ; ?></a></td>
																			<td><?= $order['durumkodlariBaslik'] ; ?></td>
																			<td><?= $order['siparislerTutar'] ; ?></td>
																			<td><?= $order['siparislerOdeme'] == '1' ? 'Havale' : 'Kredi Kartı'   ; ?></td>
																			<td><?= dt($order['siparislerTarih']).' - '.dt($order['siparislerSaat'], true) ; ?></td>
																		</tr>
                                                                    <?php	} ?>
																</tbody>
														</table>

														<?php }else{ 

														alert("siparişiniz bulunmuyor !", "danger") ;
														} ?>
													</div>
														
													</div>			
												</div>
											</div>
											<!-- Single-product end -->
										</div>
									</div>	
								</div>								
							</div>
							<?php
										break ;
		case 'adres_sil' : 
			$ID = get('ID') ;
			if(!$ID){
				go(site) ;
			}
			$adres_sil = $db->prepare("SELECT * FROM urun_adresler WHERE urun_adresBayi = ? AND urun_adresID  = ?") ;
			$adres_sil->execute([$bayi_kodu, $ID]) ; 
			if($adres_sil->rowCount()){
				$sil = $db->prepare("UPDATE urun_adresler SET urun_adresDurum = ? WHERE urun_adresBayi = ? AND urun_adresID  = ?") ;
				$sil->execute([0, $bayi_kodu, $ID]) ; 
				if($sil->rowCount()){
					alert('Adresiniz silindi', 'success') ;
					go($_SERVER['HTTP_REFERER'], 2) ;
				}else{
					alert('bir hata oluştu', 'danger') ;
				}
			}else{
				go(site) ;
			}
		break ;
		case 'adres_duzenle' : 
			$ID = get('ID') ;
			if(!$ID){
				go(site) ;
			}
			$adres_duzenle = $db->prepare("SELECT * FROM urun_adresler WHERE urun_adresBayi = ? AND urun_adresID  = ?") ;
			$adres_duzenle->execute([$bayi_kodu, $ID]) ; 
			if($adres_duzenle->rowCount()){
				$address_datas = $adres_duzenle->fetch(PDO::FETCH_ASSOC) ;
				// print_r($address_datas) ;
		?>

					<form action="" method="post" onsubmit="return false;" id="bayi_address_update_form">
						<div class="customer-login text-left">

							<h4 class="title-1 title-border text-uppercase mb-30">ADRES DÜZENLE</h4>								
							<input type="hidden" name="adres_id" value="<?= $address_datas['urun_adresID'] ; ?>">
							<input type="text" name="adres_baslik" value="<?= $address_datas['urun_adresBaslik'] ; ?>">
							<input type="text" name="adres_icerik" value="<?= $address_datas['urun_adresTarif'] ; ?>">
							<select name="status" id="" class="form-control">
								<option value="1" <?= ($address_datas['urun_adresDurum'] == 1) ? 'selected' : NULL ; ?> >Aktif</option>
								<option value="0" <?= ($address_datas['urun_adresDurum'] == 0) ? 'selected' : NULL ; ?> >Pasif</option>
							</select>
							
							<button type="submit" onclick="bayi_address_update()" id="bayi_address_update_button" class="button-one submit-button mt-15">adres güncelle</button>
						</div>
					</form>		

		<?php
			}else{
				go(site) ;
			} 
		break ;


		case 'newaddress' :
		?>

					<form action="" method="post" onsubmit="return false;" id="bayi_new_address_form">
						<div class="customer-login text-left">

							<h4 class="title-1 title-border text-uppercase mb-30">ADRES EKLE</h4>
							<input type="text" name="adres_baslik" placeholder="adres beşlık">
							<input type="text" name="adres_icerik" placeholder="açık adres">
							<button type="submit" onclick="bayi_new_address()" id="bayi_new_address_button" class="button-one submit-button mt-15">adres ekle</button>
						</div>
					</form>		

		<?php
			
		break ;



									case 'address' :
										
										$adresses = $db->prepare("SELECT * FROM urun_adresler WHERE urun_adresBayi = ?") ;
										$adresses->execute([$bayi_kodu]) ;
										?>
							<div class="shop-content mt-tab-30 mb-30 mb-lg-0">
								<div class="product-option mb-30 clearfix">
									<!-- Nav tabs -->
									<ul class="nav d-block shop-tab">
										<li>ADRESLERİM ( <?= $adresses->rowCount() ?> )</li>
										<li><a href="<?= site ?>/profile.php?process=newaddress" >[Yeni Adres Ekle]</a></li>
									</ul>
								</div>
								<!-- Tab panes -->
								<div class="tab-content">
									<div class="tab-pane active" id="grid-view">							
										<div class="row">
											<!-- Single-product start -->
											<div class="login-area">
												<div class="container">
													<div class="row">	

													<div class="table-responsive">
														<?php 
															
															if($adresses->rowCount()){
																
															

														?>
														<table class="table table-hover" id="myTable">
																<thead>
																	<th>ADRES ID</th>
																	<th>ADRES BAŞLIK</th>
																	<th>ADRES</th>
																	<th>ADRES DURUM</th>
																	<th>işlem</th>
																</thead>
																<tbody>
																	<?php
																	foreach($adresses as $adress){ ?>
																		<tr>
																			<td>#<?= $adress['urun_adresID'] ; ?></td>
																			<td><?= $adress['urun_adresBaslik'] ; ?></td>
																			<td><?= $adress['urun_adresTarif'] ; ?></td>
																			<td><?= $adress['urun_adresDurum'] == 1 ? "Aktif" : "Pasif" ; ?></td>
																			<td>
					<a href="<?= site; ?>/profile.php?process=adres_sil&ID=<?= $adress['urun_adresID']; ?>" class="btn btn-danger btn-sm" title="adresi sil"><i class="zmdi zmdi-close"></i></a>
					<a href="<?= site; ?>/profile.php?process=adres_duzenle&ID=<?= $adress['urun_adresID']; ?>" class="btn btn-warning btn-sm" title="adresi düzenle"><i class="zmdi zmdi-edit"></i></a>
						                                               </td>
																		</tr>
                                                                    <?php	} ?>
																</tbody>
														</table>

														<?php }else{ 

														alert("KAYITLI ADRESİNİZ bulunmuyor !", "danger") ;
														} ?>
													</div>
														
													</div>			
												</div>
											</div>
											<!-- Single-product end -->
										</div>
									</div>	
								</div>								
							</div>
										<?php
										break ;
									case 'profil' : 
							?> 
							<!-- Shop-Content End -->
							<div class="shop-content mt-tab-30 mb-30 mb-lg-0">
								<div class="product-option mb-30 clearfix">
									<!-- Nav tabs -->
									<ul class="nav d-block shop-tab">
										<li>PROFİL BİLGİLERİ</li>
									</ul>
								</div>
								<!-- Tab panes -->
								<div class="tab-content">
									<div class="tab-pane active" id="grid-view">							
										<div class="row">
											<!-- Single-product start -->
											<div class="login-area">
												<div class="container">
													<div class="row">	
														<form action="" method="post" onsubmit="return false ;" id="bayi_profile_form">
															<div class="customer-login">

																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Kodu</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_kodu ; ?>" readonly name="bayi_kodu"></div>
																</div>
																
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi e-posta</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_email ; ?>" name="bayi_email"></div>
																</div>
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Adı</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_name ; ?>" name="bayi_name"></div>
																</div>
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi İndirim Oranı</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_gift ; ?>" name="bayi_gift"></div>
																</div>
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Telefon Numarası</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_phone ; ?>" name="bayi_telefon"></div>
																</div>
																
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Fax Numarası</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_fax ; ?>" name="bayi_fax"></div>
																</div>
																
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Vergi Numarası</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_vergi_no ; ?>" name="bayi_vergi_no"></div>
																</div>
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Vergi Dairesi</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_vergi_dairesi ; ?>" name="bayi_vergi_dairesi"></div>
																</div>
																<div class="row">
																	<div class="col-sm-4"><label for="">Bayi Web Site Adresi</label></div>
																	<div class="col-sm-8"><input type="text" value="<?= $bayi_site ; ?>" name="bayi_site"></div>
																</div>
																																
																<button id="bayi_profile_update_button" onclick="bayi_profile_update() ;" type="submit" class="button-one submit-button mt-15">PROFİLİMİ GÜNCELLE</button>
															</div>
														</form>	
													</div>			
												</div>
											</div>
											<!-- Single-product end -->
										</div>
									</div>	
								</div>								
							</div>
							<!-- Shop-Content End -->
							<?php
									break ;

									case 'changepassword' : 
										?> 
										<!-- Shop-Content End -->
										<div class="shop-content mt-tab-30 mb-30 mb-lg-0">
											<div class="product-option mb-30 clearfix">
												<!-- Nav tabs -->
												<ul class="nav d-block shop-tab">
													<li>ŞİFRE DEĞİŞTİR</li>
												</ul>
											</div>
											<!-- Tab panes -->
											<div class="tab-content">
												<div class="tab-pane active" id="grid-view">							
													<div class="row">
														<!-- Single-product start -->
														<div class="login-area">
															<div class="container">
																<div class="row">	
																	<form action="" method="post" onsubmit="return false ;" id="bayi_password_update_form">
																		<div class="customer-login">
			
																			<div class="row">
																				<div class="col-sm-4"><label for="">Yeni Şifreniz </label></div>
																				<div class="col-sm-8"><input type="password" name="bayi_password"></div>
																			</div>
																			
																			<div class="row">
																				<div class="col-sm-4"><label for="">Yeni Şifreniz Tekrarı</label></div>
																				<div class="col-sm-8"><input type="password" name="bayi_password_again"></div>
																			</div>	
																																			
																			<button id="bayi_password_update_button" onclick="bayi_password_update() ;" type="submit" class="button-one submit-button mt-15">ŞİFRENİ GÜNCELLE</button>
																		</div>
																	</form>	
																</div>			
															</div>
														</div>
														<!-- Single-product end -->
													</div>
												</div>	
											</div>								
										</div>
										<!-- Shop-Content End -->
										<?php
												break ;
											}
										?>










						</div>
					</div>
				</div>
			</div>
			<!-- PRODUCT-AREA END -->
	
	


			<!-- Footer start -->
			<?php require_once 'inc/footer.php' ;?>
			<!--Footer end -->

			
			<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.js"></script>

			<script>
$(document).ready( function () {
    $('#myTable').DataTable();
} );
			</script>