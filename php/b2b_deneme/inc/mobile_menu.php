
			<div class="mobile-menu-area">
				<div class="container-fluid">
					<div class="row">
						<div class="col-xs-12 d-block d-md-none">
							<div class="mobile-menu">
								<nav id="dropdown">
								<ul>
							<li><a href="<?= site ; ?>">ANASAYFA</a></li>
							<li><a href="<?= site ; ?>">ÜRÜNLER</a></li>
							<li><a href="<?= site ; ?>/contact.php">BİZE ULAŞIN</a></li>

							<?php if(isset($_SESSION['bayi_login'])){ ?>
                            	<li><a href="<?= site ; ?>/profile.php?process=profil">HESABIM</a></li>	
								<li><a onclick="return confirm('Onaylıyor musunuz ');" href="<?= site ; ?>/logout.php">ÇIKIŞ YAP</a></li>
							<?php }else{ ?>
								<li><a href="<?= site ; ?>/login.php">KAYIT OL</a></li>					
								<li><a href="<?= site ; ?>/login.php">GİRİŞ YAP</a></li>		
							<?php } ?>

														
						</ul>
								</nav>
							</div>
						</div>
					</div>
				</div>
			</div>