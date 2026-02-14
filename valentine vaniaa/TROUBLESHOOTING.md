# 🆘 Troubleshooting & FAQ Guide

## ⚡ Quick Fixes (Try These First!)

### **Aplikasi tidak muncul**
```
1. Pastikan sudah di folder yang benar:
   cd "d:\valentine vaniaa"

2. Cek Python terinstall:
   python --version

3. Run ulang:
   python valentine_app.py

4. Jika masih tidak muncul, cek error:
   python valentine_app.py 2>&1 > error.txt
   (Buka file error.txt untuk lihat error message)
```

### **Font tidak cantik**
```
Di valentine_app.py, cari:
self.font_title = font.Font(family="Arial", size=32, weight="bold")

Ganti "Arial" dengan:
- "Georgia"           (Elegant)
- "Segoe UI"         (Modern)
- "Times New Roman"  (Classic)
- "Calibri"          (Professional)
```

### **Animasi lambat/lag**
```
Di animate_heart_fall(), ubah:
self.root.after(30, ...)  → self.root.after(20, ...)  (faster)

Atau kurangi frekuensi hati baru:
self.root.after(800, ...)  → self.root.after(1200, ...)
```

### **Window tidak centered**
```
Comment line ini di __init__:
# self.center_window()
```

### **Button tidak responsive**
```
Pastikan tidak ada infinite loop atau heavy computation
Cek function onYesClicked() dan onNoClicked()
```

---

## ❓ FAQ (Frequently Asked Questions)

### **Q1: Aplikasi butuh di-install dulu?**
```
❌ TIDAK! 
Cukup punya Python 3.7+
Tkinter sudah built-in, tidak perlu pip install
Langsung jalankan: python valentine_app.py
```

### **Q2: Bisa jalan di Mac/Linux?**
```
✅ YA!
Kode ini pure Python + Tkinter (cross-platform)

Mac:
python3 valentine_app.py

Linux (Ubuntu/Debian):
sudo apt-get install python3-tk
python3 valentine_app.py
```

### **Q3: Bisa unlock animasi lebih smooth?**
```
✅ YA!
Ubah animation intervals yang lebih kecil:

# Di animate_falling_hearts():
self.root.after(500, ...)  # Update 2x lebih sering

# Di animate_heart_fall():
self.root.after(15, ...)   # Smooth rendering

# Decrease frame duration untuk smooth animasi
```

### **Q4: Gimana cara tambah foto asli?**
```
✅ BISA (Butuh modifikasi):

Tambah library Pillow:
pip install Pillow

Kemudian di show_photo_page(), modifikan draw_heart_placeholder():

from PIL import Image, ImageTk

# Load image
image = Image.open("path/to/image.png")
image = image.resize((200, 200), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Display di canvas
canvas.create_image(500, 200, image=photo)
canvas.image = photo  # Keep reference!
```

### **Q5: Bisa tambah sound/musik?**
```
✅ BISA (Butuh modifikasi):

Install pygame:
pip install pygame

Tambah di show_welcome_page():
import pygame
pygame.mixer.init()
pygame.mixer.music.load("path/to/music.mp3")
pygame.mixer.music.play()

Atau pakai winsound (Windows only):
import winsound
winsound.Beep(1000, 500)  # Frequency, Duration
```

### **Q6: Gimana share ke orang lain?**
```
✅ CARA:

Opsi 1 - Share file .py (mereka perlu Python):
1. Kirim valentine_app.py
2. Mereka run: python valentine_app.py

Opsi 2 - Share executable (Windows):
1. Install pyinstaller:
   pip install pyinstaller

2. Create exe:
   pyinstaller --onefile valentine_app.py

3. Ambil file dari folder 'dist/'
4. Kirim ke orang lain (no Python needed!)

Opsi 3 - Create installer:
1. Install py2exe atau nuitka
2. Build dengan setup.py
3. Share installer
```

