-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 23 Kas 2022, 21:52:44
-- Sunucu sürümü: 10.4.22-MariaDB
-- PHP Sürümü: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `abc-kurs`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `siparis`
--

CREATE TABLE `siparis` (
  `id` int(11) NOT NULL,
  `sip_name` varchar(50) NOT NULL,
  `sip_mail` varchar(50) NOT NULL,
  `sip_tel` varchar(11) NOT NULL,
  `sip_teslim_tarihi` date NOT NULL,
  `sip_ucret` int(11) NOT NULL,
  `sip_baslik` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `siparis`
--

INSERT INTO `siparis` (`id`, `sip_name`, `sip_mail`, `sip_tel`, `sip_teslim_tarihi`, `sip_ucret`, `sip_baslik`) VALUES
(1, 'sinan şimşek', 'eemsinan.73@gmail.com', '5444494263', '2022-10-31', 5000, 'e-ticaret'),
(3, 'baran', 'baran@gmail.com', '54444449426', '2022-11-27', 10000, 'mobil uygulama'),
(4, 'emine şimşek', 'emine@gmail.com', '5444494263', '2022-12-21', 2500, 'el işi örgüler'),
(5, 'baran şiğmşek', 'brn@gmail.com', '54444494263', '2022-11-09', 6000, 'veri tabanı');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `siparis`
--
ALTER TABLE `siparis`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `siparis`
--
ALTER TABLE `siparis`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
