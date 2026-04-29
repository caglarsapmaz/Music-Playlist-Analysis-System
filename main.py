#Çağlar SAPMAZ

import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
# 1. VERİ YAPISI VE CORE METODLAR
# ==========================================

def get_total_duration(songs):
    """Tüm şarkıların toplam süresini saniye cinsinden hesaplar."""
    total = 0
    for song in songs:
        total += song["duration"]
    return total

def get_most_played_song(songs):
    """En çok dinlenen şarkıyı bulur ve döndürür."""
    if not songs:
        return None
    return max(songs, key=lambda s: s["plays"])

def get_average_duration(songs):
    """Şarkıların ortalama süresini hesaplar."""
    if not songs:
        return 0
    total = get_total_duration(songs)
    return total / len(songs)

def print_playlist(songs):
    """Playlist'i konsola düzenli bir formatta yazdırır."""
    print("-" * 60)
    print(f"{'Şarkı Adı':<30} | {'Sanatçı':<15} | {'Süre (sn)':<9} | {'Dinlenme'}")
    print("-" * 60)
    for song in songs:
        print(f"{song['title']:<30} | {song['artist']:<15} | {song['duration']:<9} | {song['plays']}")
    print("-" * 60)

# --- BONUS METODLAR ---

def get_longest_song(songs):
    """Süresi en uzun olan şarkıyı bulur (Bonus)."""
    if not songs:
        return None
    return max(songs, key=lambda s: s["duration"])

def filter_by_artist(songs, artist_name):
    """Belirtilen sanatçının şarkılarını filtreler (Bonus)."""
    return [song for song in songs if song["artist"].lower() == artist_name.lower()]

def sort_by_plays(songs):
    """Şarkıları dinlenme sayısına göre çoktan aza sıralar (Bonus)."""
    return sorted(songs, key=lambda s: s["plays"], reverse=True)


# ==========================================
# 2. ARAYÜZ (GUI) TASARIMI
# ==========================================

class PlaylistApp:
    def __init__(self, root, songs):
        self.root = root
        self.songs = songs
        self.root.title("Music Playlist Analysis System")
        self.root.geometry("650x500")
        self.root.configure(bg="#121212")

        # Stil Ayarları
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                        background="#1E1E1E", foreground="#FFFFFF", 
                        fieldbackground="#1E1E1E", rowheight=30)
        style.map("Treeview", background=[("selected", "#1DB954")])
        style.configure("Treeview.Heading", 
                        background="#282828", foreground="#1DB954", font=('Arial', 10, 'bold'))

        # Başlık
        title_lbl = tk.Label(root, text="🎵 Music Playlist Analyzer", bg="#121212", fg="#1DB954", font=("Arial", 16, "bold"))
        title_lbl.pack(pady=10)

        # Tablo (Treeview)
        columns = ("title", "artist", "duration", "plays")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
        self.tree.heading("title", text="Şarkı Adı")
        self.tree.heading("artist", text="Sanatçı")
        self.tree.heading("duration", text="Süre (sn)")
        self.tree.heading("plays", text="Dinlenme")
        
        self.tree.column("title", width=220)
        self.tree.column("artist", width=120)
        self.tree.column("duration", width=100, anchor="center")
        self.tree.column("plays", width=100, anchor="center")
        self.tree.pack(pady=10, padx=20, fill="x")

        self.load_data(self.songs)

        # Buton Çerçevesi
        btn_frame = tk.Frame(root, bg="#121212")
        btn_frame.pack(pady=10)

        # Butonlar (macOS görünüm sorunu için bg ve fg kaldırıldı)
        btn_config = {"font": ("Arial", 10, "bold"), "width": 18}
        
        tk.Button(btn_frame, text="Analiz Raporu", command=self.show_analysis, **btn_config).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(btn_frame, text="Sırala (Dinlenme)", command=self.sort_data, **btn_config).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(btn_frame, text="En Uzun Şarkı", command=self.show_longest, **btn_config).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(btn_frame, text="Orijinal Listeyi Yükle", command=lambda: self.load_data(self.songs), **btn_config).grid(row=1, column=1, padx=10, pady=5)

    def load_data(self, data):
        """Tabloyu temizler ve verilen listeyi tabloya yükler."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for song in data:
            self.tree.insert("", "end", values=(song["title"], song["artist"], song["duration"], song["plays"]))

    def show_analysis(self):
        """Analiz metotlarını çalıştırıp sonucu ekranda gösterir."""
        total_dur = get_total_duration(self.songs)
        avg_dur = get_average_duration(self.songs)
        most_played = get_most_played_song(self.songs)

        report = (
            f"📊 GENEL ANALİZ\n\n"
            f"Toplam Süre: {total_dur} saniye\n"
            f"Ortalama Süre: {avg_dur:.2f} saniye\n\n"
            f"🏆 EN ÇOK DİNLENEN ŞARKI\n"
            f"Adı: {most_played['title']}\n"
            f"Sanatçı: {most_played['artist']}\n"
            f"Dinlenme: {most_played['plays']}"
        )
        messagebox.showinfo("Analiz Raporu", report)

    def sort_data(self):
        """Bonus: Şarkıları dinlenmeye göre sıralar ve tabloyu günceller."""
        sorted_songs = sort_by_plays(self.songs)
        self.load_data(sorted_songs)

    def show_longest(self):
        """Bonus: En uzun şarkıyı mesaj olarak gösterir."""
        longest = get_longest_song(self.songs)
        report = f"⏱ EN UZUN ŞARKI\n\nAdı: {longest['title']}\nSüre: {longest['duration']} saniye"
        messagebox.showinfo("En Uzun Şarkı", report)


# ==========================================
# 3. ANA FONKSİYON (MAIN)
# ==========================================

def main():
    """Programın başlangıç noktası. Şarkı listesini oluşturur ve metotları çağırır."""
    
    playlist = [
        {"title": "In Your Eyes - Radio Edit", "artist": "Inna", "duration": 197, "plays": 15000000},
        {"title": "I Don't Want to Be", "artist": "Gavin DeGraw", "duration": 217, "plays": 85000000},
        {"title": "G&V", "artist": "Ivan B", "duration": 194, "plays": 3500000},
        {"title": "No Role Modelz", "artist": "J. Cole", "duration": 293, "plays": 125000000},
        {"title": "The Monster", "artist": "Eminem", "duration": 250, "plays": 98000000}
    ]

    print("\n--- ZORUNLU METOD ÇIKTILARI (KONSOL) ---")
    print_playlist(playlist)
    
    print(f"\nToplam Süre: {get_total_duration(playlist)} saniye")
    print(f"Ortalama Süre: {get_average_duration(playlist):.2f} saniye")
    
    most_played = get_most_played_song(playlist)
    print(f"En Çok Dinlenen Şarkı: {most_played['title']} ({most_played['plays']} dinlenme)")

    print("\n--- BONUS METOD ÇIKTILARI ---")
    longest = get_longest_song(playlist)
    print(f"En Uzun Şarkı: {longest['title']} ({longest['duration']} sn)")
    
    eminem_songs = filter_by_artist(playlist, "Eminem")
    print(f"Eminem Şarkıları: {[s['title'] for s in eminem_songs]}")

    print("\n[Bilgi] Arayüz başlatılıyor. Lütfen açılan pencereye geçin...\n")

    root = tk.Tk()
    app = PlaylistApp(root, playlist)
    root.mainloop()

if __name__ == "__main__":
    main()