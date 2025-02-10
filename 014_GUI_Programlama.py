# Python'da GUI Programlama (Tkinter)
# ==============================

"""
GUI (GRAPHICAL USER INTERFACE) NEDİR?
---------------------------------
GUI, kullanıcıların grafiksel öğeler (butonlar, menüler, formlar vb.) 
aracılığıyla programla etkileşime girmesini sağlayan arayüzdür.

Tkinter:
- Python'un standart GUI kütüphanesidir
- Platformlar arası çalışır (Windows, macOS, Linux)
- Hafif ve kullanımı kolaydır
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json

class NotUygulamasi:
    """Basit bir not tutma uygulaması."""
    
    def __init__(self):
        # Ana pencere oluşturma
        self.pencere = tk.Tk()
        self.pencere.title("Not Defteri Uygulaması")
        self.pencere.geometry("600x400")
        
        # Stil ayarları
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6)
        self.style.configure("TLabel", padding=6)
        
        # Notları tutacak liste
        self.notlar = []
        
        # Arayüz öğelerini oluştur
        self.arayuz_olustur()
        
        # Varsa önceki notları yükle
        self.notlari_yukle()
    
    def arayuz_olustur(self):
        """Arayüz öğelerini oluşturur ve yerleştirir."""
        # Üst frame - Not ekleme alanı
        ust_frame = ttk.Frame(self.pencere, padding="10")
        ust_frame.pack(fill=tk.X)
        
        # Not başlığı
        ttk.Label(ust_frame, text="Başlık:").pack(side=tk.LEFT)
        self.baslik_giris = ttk.Entry(ust_frame, width=40)
        self.baslik_giris.pack(side=tk.LEFT, padx=5)
        
        # Not içeriği
        orta_frame = ttk.Frame(self.pencere, padding="10")
        orta_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(orta_frame, text="İçerik:").pack(anchor=tk.W)
        self.icerik_giris = tk.Text(orta_frame, height=10)
        self.icerik_giris.pack(fill=tk.BOTH, expand=True)
        
        # Butonlar
        buton_frame = ttk.Frame(self.pencere, padding="10")
        buton_frame.pack(fill=tk.X)
        
        ttk.Button(
            buton_frame, 
            text="Not Ekle", 
            command=self.not_ekle
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            buton_frame, 
            text="Seçili Notu Sil", 
            command=self.not_sil
        ).pack(side=tk.LEFT, padx=5)
        
        # Not listesi
        liste_frame = ttk.Frame(self.pencere, padding="10")
        liste_frame.pack(fill=tk.BOTH, expand=True)
        
        # Treeview (tablo görünümü) oluşturma
        self.tablo = ttk.Treeview(
            liste_frame, 
            columns=("Başlık", "Tarih"),
            show="headings"
        )
        
        # Sütun başlıkları
        self.tablo.heading("Başlık", text="Başlık")
        self.tablo.heading("Tarih", text="Tarih")
        
        # Sütun genişlikleri
        self.tablo.column("Başlık", width=200)
        self.tablo.column("Tarih", width=100)
        
        # Scrollbar ekleme
        scrollbar = ttk.Scrollbar(
            liste_frame, 
            orient=tk.VERTICAL, 
            command=self.tablo.yview
        )
        self.tablo.configure(yscrollcommand=scrollbar.set)
        
        # Tablo ve scrollbar'ı yerleştirme
        self.tablo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Tablo seçim olayını bağlama
        self.tablo.bind("<<TreeviewSelect>>", self.not_goster)
    
    def not_ekle(self):
        """Yeni not ekler."""
        baslik = self.baslik_giris.get().strip()
        icerik = self.icerik_giris.get("1.0", tk.END).strip()
        
        if not baslik or not icerik:
            messagebox.showwarning(
                "Uyarı",
                "Başlık ve içerik alanları boş bırakılamaz!"
            )
            return
        
        # Yeni notu oluştur
        yeni_not = {
            "baslik": baslik,
            "icerik": icerik,
            "tarih": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        # Nota ekle ve kaydet
        self.notlar.append(yeni_not)
        self.notlari_kaydet()
        
        # Tabloya ekle
        self.tablo.insert(
            "", 
            tk.END, 
            values=(yeni_not["baslik"], yeni_not["tarih"])
        )
        
        # Giriş alanlarını temizle
        self.baslik_giris.delete(0, tk.END)
        self.icerik_giris.delete("1.0", tk.END)
        
        messagebox.showinfo("Bilgi", "Not başarıyla eklendi!")
    
    def not_sil(self):
        """Seçili notu siler."""
        secili = self.tablo.selection()
        if not secili:
            messagebox.showwarning("Uyarı", "Lütfen silinecek notu seçin!")
            return
        
        if messagebox.askyesno("Onay", "Seçili notu silmek istediğinize emin misiniz?"):
            # Tablodan seçili öğeyi al
            item = self.tablo.item(secili[0])
            baslik = item["values"][0]
            
            # Notlar listesinden sil
            self.notlar = [
                not_ for not_ in self.notlar 
                if not_["baslik"] != baslik
            ]
            
            # Tablodan sil
            self.tablo.delete(secili[0])
            
            # Değişiklikleri kaydet
            self.notlari_kaydet()
            
            # Giriş alanlarını temizle
            self.baslik_giris.delete(0, tk.END)
            self.icerik_giris.delete("1.0", tk.END)
            
            messagebox.showinfo("Bilgi", "Not başarıyla silindi!")
    
    def not_goster(self, event):
        """Seçili notun detaylarını gösterir."""
        secili = self.tablo.selection()
        if not secili:
            return
        
        # Tablodan seçili öğeyi al
        item = self.tablo.item(secili[0])
        baslik = item["values"][0]
        
        # Notu bul
        for not_ in self.notlar:
            if not_["baslik"] == baslik:
                # Giriş alanlarını doldur
                self.baslik_giris.delete(0, tk.END)
                self.baslik_giris.insert(0, not_["baslik"])
                
                self.icerik_giris.delete("1.0", tk.END)
                self.icerik_giris.insert("1.0", not_["icerik"])
                break
    
    def notlari_kaydet(self):
        """Notları JSON dosyasına kaydeder."""
        try:
            with open("notlar.json", "w", encoding="utf-8") as f:
                json.dump(self.notlar, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Hata", f"Notlar kaydedilirken hata oluştu: {e}")
    
    def notlari_yukle(self):
        """Notları JSON dosyasından yükler."""
        try:
            with open("notlar.json", "r", encoding="utf-8") as f:
                self.notlar = json.load(f)
                
                # Notları tabloya ekle
                for not_ in self.notlar:
                    self.tablo.insert(
                        "", 
                        tk.END, 
                        values=(not_["baslik"], not_["tarih"])
                    )
        except FileNotFoundError:
            # Dosya yoksa boş liste ile devam et
            pass
        except Exception as e:
            messagebox.showerror("Hata", f"Notlar yüklenirken hata oluştu: {e}")
    
    def calistir(self):
        """Uygulamayı başlatır."""
        self.pencere.mainloop()

"""
GUI PROGRAMLAMA İPUÇLARI
----------------------
1. Kullanıcı dostu arayüz tasarlayın
2. Hata mesajlarını anlaşılır yapın
3. Klavye kısayolları ekleyin
4. Doğrulama kontrolleri yapın
5. Yardım menüsü ekleyin

TASARIM İPUÇLARI
--------------
1. Widget'ları mantıklı gruplandırın
2. Yeterli boşluk bırakın
3. Renk ve font seçimine dikkat edin
4. Tutarlı bir tasarım kullanın
5. Platform standartlarına uyun

PERFORMANS İPUÇLARI
----------------
1. Ağır işlemleri arka planda yapın
2. Gereksiz widget güncellemelerinden kaçının
3. Bellek yönetimine dikkat edin
4. Büyük veriler için sayfalama kullanın
5. Düzenli temizlik yapın
"""

if __name__ == "__main__":
    # Uygulamayı başlat
    uygulama = NotUygulamasi()
    uygulama.calistir() 