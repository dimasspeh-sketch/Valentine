import tkinter as tk
from tkinter import font, messagebox
import math
import random

# ==================== KONFIGURASI WARNA VALENTINE ====================
PINK_LIGHT = "#FFB6C1"      # Light pink
PINK_MEDIUM = "#FFB0D4"     # Medium pink
RED_VALENTINE = "#FF1493"   # Deep pink
RED_DARK = "#C41E3A"        # Dark red
RED_LIGHT = "#FF6B7A"       # Light red
WHITE_CREAM = "#FFF8DC"     # Cream white
GOLD = "#FFD700"            # Gold accent

# ==================== KELAS UTAMA APLIKASI ====================
class ValentineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💕 Valentine's Day Adventure 💕")
        self.root.geometry("1000x700")
        self.root.configure(bg=PINK_LIGHT)
        self.root.resizable(False, False)
        
        # Pusatkan window di layar
        self.center_window()
        
        # Font setup
        self.font_title = font.Font(family="Arial", size=32, weight="bold")
        self.font_subtitle = font.Font(family="Arial", size=14)
        self.font_text = font.Font(family="Arial", size=11)
        self.font_button = font.Font(family="Arial", size=12, weight="bold")
        self.font_quote = font.Font(family="Georgia", size=10, slant="italic")
        
        # Current page
        self.current_page = "welcome"
        
        # Data holder untuk nama couple
        self.couple_name = "My Love"
        
        # Mulai dari halaman pertama
        self.show_welcome_page()
    
    def center_window(self):
        """Pusatkan window di tengah layar"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def clear_window(self):
        """Hapus semua widget dari window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # ==================== HALAMAN 1: WELCOME PAGE (YES/NO GAME) ====================
    def show_welcome_page(self):
        """Halaman awal dengan game Yes/No"""
        self.clear_window()
        self.current_page = "welcome"
        
        # Background frame
        main_frame = tk.Frame(self.root, bg=PINK_LIGHT)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas untuk animasi hati jatuh
        self.canvas_welcome = tk.Canvas(main_frame, bg=PINK_LIGHT, highlightthickness=0)
        self.canvas_welcome.pack(fill=tk.BOTH, expand=True)
        
        # Title dengan hati
        title_frame = tk.Frame(self.canvas_welcome, bg=PINK_LIGHT)
        self.canvas_welcome.create_window(500, 50, window=title_frame)
        
        title = tk.Label(title_frame, text="💕 Valentine's Day Adventure 💕", 
                         font=self.font_title, bg=PINK_LIGHT, fg=RED_DARK)
        title.pack()
        
        # Pesan romantis (English + Indo)
        message_frame = tk.Frame(self.canvas_welcome, bg=WHITE_CREAM, 
                                 highlightbackground=RED_VALENTINE, highlightthickness=2)
        self.canvas_welcome.create_window(500, 200, window=message_frame, width=700)
        
        quote_en = tk.Label(message_frame, 
                           text='"Love is the bridge between two hearts, and you are mine."',
                           font=self.font_quote, bg=WHITE_CREAM, fg=RED_VALENTINE, 
                           wraplength=650)
        quote_en.pack(pady=10)
        
        message_indo = tk.Label(message_frame, 
                               text="Will you be my Valentine?\nApakah kamu ingin memulai petualangan cinta ini?\n\n" +
                                    "Dengan percaya diri, aku meminta hatimu menjadi milikku selamanya...",
                               font=self.font_subtitle, bg=WHITE_CREAM, fg=RED_DARK, 
                               justify=tk.CENTER, wraplength=650)
        message_indo.pack(pady=20)
        
        # Button frame
        button_frame = tk.Frame(self.canvas_welcome, bg=PINK_LIGHT)
        self.canvas_welcome.create_window(500, 450, window=button_frame)
        
        # Yes button dengan style cantik
        yes_btn = tk.Button(button_frame, text="💚 YES 💚", font=self.font_button,
                           bg=RED_LIGHT, fg="white", padx=30, pady=15,
                           command=self.on_yes_clicked, activebackground=RED_DARK,
                           relief=tk.RAISED, bd=3, cursor="hand2")
        yes_btn.pack(side=tk.LEFT, padx=30)
        
        # No button
        no_btn = tk.Button(button_frame, text="❌ NO ❌", font=self.font_button,
                          bg=PINK_MEDIUM, fg=RED_DARK, padx=30, pady=15,
                          command=self.on_no_clicked, activebackground=PINK_LIGHT,
                          relief=tk.RAISED, bd=3, cursor="hand2")
        no_btn.pack(side=tk.LEFT, padx=30)
        
        # Mulai animasi hati jatuh
        self.animate_falling_hearts()
    
    def animate_falling_hearts(self):
        """Animasi hati jatuh dari atas"""
        if self.current_page != "welcome":
            return
        
        # Random hati jatuh
        if random.random() < 0.3:
            x = random.randint(50, 950)
            heart = self.canvas_welcome.create_text(x, -20, text="❤️", font=("Arial", random.randint(20, 40)))
            self.animate_heart_fall(heart, x, 0)
        
        self.root.after(800, self.animate_falling_hearts)
    
    def animate_heart_fall(self, heart_id, x, y):
        """Animasi hati jatuh ke bawah"""
        if self.current_page != "welcome":
            try:
                self.canvas_welcome.delete(heart_id)
            except:
                pass
            return
        
        if y < 700:
            try:
                self.canvas_welcome.coords(heart_id, x + math.sin(y/20) * 10, y)
                self.root.after(30, lambda: self.animate_heart_fall(heart_id, x, y + 5))
            except:
                pass
        else:
            try:
                self.canvas_welcome.delete(heart_id)
            except:
                pass
    
    def on_yes_clicked(self):
        """Handle ketika Yes diklik"""
        # Animasi transisi
        self.animate_transition_to_photo_page()
    
    def on_no_clicked(self):
        """Handle ketika No diklik - tunjukkan pesan lucu"""
        result = messagebox.showinfo("💭 Love is Patient 💭", 
                                    "Love is patient! Coba lagi ya?\n\n'True love waits, but not forever!'")
    
    def animate_transition_to_photo_page(self):
        """Animasi transisi ke halaman foto"""
        self.clear_window()
        self.show_photo_page()
    
    # ==================== HALAMAN 2: PHOTO PAGE ====================
    def show_photo_page(self):
        """Halaman untuk menampilkan placeholder foto Valentine"""
        self.clear_window()
        self.current_page = "photo"
        
        # Background
        main_frame = tk.Frame(self.root, bg=PINK_LIGHT)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(main_frame, text="💕 Foto Kenangan Cinta Kita 💕", 
                        font=self.font_title, bg=PINK_LIGHT, fg=RED_DARK)
        title.pack(pady=20)
        
        # Canvas untuk placeholder hati
        canvas = tk.Canvas(main_frame, bg=PINK_LIGHT, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True, padx=50, pady=30)
        
        # Draw heart shape placeholder
        self.draw_heart_placeholder(canvas)
        
        # Bottom frame dengan tombol
        bottom_frame = tk.Frame(main_frame, bg=PINK_LIGHT)
        bottom_frame.pack(pady=20)
        
        next_btn = tk.Button(bottom_frame, text="💕 Lanjut ke Surat Cinta 💕", 
                            font=self.font_button, bg=RED_VALENTINE, fg="white",
                            padx=20, pady=12, command=self.show_letter_page,
                            activebackground=RED_DARK, relief=tk.RAISED, bd=3,
                            cursor="hand2")
        next_btn.pack()
    
    def draw_heart_placeholder(self, canvas):
        """Draw heart shape sebagai placeholder untuk foto"""
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        
        if canvas_width < 100:  # Jika belum ter-render dengan benar
            canvas_width = 900
            canvas_height = 300
        
        cx, cy = canvas_width // 2, canvas_height // 2
        size = 100
        
        # Draw heart shape menggunakan bezier-like curves
        points = []
        for t in range(0, 361, 5):
            rad = math.radians(t)
            # Heart equation
            x = 16 * math.sin(rad) ** 3
            y = 13 * math.cos(rad) - 5 * math.cos(2*rad) - 2 * math.cos(3*rad) - math.cos(4*rad)
            points.append(cx + x * size)
            points.append(cy - y * size - 50)
        
        # Draw heart outline
        if len(points) > 4:
            canvas.create_polygon(points, fill=PINK_MEDIUM, outline=RED_VALENTINE, width=3)
            
            # Text di tengah hati
            canvas.create_text(cx, cy - 50, text="🖼️\n\nFoto Kenangan Valentine\nakan muncul di sini\n\n✨",
                              font=("Arial", 16), fill=RED_DARK, justify=tk.CENTER)
    
    # ==================== HALAMAN 3: LETTER PAGE ====================
    def show_letter_page(self):
        """Halaman surat dengan animasi dan konten Valentine"""
        self.clear_window()
        self.current_page = "letter"
        
        # Background dengan warna Valentine
        main_frame = tk.Frame(self.root, bg=RED_LIGHT)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(main_frame, text="💌 Surat Cinta Untukmu 💌", 
                        font=self.font_title, bg=RED_LIGHT, fg="white")
        title.pack(pady=15)
        
        # Main content frame
        content_frame = tk.Frame(main_frame, bg=PINK_LIGHT)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Frame untuk letter (envelope-like appearance)
        letter_frame = tk.Frame(content_frame, bg=WHITE_CREAM, 
                               highlightbackground=RED_VALENTINE, highlightthickness=3, 
                               relief=tk.RAISED)
        letter_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Horizontal split: Left (text) and Right (image)
        h_split = tk.Frame(letter_frame, bg=WHITE_CREAM)
        h_split.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # LEFT SIDE: Letter content
        left_frame = tk.Frame(h_split, bg=WHITE_CREAM)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Quote di atas
        quote_label = tk.Label(left_frame, 
                              text='"Love is not about how many days, but how much you love each other."\n— Unknown',
                              font=self.font_quote, bg=WHITE_CREAM, fg=RED_VALENTINE, 
                              justify=tk.CENTER, wraplength=350)
        quote_label.pack(pady=10)
        
        # Divider
        tk.Frame(left_frame, bg=GOLD, height=2).pack(fill=tk.X, pady=10)
        
        # Letter content
        letter_text = """Sayang,

Hari ini adalah momen istimewa untuk mengatakan 
apa yang selama ini ku simpan di hati.

Kamu adalah cahaya dalam hidupku, sinar 
matahari yang menerangi setiap pagi ku. Dalam 
setiap detik bersama mu, aku merasakan bahwa 
hidup memang bermakna.

Terima kasih telah memilih aku, untuk 
menjadi bagian dari cerita indah kita. Setiap 
senyuman mu, setiap tawa mu, membuat hatiku 
berdetak lebih cepat.

Aku bersumpah akan selalu ada untuk mu, 
dalam suka dan duka, dalam gelap dan terang. 
Mari kita ciptakan bersama kenangan indah 
yang akan kita ceritakan sampai tua.

Selamanya cinta mu,
Sang Pecinta Valentine 💕"""
        
        letter_content = tk.Label(left_frame, text=letter_text, 
                                 font=self.font_text, bg=WHITE_CREAM, 
                                 fg=RED_DARK, justify=tk.LEFT, wraplength=350)
        letter_content.pack(pady=10, anchor=tk.W)
        
        # RIGHT SIDE: Image placeholder dan flower tree
        right_frame = tk.Frame(h_split, bg=WHITE_CREAM)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20)
        
        # Canvas untuk animasi pohon bunga
        tree_canvas = tk.Canvas(right_frame, bg=WHITE_CREAM, 
                               highlightthickness=0, width=250, height=280)
        tree_canvas.pack(pady=10)
        
        # Draw animated flower tree
        self.draw_flower_tree(tree_canvas)
        
        # BOTTOM: Photo frames (4 boxes)
        photo_frame_label = tk.Label(letter_frame, text="📸 Foto Kenangan Kita 📸", 
                                     font=self.font_button, bg=WHITE_CREAM, fg=RED_VALENTINE)
        photo_frame_label.pack(pady=10)
        
        # Grid untuk 4 foto
        photos_grid = tk.Frame(letter_frame, bg=WHITE_CREAM)
        photos_grid.pack(pady=10)
        
        photos = [
            ("📷 Foto 1", "Kenangan Manis"),
            ("📷 Foto 2", "Saat Tertawa"),
            ("📷 Foto 3", "Momen Istimewa"),
            ("📷 Foto 4", "Cinta Kita")
        ]
        
        for i, (emoji, text) in enumerate(photos):
            photo_box = self.create_photo_box(photos_grid, emoji, text)
            photo_box.grid(row=0, column=i, padx=10, pady=10)
        
        # Bottom buttons
        button_frame = tk.Frame(letter_frame, bg=WHITE_CREAM)
        button_frame.pack(pady=20)
        
        close_btn = tk.Button(button_frame, text="❤️ Happy Valentine's Day! ❤️", 
                             font=self.font_button, bg=RED_VALENTINE, fg="white",
                             padx=20, pady=12, command=self.show_ending,
                             activebackground=RED_DARK, relief=tk.RAISED, bd=3,
                             cursor="hand2")
        close_btn.pack()
        
        # Animasi surat slide up
        self.animate_letter_slide_up(letter_frame)
    
    def create_photo_box(self, parent, emoji, label_text):
        """Create kotak foto dengan frame hati"""
        box = tk.Frame(parent, bg=PINK_MEDIUM, highlightbackground=RED_VALENTINE, 
                      highlightthickness=2, relief=tk.RAISED)
        
        emoji_label = tk.Label(box, text=emoji, font=("Arial", 24), 
                              bg=PINK_MEDIUM, fg=RED_VALENTINE)
        emoji_label.pack(pady=5)
        
        text_label = tk.Label(box, text=label_text, font=("Arial", 9, "bold"),
                             bg=PINK_MEDIUM, fg=RED_DARK, wraplength=60, justify=tk.CENTER)
        text_label.pack(pady=5)
        
        return box
    
    def draw_flower_tree(self, canvas):
        """Draw animated flower tree"""
        width = canvas.winfo_width() or 250
        height = canvas.winfo_height() or 280
        
        # Draw trunk
        canvas.create_rectangle(width//2 - 8, height//2 + 40, 
                               width//2 + 8, height - 20,
                               fill="#8B4513", outline="#654321", width=2)
        
        # Draw flowers (animated popping effect)
        flowers = [
            (width//2 - 60, height//2 - 20),
            (width//2 + 60, height//2 - 20),
            (width//2 - 40, height//2 - 60),
            (width//2 + 40, height//2 - 60),
            (width//2, height//2 - 90),
            (width//2 - 70, height//2 + 10),
            (width//2 + 70, height//2 + 10),
        ]
        
        for i, (x, y) in enumerate(flowers):
            # Outer petals
            for petal in range(5):
                angle = petal * 72
                px = x + 25 * math.cos(math.radians(angle))
                py = y + 25 * math.sin(math.radians(angle))
                canvas.create_oval(px-8, py-8, px+8, py+8, fill=RED_VALENTINE, 
                                  outline=RED_DARK, width=1)
            
            # Center
            canvas.create_oval(x-6, y-6, x+6, y+6, fill=GOLD, outline=RED_DARK, width=1)
        
        # Draw leaves
        canvas.create_polygon(width//2 - 40, height//2 + 20,
                             width//2 - 60, height//2 - 10,
                             width//2 - 45, height//2 + 30,
                             fill="#2F8B42", outline="#1B4D23", width=1)
        
        canvas.create_polygon(width//2 + 40, height//2 + 20,
                             width//2 + 60, height//2 - 10,
                             width//2 + 45, height//2 + 30,
                             fill="#2F8B42", outline="#1B4D23", width=1)
    
    def animate_letter_slide_up(self, letter_frame):
        """Animasi surat slide up dari bawah"""
        if self.current_page != "letter":
            return
        
        # Reset position
        letter_frame.place(x=10, y=750)
        self.animate_letter_position(letter_frame, 750, 70)
    
    def animate_letter_position(self, frame, current_y, target_y):
        """Animate frame position"""
        if self.current_page != "letter":
            return
        
        if current_y > target_y:
            current_y -= 15
            frame.place(x=10, y=current_y, relwidth=0.98, relheight=0.85)
            self.root.after(20, lambda: self.animate_letter_position(frame, current_y, target_y))
        else:
            frame.place_forget()
            frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # ==================== HALAMAN AKHIR ====================
    def show_ending(self):
        """Halaman akhir dengan pesan Valentine"""
        self.clear_window()
        self.current_page = "ending"
        
        main_frame = tk.Frame(self.root, bg=RED_VALENTINE)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas untuk animasi hati
        canvas = tk.Canvas(main_frame, bg=RED_VALENTINE, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Title
        canvas.create_text(500, 80, text="💕 Happy Valentine's Day! 💕",
                          font=self.font_title, fill="white")
        
        # Message
        message = """Terima kasih telah menjadi bagian dari petualangan cinta ini.
        
Setiap momen bersamu adalah hadiah terindah.
Selamanya akan aku hargai cinta yang kamu berikan.

I Love You More Than Words Can Say ❤️
        
Selamanya milikmu,
Sang Pecinta Valentine"""
        
        canvas.create_text(500, 300, text=message,
                          font=self.font_text, fill="white", justify=tk.CENTER)
        
        # Animated hearts
        self.animate_ending_hearts(canvas)
        
        # Close button
        close_frame = tk.Frame(canvas, bg=RED_VALENTINE)
        canvas.create_window(500, 600, window=close_frame)
        
        close_btn = tk.Button(close_frame, text="Tutup Aplikasi", 
                             font=self.font_button, bg="white", fg=RED_VALENTINE,
                             padx=30, pady=12, command=self.root.quit,
                             activebackground=PINK_LIGHT, relief=tk.RAISED, bd=3,
                             cursor="hand2")
        close_btn.pack()
    
    def animate_ending_hearts(self, canvas):
        """Animasi hati di halaman akhir"""
        if self.current_page != "ending":
            return
        
        if random.random() < 0.5:
            x = random.randint(50, 950)
            y = random.randint(100, 150)
            size = random.randint(20, 40)
            heart = canvas.create_text(x, y, text="❤️", font=("Arial", size))
            self.animate_floating_heart(canvas, heart, x, y)
        
        self.root.after(300, lambda: self.animate_ending_hearts(canvas))
    
    def animate_floating_heart(self, canvas, heart_id, x, y):
        """Animasi hati melayang"""
        if self.current_page != "ending":
            try:
                canvas.delete(heart_id)
            except:
                pass
            return
        
        if y > -50:
            new_x = x + math.sin(y/20) * 5
            try:
                canvas.coords(heart_id, new_x, y - 3)
                self.root.after(30, lambda: self.animate_floating_heart(canvas, heart_id, x, y - 3))
            except:
                pass
        else:
            try:
                canvas.delete(heart_id)
            except:
                pass


# ==================== MAIN PROGRAM ====================
if __name__ == "__main__":
    root = tk.Tk()
    app = ValentineApp(root)
    root.mainloop()
