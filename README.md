# Music Playlist Analysis System

## Proje Amacı
Bu proje, bir müzik çalma listesini analiz etmek için Python kullanılarak geliştirilmiş bir uygulamadır. Öğrencilerin temel Python veri yapıları (liste, sözlük) ve fonksiyon (metot) tanımlama becerilerini ölçmeyi hedeflemektedir. Konsol çıktısına ek olarak kullanıcı dostu bir grafiksel arayüz (GUI) sunmaktadır.

## Metot Açıklamaları
Projede istenen zorunlu ve bonus metotlar eksiksiz olarak kodlanmıştır:

* **Zorunlu Metotlar:**
  * `get_total_duration(songs)`: Listedeki tüm şarkıların saniye cinsinden toplam süresini toplar ve döndürür.
  * `get_most_played_song(songs)`: Dinlenme sayısı (`plays`) değerine bakarak en yüksek olan şarkı sözlüğünü bulur.
  * `get_average_duration(songs)`: Toplam süreyi şarkı sayısına bölerek ortalama şarkı süresini hesaplar.
  * `print_playlist(songs)`: Çalma listesini konsol üzerinde okunabilir bir tablo halinde düzenli şekilde yazdırır.
  * `main()`: En az 5 şarkılık veri yapısını oluşturur, tüm analitik metotları çağırır ve görsel arayüzü başlatır.

* **Bonus Metotlar:**
  * `get_longest_song(songs)`: Listedeki süresi (`duration`) en uzun olan şarkıyı bulur.
  * `filter_by_artist(songs, artist)`: Gönderilen sanatçı ismine sahip tüm şarkıları filtreleyip yeni bir liste döndürür.
  * `sort_by_plays(songs)`: Şarkıları dinlenme sayılarına göre çoktan aza doğru sıralar.

## Çalıştırma Bilgisi
1. Bilgisayarınızda Python'ın yüklü olduğundan emin olun. (Sürüm 3.x önerilir).
2. Terminal veya komut satırını açın.
3. Proje dizinine gidin.
4. `python main.py` komutunu çalıştırın.
5. İlk olarak zorunlu ve bonus çıktıları konsolda göreceksiniz. Ardından analizleri görsel olarak inceleyebileceğiniz Tkinter masaüstü arayüzü açılacaktır. (Ek bir kütüphane kurulumuna gerek yoktur, Tkinter Python ile gömülü gelmektedir).