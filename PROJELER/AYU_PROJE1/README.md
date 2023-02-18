# Web Tabanlı Hastane Randevu Sistemi

- 1 -- Bu projeyi çalıştırmak için localhost hizmeti sunan xampp, wampserver gibi server yazılımının bilgisayarınızda yüklü olması lazım.
- 2 -- Projede database olarak MySql kullandığım için database kullanıcı adı ve şifresini bu database serverına göre yazdım. Bu yüzden [phpmyadmin](http://localhost/phpmyadmin/) admin panelini kullanabilirsiniz. 
- 3 -- phpmyadmin sayfasına gittiğinizde ayu_proje1 adında bir veritabanı oluşturduktan sonra, [İçe Aktar](http://localhost/phpmyadmin/index.php?route=/server/import) linkine giderek AYU_PROJE1 klasörü içinde bulunan ayu_proje1.sql isimli veritabanı dosyasını import etmeniz lazım.
- 4 -- C:\xampp\htdocs dizinine AYU_PROJE1 isminde proje klasörünü ekleyin
- 5 -- projenin anasayfasına [Hastane Randevu sistemi](http://localhost/AYU_PROJE1/) gidip ziyaret edebilirsiniz.


### Bu programın 3 tane kullanıcı türü vardır
### Tüm kullanıcı türleri için aynı pencereden giriş yapılır 
### Giriş yapıldıktan sonra Model/login tarafında, hangi kullanıcı türü giriş yaptıysa ilgili kullanıcı türünün Anasayfasına yönlendirilir

## admin 
- tc kimlik no : 45145145199
- şifre : 111


## doctor 1
- tc kimlik no : 14914914933
- şifre : 14914914933   // doktor ilk defa eklendiğinde şifre tc numarasıdır

## doctor 2
- tc kimlik no : 14214214233
- şifre : 14214214233

## hasta 1 
- tc kimlik no : 11111111111
- şifre : 111

## hasta 2 
- tc kimlik no : 22222222222
- şifre : 111