### **Q7: Bisa ubah nama pacar di aplikasi?**
```
✅ BISA!

Method 1 - Hard code (simple):
Di show_letter_page(), ubah:
Dear [Nama],
Menjadi:
Dear Nama Pacar Ku,

Method 2 - Dynamic (lebih bagus):
Di __init__:
self.couple_name = "Your Lover's Name"

Di show_letter_page():
letter_text = f"""Dear {self.couple_name},
Isi surat...
"""
```

### **Q8: Gimana kalo mau multiple pages berbeda?**
```
✅ BISA!

Template untuk page baru:
def show_custom_page(self):
    self.clear_window()
    self.current_page = "custom"
    
    main_frame = tk.Frame(self.root, bg=PINK_LIGHT)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Add your content here
    
    # Button untuk lanjut:
    next_btn = tk.Button(..., command=self.show_letter_page)

# Debug dengan: print(self.current_page)
```

### **Q9: Gimana backup aplikasi?**
```
✅ CARA TERMUDAH:

# Windows Command Prompt:
copy valentine_app.py valentine_app_backup.py

# Atau pakai folder struktur:
- valentine_app/
  ├─ valentine_app.py (active)
  ├─ valentine_app_v1.py (backup)
  ├─ valentine_app_v2.py (backup)
  └─ valentine_app_latest.py (latest)
```

### **Q10: Error "module not found"?**
```
❌ MASALAH:
"ModuleNotFoundError: No module named 'tkinter'"

✅ SOLUSI:

Windows:
- Reinstall Python
- Pilih "tcl/tk and IDLE" saat install
- Atau jalankan: python -m pip install tk

Mac:
- brew install python-tk
- atau: sudo apt-get install python3-tk

Linux:
- sudo apt-get install python3-tk
- Ubuntu: python3 -m pip install tk
```

---

## 🐛 Common Errors & Solutions

### **Error 1: "ImportError: No module named tkinter"**
```
Windows:
1. Buka Control Panel
2. Programs > Programs and Features
3. Cari Python
4. Click "Modify"
5. Pilih "Modify"
6. Centang "tcl/tk and IDLE"
7. Next > Install

Or reinstall:
python -m pip install tk
```

### **Error 2: "tkinter._tkinter.TclError: invalid command"**
```
Biasanya karena widget deleted saat masih di-reference.

Solusi: Check bahwa current_page benar sebelum update:

if self.current_page != "welcome":
    return  # Exit function
```

### **Error 3: Aplikasi freeze/hang**
```
Cause: Infinite loop atau heavy operation di main thread

Solusi: Gunakan after() untuk async operations:

# ❌ WRONG (freeze aplikasi):
while True:
    animate_stuff()
    time.sleep(0.1)

# ✅ RIGHT (smooth):
def animate(self):
    animate_stuff()
    self.root.after(100, self.animate)
```

### **Error 4: Window tidak ter-close dengan benar**
```
Solusi: Pastikan close button call root.quit():

def on_close(self):
    self.root.quit()  # atau self.root.destroy()

# Di root initialization:
self.root.protocol("WM_DELETE_WINDOW", self.on_close)
```

### **Error 5: Font terlihat aneh/besar/kecil**
```
Solusi 1: Ubah font family:
self.font_title = font.Font(family="Segoe UI", size=32)

Solusi 2: Ubah size:
self.font_title = font.Font(family="Arial", size=24)  # Lebih kecil

Solusi 3: Ubah weight:
self.font_title = font.Font(family="Arial", size=32, weight="normal")
```

### **Error 6: Animasi hati tidak terlihat**
```
Solusi:
1. Check warna hati sama dengan background
   Ubah canvas color atau emoji

2. Check emoji support:
   print("❤️")  # Di console, harus terlihat

3. Ubah emoji:
   "❤️" → "💕"
```

---

## 🔍 Debugging Tips

