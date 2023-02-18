       <!-- Sidebar -->
       <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

        <!-- Sidebar - Brand -->
        <a class="sidebar-brand d-flex align-items-center justify-content-center" href="<?= Router::url('admin') ; ?>">
            <div class="sidebar-brand-icon rotate-n-15">
                <i class="fas fa-laugh-wink"></i>
            </div>
            <div class="sidebar-brand-text mx-3"> <?= $_SESSION['adminName'] ?? NULL ; ?>  </div>
        </a>

            <!-- Divider -->
            <hr class="sidebar-divider my-0">

            <!-- Nav Item - Dashboard -->
            <li class="nav-item active">
                <a class="nav-link" href="#">
                    <i class="fas fa-fw fa-tachometer-alt"></i>
                    <span>Admin Paneli</span></a>
            </li>

            <!-- Divider -->
            <hr class="sidebar-divider">







    <!-- Nav Item - Charts -->
     <li class="nav-item">
        <a class="nav-link" href="<?= Router::url('polikliniks') ; ?>">
            <i class="fas fa-fw fa-chart-area"></i>
            <span>Poliklinikler</span></a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="<?= Router::url('doctors') ; ?>">
            <i class="fas fa-fw fa-chart-area"></i>
            <span>Doktorlar</span></a>
    </li>

   
    
    <li class="nav-item">
        <a class="nav-link" href="<?= Router::url('seans') ; ?>">
            <i class="fas fa-fw fa-chart-area"></i>
            <span>Seanslar</span></a>
    </li>

    <li class="nav-item">
        <a class="nav-link" href="<?= Router::url('profileadmin') ; ?>">
            <i class="fas fa-fw fa-chart-area"></i>
            <span>Profil</span></a>
    </li>

    <li class="nav-item">
        <a class="nav-link" href="<?= Router::url('pagesettings') ; ?>">
            <i class="fas fa-fw fa-chart-area"></i>
            <span>Site Ayarları</span></a>
    </li>

   
    

    <!-- Divider -->
    <hr class="sidebar-divider d-none d-md-block">

    <!-- Sidebar Toggler (Sidebar) -->
    <div class="text-center d-none d-md-inline">
        <button class="rounded-circle border-0" id="sidebarToggle"></button>
    </div>



</ul>
<!-- End of Sidebar -->
