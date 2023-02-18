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
			<div class="heading-banner-area overlay-bg">
				<div class="container">
					<div class="row">
						<div class="col-md-12">
							<div class="heading-banner">
								<div class="heading-banner-title">
									<h2>Contact Us</h2>
								</div>
								<div class="breadcumbs pb-15">
									<ul>
										<li><a href="index.html">Home</a></li>
										<li>Contact Us</li>
									</ul>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- HEADING-BANNER END -->

			<!-- contact-us-AREA START -->
			<div class="contact-us-area  pt-80 pb-80">
				<div class="container">	
					<div class="contact-us customer-login bg-white">
						<div class="row">
							<div class="col-lg-4 col-md-5">
								<div class="contact-details">
									<h4 class="title-1 title-border text-uppercase mb-30">iletişim bilgileri</h4>
									<ul>
										<li>
											<i class="zmdi zmdi-pin"></i>
											
											<span><?= $row->ayarlarAdres ?></span>
										</li>
										<li>
											<i class="zmdi zmdi-phone"></i>
												
											<span><?= $row->ayarlarTelefon ?></span>
											<span><?= $row->ayarlarFax ?></span>
										</li>
										<li>
											<i class="zmdi zmdi-email"></i>
											<span><?= $row->ayarlarEposta ?></span>
										</li>
									</ul>
								</div>
								<div class="send-message mt-60">
									<form id="iletisim_form" onsubmit="return false;" method="post">
										<h4 class="title-1 title-border text-uppercase mb-30">İLETİŞİM FORMU</h4>
										<input type="text" name="your_name" placeholder="adınız" />
										<input type="text" name="your_email" placeholder="email adresiniz..." />
										<input type="text" name="your_konu" placeholder="konu" />
										<textarea class="custom-textarea" name="your_message" placeholder="mesajınız.."></textarea>
										<button class="button-one submit-button mt-20" type="submit" onclick="iletisim_form()" id="iletisim_form_button">mesaj gönder</button>
										<p class="form-message"></p>
									</form>
								</div>
							</div>
							<div class="col-lg-8 col-md-7 mt-xs-30">
								<div class="map-area">
									
									<?= $row->ayarlarMap ?>
								
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- ABOUT-US-AREA END -->

			<!-- FOOTER START -->
			<?php require_once 'inc/footer.php' ;?>
			<!-- FOOTER END -->
