import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import font_manager
import os

# بررسی وجود فایل فونت
font_path = "/Users/arshia/Library/Fonts/GreatVibes-Regular.ttf"
if not os.path.exists(font_path):
    raise FileNotFoundError("Font file not found. Please check the path.")

# معرفی فونت انگلیسی به هم پیوسته
cursive_font = font_manager.FontProperties(fname=font_path)

# تولید مقادیر پارامتری ثابت
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# ایجاد شکل و تنظیمات اولیه
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_title("Heart Animation", fontproperties=cursive_font, fontsize=20)
ax.grid(True)

# تعریف رنگ Hex
hex_color = "#4169E1"  

# رسم اولیه قلب
heart_line, = ax.plot([], [], color="red", linewidth=2)
heart_fill = ax.fill([], [], alpha=0.6)[0]  # استفاده از رنگ Hex
text = ax.text(0, 0, "William", fontsize=40, color="black", 
               ha="center", va="center", fontproperties=cursive_font)

# تابع برای به‌روزرسانی انیمیشن
def update(frame):
    # تغییر مقیاس برای حالت ضربان قلب
    scale = 1 + 0.1 * np.sin(frame / 10)
    scaled_x = scale * x
    scaled_y = scale * y
    
    # به‌روزرسانی خطوط و پرشدگی قلب
    heart_line.set_data(scaled_x, scaled_y)
    heart_fill.set_xy(np.column_stack([scaled_x, scaled_y]))
    
    # حرکت متن در داخل قلب
  
    return heart_line, heart_fill, text

# تنظیمات انیمیشن
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# نمایش انیمیشن
plt.show()