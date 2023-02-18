<?php 
	require_once 'inc/header.php' ;

	if(isset($_SESSION['bayi_login'])){
		if($_SESSION['bayi_login'] == sha1(md5(IP().$bayi_kodu))){
			go(site) ;
		}
	}
?>

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
							<h2>kayıt | giriş</h2>
						</div>
						<div class="breadcumbs pb-15">
							<ul>
								<li><a href="<?= site ?>">anasayfa</a></li>
								<li>kayıt | giriş</li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<!-- HEADING-BANNER END -->

	<!-- SHOPPING-CART-AREA START -->
	<div class="login-area  pt-80 pb-80">
		<div class="container">
			<div class="row">					
				<div class="col-lg-6">
					<form action="" method="post" onsubmit="return false;" id="bayi_login_form">
						<div class="customer-login text-left">
							<h4 class="title-1 title-border text-uppercase mb-30">BAYİ GİRİŞİ</h4>								
							<input type="text" placeholder="Email veya bayi kodu giriniz" name="bayi_email_or_bayi_code">
							<input type="password" placeholder="Password" name="bayi_password">
							<p><a href="#" class="text-gray">Şifremi unuttum</a></p>
							<button type="submit" onclick="bayi_login()" id="bayi_login_button" class="button-one submit-button mt-15">GİRİŞ YAP</button>
						</div>
					</form>					
				</div>

				<div class="col-lg-6">
					<form action="" method="post" onsubmit="return false;" id="bayi_register_form">
						<div class="customer-login text-left">
							<h4 class="title-1 title-border text-uppercase mb-30">BAYİ KAYIT</h4>
							
							<input type="text" placeholder="Bayi Adı" name="bayi_name">
							<input type="text" placeholder="Bayi e-posta" name="bayi_email">
							<input type="password" placeholder="Şifre" name="bayi_password">
							<input type="password" placeholder="Şifre Tekrar" name="bayi_password_tekrar">
							<input type="text" placeholder="Bayi Telefon" name="bayi_telefon">
							<input type="text" placeholder="Bayi Vergi No" name="bayi_vergino">
							<input type="text" placeholder="Bayi Vergi Dairesi" name="bayi_vergi_dairesi">
						
							<button id="bayi_register_button" onclick="bayi_register()" type="submit" class="button-one submit-button mt-15">Kayıt Ol</button>
						</div>
					</form>					
				</div>
			</div>			
		</div>
	</div>
	<!-- SHOPPING-CART-AREA END -->

			<!-- FOOTER START -->
			<?php require_once 'inc/footer.php' ;?>
			<!-- FOOTER END -->