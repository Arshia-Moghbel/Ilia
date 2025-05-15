import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import font_manager
import os

font_path = "/Users/arshia/Library/Fonts/GreatVibes-Regular.ttf"
if os.path.exists(font_path):
    cursive_font = font_manager.FontProperties(fname=font_path)
else:
    cursive_font = None  

t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_title("Heart Animation", fontproperties=cursive_font, fontsize=20)
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])


hex_color = "#FF3366"


heart_line, = ax.plot([], [], color="red", linewidth=2)
heart_fill = ax.fill([], [], hex_color, alpha=0.6)[0]

text = ax.text(0, 0, "William", fontsize=40, color="black", 
               ha="center", va="center", fontproperties=cursive_font)


def update(frame):

    scale = 1 + 0.05 * np.sin(frame / 10)
    scaled_x = scale * x
    scaled_y = scale * y
    
    heart_line.set_data(scaled_x, scaled_y)
    heart_fill.set_xy(np.column_stack([scaled_x, scaled_y]))
    
    return heart_line, heart_fill, text


ani = FuncAnimation(fig, update, frames=200, interval=50)

plt.show()