# 🎵 Music Playlist Analysis System

Bu proje, bir müzik çalma listesini hem terminal üzerinden analiz eden hem de kullanıcı dostu bir arayüz (GUI) ile yönetilmesini sağlayan kapsamlı bir Python uygulamasıdır.

## 👤 Geliştirici
**Çağlar SAPMAZ** tarafından yapay zekadan destek alınarak geliştirilmiştir.

---

## 🚀 Öne Çıkan Özellikler

Uygulama, veri işleme ve görselleştirme konularında iki farklı katman sunar:

### 🧠 Core (Temel) Analiz Yetenekleri
* **Toplam Süre Hesaplama:** Listede bulunan tüm şarkıların toplam uzunluğunu saniye bazında hesaplar.
* **Popülerlik Analizi:** Dinlenme sayılarına göre en popüler şarkıyı anında tespit eder.
* **İstatistiksel Ortalama:** Şarkıların ortalama sürelerini bularak listenin genel temposunu analiz eder.
* **Terminal Raporlama:** Verileri konsol ekranında düzenli tablolar halinde yazdırır.

### 🌟 Bonus Fonksiyonlar
* **Zamanın Devi:** Listenin süresi en uzun olan şarkısını belirler.
* **Sanatçı Filtresi:** Belirli bir sanatçıya ait eserleri listeden ayıklar.
* **Akıllı Sıralama:** Şarkıları en çok dinlenenden en aza doğru dinamik olarak sıralar.

---

## 🎨 Kullanıcı Arayüzü (GUI)

Modern bir **Dark Mode** temasıyla tasarlanan arayüz şu özellikleri içerir:

* **Spotify Estetiği:** Koyu arka plan (#121212) ve canlı yeşil (#1DB954) detaylarla şık bir görünüm.
* **İnteraktif Tablo:** Tüm şarkı bilgilerini içeren etkileşimli bir `Treeview` yapısı.
* **Hızlı Erişim Butonları:**
    * 📊 **Analiz Raporu:** Genel istatistikleri bir popup penceresinde gösterir.
    * 📶 **Sırala:** Tabloyu dinlenme sayısına göre anlık olarak günceller.
    * ⏱ **En Uzun Şarkı:** En uzun parçayı hızlıca raporlar.
    * 🔄 **Sıfırla:** Yapılan filtreleri temizleyerek orijinal listeyi geri yükler.

---

## 🛠 Teknik Detaylar

* **Dil:** Python 
* **Arayüz Kütüphanesi:** `tkinter` & `ttk`
* **Tema:** Clam (Customized Dark Theme)

### Dahili Şarkı Listesi
Uygulama içerisinde örnek olarak şu sanatçıların verileri bulunmaktadır:
* Inna
* Gavin DeGraw
* Ivan B
* J. Cole
* Eminem

---

## 🖥 Kurulum ve Çalıştırma

1.  Bilgisayarınızda Python yüklü olduğundan emin olun.
2.  Depoyu klonlayın veya `main.py` dosyasını indirin.
3.  Terminal üzerinden uygulamayı başlatın:
    ```bash
    python main.py
    ```

---
🎧 *Müzik verilerinizi analiz etmek hiç bu kadar şık olmamıştı!*
