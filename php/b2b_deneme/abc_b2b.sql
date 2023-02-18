-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 12 Oca 2023, 10:35:07
-- Sunucu sürümü: 10.4.27-MariaDB
-- PHP Sürümü: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `abc_b2b`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `ayarlar`
--

CREATE TABLE `ayarlar` (
  `ayarlarIP` int(11) NOT NULL,
  `ayarlarSiteBaslik` varchar(250) NOT NULL,
  `ayarlarSiteUrl` varchar(250) NOT NULL,
  `ayarlarSiteDescription` varchar(250) NOT NULL,
  `ayarlarSiteLogo` varchar(250) NOT NULL,
  `ayarlarSiteKeyword` varchar(250) NOT NULL,
  `ayarlarSiteKDV` int(11) NOT NULL,
  `ayarlarSiteSiparisDurum` varchar(250) NOT NULL,
  `ayarlarSiteDurum` tinyint(1) NOT NULL DEFAULT 1,
  `ayarlarSmtpHost` varchar(250) NOT NULL,
  `ayarlarSmtpEmail` varchar(250) NOT NULL,
  `ayarlarSmtpSifre` varchar(250) NOT NULL,
  `ayarlarSmtpSec` varchar(250) NOT NULL,
  `ayarlarSmtpPort` varchar(250) NOT NULL,
  `ayarlarSmtpKime` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `bayiloglari`
--

CREATE TABLE `bayiloglari` (
  `bayiloglariID` int(11) NOT NULL,
  `bayiloglariBayi` varchar(250) NOT NULL,
  `bayiloglariTarih` timestamp NOT NULL DEFAULT current_timestamp(),
  `bayiloglariIP` varchar(250) NOT NULL,
  `bayiloglariAciklama` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `durumkodlari`
--

CREATE TABLE `durumkodlari` (
  `durumkodlariID` int(11) NOT NULL,
  `durumkodlariBaslik` varchar(250) NOT NULL,
  `durumkodlariKodu` varchar(250) NOT NULL,
  `durumkodlariTarih` timestamp NOT NULL DEFAULT current_timestamp(),
  `durumkodlariEkleyen` int(11) NOT NULL,
  `durumkodlariDurum` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `mesajlar`
--

CREATE TABLE `mesajlar` (
  `mesajID` int(11) UNSIGNED NOT NULL,
  `mesajIsim` varchar(250) NOT NULL,
  `mesajPosta` varchar(250) NOT NULL,
  `mesajKonu` varchar(250) NOT NULL,
  `mesajIcerik` text NOT NULL,
  `mesajDurum` tinyint(1) NOT NULL DEFAULT 1,
  `mesajIP` varchar(250) NOT NULL,
  `mesajTarih` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `sepet`
--

CREATE TABLE `sepet` (
  `sepetID` int(11) NOT NULL,
  `sepetBayi` varchar(250) NOT NULL,
  `sepetUrun` varchar(250) NOT NULL,
  `sepetAdet` int(11) NOT NULL,
  `sepetTarih` date NOT NULL,
  `sepetSilinme` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `siparisler`
--

CREATE TABLE `siparisler` (
  `siparislerID` int(11) NOT NULL,
  `siparislerBayi` varchar(250) NOT NULL,
  `siparislerTarih` date NOT NULL,
  `siparislerSaat` date NOT NULL,
  `siparislerDurum` tinyint(1) NOT NULL DEFAULT 1,
  `siparislerNot` text NOT NULL,
  `siparislerTutar` double(15,2) NOT NULL,
  `siparislerOdeme` tinyint(1) NOT NULL DEFAULT 1 COMMENT '1 - havele 2 - kredi kartı',
  `siparislerKodu` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `siparis_urunler`
--

CREATE TABLE `siparis_urunler` (
  `siparis_urunlerID` int(11) NOT NULL,
  `siparis_urunlerKodu` varchar(250) NOT NULL,
  `siparis_urunlerUrun` varchar(250) NOT NULL,
  `siparis_urunlerBirim` double(15,2) NOT NULL,
  `siparis_urunlerAdet` int(11) NOT NULL,
  `siparis_urunlerToplam` double(15,2) NOT NULL,
  `siparis_urunlerUrunAdi` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urunler`
--

CREATE TABLE `urunler` (
  `urunID` int(11) NOT NULL,
  `urunKategori` int(11) NOT NULL,
  `urunBaslik` varchar(250) NOT NULL,
  `urunSef` varchar(250) NOT NULL,
  `urunIcerik` text NOT NULL,
  `urunKapakresim` varchar(250) NOT NULL,
  `urunBannerresim` varchar(250) NOT NULL,
  `urunFiyat` double(15,2) NOT NULL,
  `urunKodu` varchar(250) NOT NULL,
  `urunStok` int(11) NOT NULL,
  `urunKeyword` varchar(250) NOT NULL,
  `urunDescription` varchar(250) NOT NULL,
  `urunDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `urunEkleyen` int(11) NOT NULL,
  `urunVitrin` tinyint(1) NOT NULL DEFAULT 1 COMMENT '1 = vitrin 2= vitrin değil',
  `urunDurum` tinyint(1) NOT NULL DEFAULT 1 COMMENT '1 = aktif 2 = pasif'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urun_adresler`
--

CREATE TABLE `urun_adresler` (
  `urun_adresID` int(10) UNSIGNED NOT NULL,
  `urun_adresBayi` varchar(250) NOT NULL,
  `urun_adresBaslik` varchar(250) NOT NULL,
  `urun_adresTarif` text NOT NULL,
  `urun_adresDurum` tinyint(1) NOT NULL DEFAULT 1,
  `urun_adresTarih` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urun_banka`
--

CREATE TABLE `urun_banka` (
  `urun_bankaID` int(11) UNSIGNED NOT NULL,
  `urun_bankaAdi` varchar(250) NOT NULL,
  `urun_bankaHesap` varchar(250) NOT NULL,
  `urun_bankaSube` varchar(250) NOT NULL,
  `urun_bankaIban` varchar(250) NOT NULL,
  `urun_bankaDurum` tinyint(1) NOT NULL DEFAULT 1,
  `urun_bankaEkleyen` int(11) NOT NULL,
  `urun_bankaTarih` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urun_bayiler`
--

CREATE TABLE `urun_bayiler` (
  `urun_bayiID` int(11) UNSIGNED NOT NULL,
  `urun_bayiKodu` varchar(250) NOT NULL,
  `urun_bayiAdi` varchar(250) NOT NULL,
  `urun_bayiEmail` varchar(250) NOT NULL,
  `urun_bayiSifre` varchar(250) NOT NULL,
  `urun_bayiDurum` tinyint(1) NOT NULL DEFAULT 0,
  `urun_bayiTarih` timestamp NOT NULL DEFAULT current_timestamp(),
  `urun_bayiLogo` varchar(250) DEFAULT NULL,
  `urun_bayiIndirim` tinyint(3) NOT NULL DEFAULT 0,
  `urun_bayiTelefon` varchar(50) NOT NULL,
  `urun_bayiFax` varchar(50) DEFAULT NULL,
  `urun_bayiVergino` varchar(200) NOT NULL,
  `urun_bayiVergiDairesi` varchar(250) NOT NULL,
  `urun_bayiSite` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urun_havale_bildirim`
--

CREATE TABLE `urun_havale_bildirim` (
  `urun_havaleID` int(10) UNSIGNED NOT NULL,
  `urun_havaleBayi` varchar(250) NOT NULL,
  `urun_havaleTarih` date NOT NULL,
  `urun_havaleSaat` date NOT NULL,
  `urun_havaleTutar` double(15,2) NOT NULL,
  `urun_havaleNot` text NOT NULL,
  `urun_havaleBanka` int(11) NOT NULL,
  `urun_havaleEklenme` timestamp NOT NULL DEFAULT current_timestamp(),
  `urun_havaleIP` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urun_kategoriler`
--

CREATE TABLE `urun_kategoriler` (
  `urun_kategoryID` int(11) NOT NULL,
  `urun_kategoryBaslik` varchar(250) NOT NULL,
  `urun_kategorySef` varchar(250) NOT NULL,
  `urun_kategoryKeyword` varchar(250) NOT NULL,
  `urun_kategoryDescription` varchar(250) NOT NULL,
  `urun_kategoryDurum` tinyint(1) NOT NULL DEFAULT 1,
  `urun_kategoryTarih` date NOT NULL DEFAULT current_timestamp(),
  `urun_kategoryEkleyen` int(11) NOT NULL,
  `urun_kategorySilinmeyen` tinyint(1) NOT NULL DEFAULT 2
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urun_ozellik`
--

CREATE TABLE `urun_ozellik` (
  `urun_ozellikID` int(11) NOT NULL,
  `urun_ozellikUrun` varchar(250) NOT NULL,
  `urun_ozellikBaslik` varchar(250) NOT NULL,
  `urun_ozellikIcerik` text NOT NULL,
  `urun_ozellikEkleyen` int(11) NOT NULL,
  `urun_ozellikTarih` date NOT NULL DEFAULT current_timestamp(),
  `urun_ozellikDurum` tinyint(4) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urun_resimler`
--

CREATE TABLE `urun_resimler` (
  `urun_resimlerID` int(11) NOT NULL,
  `urun_resimlerUrun` varchar(200) NOT NULL,
  `urun_resimlerDosya` varchar(250) NOT NULL,
  `urun_resimlerTarih` date NOT NULL DEFAULT current_timestamp(),
  `urun_resimlerEkleyen` int(11) NOT NULL,
  `urun_resimlerDurum` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urun_yorumlar`
--

CREATE TABLE `urun_yorumlar` (
  `urun_yorumID` int(11) UNSIGNED NOT NULL,
  `urun_yorumBayi` varchar(250) NOT NULL,
  `urun_yorumUrun` varchar(250) NOT NULL,
  `urun_yorumIsim` varchar(250) NOT NULL,
  `urun_yorumIcerik` text NOT NULL,
  `urun_yorumDurum` tinyint(1) NOT NULL DEFAULT 0 COMMENT '1 = aktif 0 = pasif',
  `urun_yorumIP` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `ayarlar`
--
ALTER TABLE `ayarlar`
  ADD PRIMARY KEY (`ayarlarIP`);

--
-- Tablo için indeksler `bayiloglari`
--
ALTER TABLE `bayiloglari`
  ADD PRIMARY KEY (`bayiloglariID`);

--
-- Tablo için indeksler `durumkodlari`
--
ALTER TABLE `durumkodlari`
  ADD PRIMARY KEY (`durumkodlariID`);

--
-- Tablo için indeksler `mesajlar`
--
ALTER TABLE `mesajlar`
  ADD PRIMARY KEY (`mesajID`);

--
-- Tablo için indeksler `sepet`
--
ALTER TABLE `sepet`
  ADD PRIMARY KEY (`sepetID`);

--
-- Tablo için indeksler `siparisler`
--
ALTER TABLE `siparisler`
  ADD PRIMARY KEY (`siparislerID`);

--
-- Tablo için indeksler `urunler`
--
ALTER TABLE `urunler`
  ADD PRIMARY KEY (`urunID`);

--
-- Tablo için indeksler `urun_adresler`
--
ALTER TABLE `urun_adresler`
  ADD PRIMARY KEY (`urun_adresID`);

--
-- Tablo için indeksler `urun_banka`
--
ALTER TABLE `urun_banka`
  ADD PRIMARY KEY (`urun_bankaID`);

--
-- Tablo için indeksler `urun_bayiler`
--
ALTER TABLE `urun_bayiler`
  ADD PRIMARY KEY (`urun_bayiID`);

--
-- Tablo için indeksler `urun_havale_bildirim`
--
ALTER TABLE `urun_havale_bildirim`
  ADD PRIMARY KEY (`urun_havaleID`);

--
-- Tablo için indeksler `urun_kategoriler`
--
ALTER TABLE `urun_kategoriler`
  ADD PRIMARY KEY (`urun_kategoryID`);

--
-- Tablo için indeksler `urun_ozellik`
--
ALTER TABLE `urun_ozellik`
  ADD PRIMARY KEY (`urun_ozellikID`);

--
-- Tablo için indeksler `urun_resimler`
--
ALTER TABLE `urun_resimler`
  ADD PRIMARY KEY (`urun_resimlerID`);

--
-- Tablo için indeksler `urun_yorumlar`
--
ALTER TABLE `urun_yorumlar`
  ADD PRIMARY KEY (`urun_yorumID`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `ayarlar`
--
ALTER TABLE `ayarlar`
  MODIFY `ayarlarIP` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `bayiloglari`
--
ALTER TABLE `bayiloglari`
  MODIFY `bayiloglariID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `durumkodlari`
--
ALTER TABLE `durumkodlari`
  MODIFY `durumkodlariID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `mesajlar`
--
ALTER TABLE `mesajlar`
  MODIFY `mesajID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `sepet`
--
ALTER TABLE `sepet`
  MODIFY `sepetID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `siparisler`
--
ALTER TABLE `siparisler`
  MODIFY `siparislerID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `urunler`
--
ALTER TABLE `urunler`
  MODIFY `urunID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `urun_adresler`
--
ALTER TABLE `urun_adresler`
  MODIFY `urun_adresID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `urun_banka`
--
ALTER TABLE `urun_banka`
  MODIFY `urun_bankaID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `urun_bayiler`
--
ALTER TABLE `urun_bayiler`
  MODIFY `urun_bayiID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `urun_havale_bildirim`
--
ALTER TABLE `urun_havale_bildirim`
  MODIFY `urun_havaleID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `urun_kategoriler`
--
ALTER TABLE `urun_kategoriler`
  MODIFY `urun_kategoryID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `urun_ozellik`
--
ALTER TABLE `urun_ozellik`
  MODIFY `urun_ozellikID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `urun_resimler`
--
ALTER TABLE `urun_resimler`
  MODIFY `urun_resimlerID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `urun_yorumlar`
--
ALTER TABLE `urun_yorumlar`
  MODIFY `urun_yorumID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