### **Tip 1: Print untuk debug**
```python
def show_welcome_page(self):
    print(f"DEBUG: Current page = {self.current_page}")  # Add this
    # ... rest of code
```

### **Tip 2: Check widget existence**
```python
def clear_window(self):
    widgets = self.root.winfo_children()
    print(f"DEBUG: {len(widgets)} widgets before clear")  # Add this
    for widget in widgets:
        widget.destroy()
    print(f"DEBUG: {len(self.root.winfo_children())} after clear")  # Add this
```

### **Tip 3: Monitor memory usage**
```python
import psutil
import os

process = psutil.Process(os.getpid())
print(f"Memory: {process.memory_info().rss / 1024 / 1024} MB")
```

### **Tip 4: Check active bindings**
```python
def show_welcome_page(self):
    print(f"DEBUG: Bindings = {self.root.bind()}")
```

---

## 🎯 Performance Optimization

### **Jika aplikasi lambat:**

```python
# 1. Kurangi animation frequency:
self.root.after(1000, self.animate)  # Dari 500ms ke 1000ms

# 2. Kurangi jumlah items di canvas:
if random.random() < 0.1:  # Dari 0.3 ke 0.1
    create_heart()

# 3. Clear old canvas items:
self.canvas.delete("old_items")

# 4. Use simpler shapes:
# Ganti bunga kompleks dengan emoji sederhana
canvas.create_text(x, y, text="🌹")  # Lebih cepat dari drawing

# 5. Limit drawing operations:
if len(self.canvas.find_all()) > 100:
    self.canvas.delete("oldest_item")
```

---

## ✅ Pre-Launch Checklist

Sebelum kirim ke pacar, check semua ini:

### **Functionality:**
- [ ] Aplikasi start tanpa error
- [ ] Yes button works & transisi smooth
- [ ] No button shows message
- [ ] Semua animasi berjalan
- [ ] Tombol responsive
- [ ] Text readable

### **Visual:**
- [ ] Warna cantik & konsisten
- [ ] Font readable
- [ ] Layout balanced
- [ ] Tidak ada text overflow
- [ ] Animasi smooth (tidak lag)

### **Content:**
- [ ] Pesan romantis ada
- [ ] English quotes present
- [ ] Indonesian text correct
- [ ] Emoji bagus & visible
- [ ] Tidak ada typo/kesalahan

### **Technical:**
- [ ] No console errors
- [ ] No memory leak
- [ ] Window dapat di-close
- [ ] Berjalan di OS target (Windows/Mac/Linux)

---

## 📞 Still Having Issues?

### **Opsi 1: Check error log**
```bash
# Save error ke file
python valentine_app.py 2>&1 > error_log.txt

# Baca file dengan notepad
notepad error_log.txt
```

### **Opsi 2: Minimal test case**
```python
# Buat file test_simple.py
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="If you see this, Tkinter works!")
label.pack()
root.mainloop()

# Run: python test_simple.py
```

### **Opsi 3: Check Python installation**
```bash
python --version              # Harus >= 3.7
python -m tkinter             # Harus membuka window
python -c "import tkinter"    # Harus success
```

---

## 💡 Quick Reference

| Problem | Solution | Line |
|---------|----------|------|
| Slow animation | Decrease after() timeout | ~200 |
| No animation | Check current_page condition | ~150 |
| Font ugly | Change family or size | ~40 |
| Button lag | Optimize onclick() function | ~250 |
| Memory leak | Add explicit delete calls | ~180 |
| Text overflow | Reduce font size or wraplength | ~195 |
| Color wrong | Check RGBA/HEX format | ~5 |

---

**Need more help?**

1. Check README.md untuk overview
2. Check QUICK_START.md untuk setup
3. Check COLOR_PALETTE.md untuk customization
4. Re-read relevant section di dokumentasi ini

**Good luck! 💕**

If all else fails, restart dan try again! 😄
