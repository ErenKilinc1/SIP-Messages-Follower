# Cisco CUBE SIP Messages Follower

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Cisco](https://img.shields.io/badge/Cisco-CUBE%20%2F%20IOS--XE-orange?style=flat-square&logo=cisco)
![Protocol](https://img.shields.io/badge/Protocol-SIP-green?style=flat-square)
![Library](https://img.shields.io/badge/Library-Paramiko-red?style=flat-square)

Cisco Unified Border Element (CUBE) gateway cihazları üzerinde akan yoğun SIP trafiğini, sadece ilgilendiğiniz telefon numaralarına göre filtreleyerek gerçek zamanlı izlemenizi sağlayan bir ağ analiz aracıdır.

Cisco CUBE üzerindeki çalışmalarda en büyük zorluklardan biri, eşzamanlı yüzlerce çağrının aktığı yoğun trafikli bir gateway cihazında belirli bir çağrıya ait SIP sinyalleşmesini izlemektir.

`debug ccsip messages` komutu çalıştırıldığında, tüm çağrılara ait paketler aynı anda ekrana akar. Bu durum, bacaklar arasındaki geçişleri takip etmeyi ve hata ayıklamayı oldukça zorlaştırır.

Ayrıca, CUBE üzerindeki yerleşik filtreleme özellikleri her zaman beklenen hassasiyette çalışmayabilir veya konfigürasyonu karmaşık olabilir.

Bu Python aracı, karmaşık debug çıktılarını gerçek zamanlı olarak tarar ve sadece sizin belirlediğiniz telefon numaralarını içeren paketleri ayıklayarak sunar. Böylece, binlerce satırlık log gürültüsünden kurtulup sadece aradığınız çağrıya odaklanabilirsiniz.
  

## Gereksinimler
Bu projenin çalışması için sisteminizde aşağıdaki bileşenlerin yüklü olması gerekir:

* **Python:** v3.8 veya daha yeni bir sürüm.
* **SSH Erişimi:** Hedef Cisco Router'a SSH üzerinden erişim yetkisi ve `privilege level 15` yetkisi.
* **Bağımlılıklar:** SSH motoru olarak `paramiko` kütüphanesi kullanılır.

## Kütüphaneleri Yükleyin
Proje, SSH bağlantısı için `paramiko` kütüphanesini kullanır.

`pip install -r requirements.txt`

## Kullanım
`SIP_messages_follower.py` dosyasını açarak konfigürasyon değişkenlerini düzenleyin:

* `ROUTER_IP`: CUBE IP adresi.
* `USERNAME` / `PASSWORD`: SSH giriş bilgileri.

* `ARANAN_NO` / `ARAYAN_NO`: Takip etmek istediğiniz telefon numaraları.



