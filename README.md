# 💕 Valentine's Day Adventure - Website Interactive 💕

**Sebuah website romantis interaktif untuk Valentine's Day 2026**

Hadiah digital yang sempurna untuk pacar Anda! Website ini simple, cantik, dan mudah di-customize.

## 🚀 Quick Start (1 Menit!)

1. **Double-click:** `index.html`
2. **Browser opens:** Website muncul! 🎊
3. **Enjoy:** Semua halaman interaktif dengan animasi smooth
     - Quote motivasi: *"Love is the bridge between two hearts, and you are mine."*
   - **Animasi**:
     - ❤️ Hati jatuh dari atas ke bawah (efek salju)
     - Hati bergerak dengan sinusoidal motion
   - **Tombol**:
     - 💚 **YES**: Transisi ke halaman foto
     - ❌ **NO**: Pesan lucu "Love is patient! Coba lagi ya?"
   - **Tema**: Pink muda (#FFB6C1) dengan aksen merah Valentine

### 2. **Halaman Photo Page** 📸
   - **Placeholder**: Hati vector berbentuk love symbol
   - **Pesan**: "Foto Kenangan Valentine akan muncul di sini"
   - **Tombol**: "💕 Lanjut ke Surat Cinta 💕"
   - **Design**: Elegant dengan border hati merah

### 3. **Halaman Surat Cinta** 💌
   - **Layout**: Two-column design
     - **Kiri**: Isi surat romantis dalam bahasa Indonesia
     - **Kanan**: Animasi pohon bunga dengan animasi floating hearts
   
   - **Konten Surat**:
     ```
     Quote (English): "Love is not about how many days, 
                       but how much you love each other." — Unknown
     
     Isi (Indonesia): Kata-kata romantis yang menyentuh hati
     ```
   
   - **Design Pohon Bunga Animasi**:
     - Pohon dengan batang cokelat
     - 7 bunga merah dengan kelopak bentuk lingkaran
     - Pusat bunga berwarna emas
     - Daun hijau di samping
   
   - **Kotak Foto Kenangan**:
     - 4 kotak dengan frame pink
     - Label: "Foto 1", "Foto 2", "Foto 3", "Foto 4"
     - Tema: Bingkai hati
   
   - **Envelope Effect**:
     - Animasi surat slide up dari bawah
     - Durasi: ~1 detik
   
   - **Tombol**: "❤️ Happy Valentine's Day! ❤️"

### 4. **Halaman Akhir - Ending** 🎊
   - **Background**: Merah Valentine (#FF1493)
   - **Konten**:
     - Pesan terima kasih romantis
     - Quote terakhir: *"I Love You More Than Words Can Say ❤️"*
   - **Animasi**:
     - Hati melayang ke atas dengan gerakan smooth
     - Interval acak
   - **Tombol**: "Tutup Aplikasi"

## 🎨 Palet Warna Valentine

| Warna | Kode Hex | Penggunaan |
|-------|----------|-----------|
| Light Pink | #FFB6C1 | Background utama |
| Medium Pink | #FFB0D4 | Accent elements |
| Deep Pink | #FF1493 | Tombol "Yes", text penting |
| Dark Red | #C41E3A | Title, dark accents |
| Light Red | #FF6B7A | Tombol alternative |
| Cream White | #FFF8DC | Placeholder text, letter background |
| Gold | #FFD700 | Pusat bunga, divider |

## 📦 Requirements

Aplikasi ini **hanya membutuhkan Tkinter** yang sudah built-in dengan Python. Tidak perlu install library tambahan!

```bash
# Tkinter adalah bagian dari Python standard library
# Tidak ada yang perlu di-install khusus!
```

## 🚀 Cara Menjalankan

### **Opsi 1: Direct Run (Recommended)**

```bash
cd "d:\valentine vaniaa"
python valentine_app.py
```

### **Opsi 2: Dari Terminal VS Code**

1. Buka folder `d:\valentine vaniaa` di VS Code
2. Klik kanan pada `valentine_app.py`
3. Pilih "Run Python File in Terminal"

### **Opsi 3: Double Click (Windows)**

1. Buat file `run.bat` dengan isi:
```batch
cd /d "d:\valentine vaniaa"
python valentine_app.py
pause
```
2. Double-click file `run.bat`

## 🎮 Cara Menggunakan Aplikasi

### **Halaman 1: Welcome**
1. Baca pesan romantis
2. Perhatikan animasi hati jatuh ❤️
3. Klik **YES** untuk lanjut (atau klik **NO** untuk joke message)

### **Halaman 2: Foto Page**
1. Lihat placeholder foto berbentuk hati ❤️
2. Klik tombol **Lanjut ke Surat Cinta**

### **Halaman 3: Surat Cinta**
1. Baca surat romantis di sisi kiri
2. Lihat animasi pohon bunga di sisi kanan 🌹
3. Lihat 4 kotak untuk foto kenangan
4. Klik **Happy Valentine's Day!** untuk selesai

### **Halaman 4: Ending**
1. Baca pesan akhir yang romantis
2. Observe animasi hati melayang ❤️
3. Klik **Tutup Aplikasi** untuk keluar

## 🔧 Customization

### **Mengubah Warna**
Edit variabel di bagian atas file `valentine_app.py`:
```python
PINK_LIGHT = "#FFB6C1"      # Ubah warna pink
RED_VALENTINE = "#FF1493"   # Ubah warna merah
```

### **Mengubah Font**
```python
self.font_title = font.Font(family="Arial", size=32, weight="bold")
# Ubah "Arial" dengan font lain: "Georgia", "Times New Roman", dll.
# Ubah "32" untuk size lebih besar/kecil
```

### **Mengubah Teks Pesan**
Cari function `show_welcome_page()`, `show_letter_page()`, etc. dan edit teks sesuai keinginan.

### **Mengubah Ukuran Window**
```python
self.root.geometry("1000x700")  # Ubah width x height
```

## 💡 Tips & Tricks

1. **Multiple Monitors**: Aplikasi akan terbuka di tengah layar utama
2. **Full Screen Mode**: Edit untuk membuat fullscreen (hapus `self.root.resizable(False, False)`)
3. **Sound**: Bisa ditambah dengan library `playsound` untuk sound effect
4. **Photo Integration**: Modifikasi `draw_heart_placeholder()` untuk load actual images

## 🎯 Alur Program

```
START
  ↓
[Halaman 1: Welcome] → Click YES
  ↓
[Animasi Hati Jatuh]
  ↓
[Halaman 2: Photo Page]
  ↓
[Click Lanjut]
  ↓
[Halaman 3: Surat Cinta] ← Main Content
  ↓ (Animasi Slide-Up)
[Pohon Bunga Animasi] + [Photo Boxes]
  ↓
[Click Happy Valentine's Day]
  ↓
[Halaman 4: Ending]
  ↓
[Animasi Hati Melayang]
  ↓
[Click Tutup] → EXIT
```

## 🐛 Troubleshooting

### **Aplikasi tidak muncul**
- Pastikan Python path benar
- Coba: `python valentine_app.py` dari terminal

### **Font tidak muncul dengan benar**
- Edit `self.font_title` dengan font yang tersedia (Arial sudah universal)

### **Animasi lambat**
- Reduce animation frequency di `after()` calls
- Contoh: `self.root.after(800, ...)` menjadi `self.root.after(500, ...)`

### **Window terbuka di layar tidak tepat**
- Hapus atau comment `self.center_window()` function

## 📝 Code Structure

```
valentine_app.py
├── Configuration Section
│   ├── Color Palette (PINK_LIGHT, RED_VALENTINE, etc.)
├── Main Class: ValentineApp
│   ├── __init__() → Initialize app
│   ├── Utility Functions
│   │   ├── center_window()
│   │   ├── clear_window()
│   ├── Page 1: show_welcome_page()
│   │   ├── animate_falling_hearts()
│   │   ├── animate_heart_fall()
│   ├── Page 2: show_photo_page()
│   │   ├── draw_heart_placeholder()
│   ├── Page 3: show_letter_page()
│   │   ├── create_photo_box()
│   │   ├── draw_flower_tree()
│   │   ├── animate_letter_slide_up()
│   ├── Page 4: show_ending()
│   │   ├── animate_ending_hearts()
│   │   ├── animate_floating_heart()
└── Main: if __name__ == "__main__"
```

## 🎁 Fitur Bonus yang Bisa Ditambah

1. **Background Music**: Gunakan `pygame` untuk musik Valentine
2. **Custom Names**: Popup input untuk nama couple
3. **Photo Upload**: Integration dengan file dialog
4. **Particle Effects**: Lebih banyak animasi
5. **Themes**: Dark mode, light mode, custom theme
6. **Export**: Save session as PDF/image

## 💕 Special Notes

- **Semua quotes dalam Bahasa Inggris** (authentic & romantic)
- **Narasi utama dalam Bahasa Indonesia** (personal & relatable)
- **Mix bahasa yang natural** di UI elements
- **Font dipilih dengan hati-hati** untuk aesthetic maksimal
- **Animasi smooth** untuk pengalaman yang menyenangkan

## 📄 License

Kode ini dibuat dengan cinta ❤️ untuk Valentine's Day 2026!

---

**Dibuat dengan ❤️ untuk orang yang berharga!**

Selamat merayakan Valentine's Day! 💕🌹✨
