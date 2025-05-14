import numpy as np
import matplotlib.pyplot as plt

# ثابت‌های فیزیکی
G = 6.67430e-11         # ثابت گرانش، m^3 kg^-1 s^-2
c = 3e8                 # سرعت نور، m/s
M = 10 * 1.989e30       # جرم سیاه‌چاله (مثلاً ۱۰ برابر خورشید)

# شعاع شوارتزشیلد
Rs = 2 * G * M / c**2

# محدوده شعاعی
r_min = 1.1 * Rs
r_max = 10 * Rs

# تعداد پرتوهای نور
num_rays = 5
theta_range = np.linspace(-np.pi / 2, np.pi / 2, num_rays)

# تابع مسیر نور به‌صورت تقریبی
def light_path_approx(theta0, b):
    phi = np.linspace(-10, 10, 1000)
    r = b / np.cos(phi - theta0)
    r[r < r_min] = np.nan  # جلوگیری از ورود به افق رویداد
    return r, phi

# ترسیم
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title("Light Bending Near a Black Hole (Approximate Simulation)")
ax.set_xlim(-12 * Rs, 12 * Rs)
ax.set_ylim(-12 * Rs, 12 * Rs)

# رسم سیاه‌چاله
black_hole = plt.Circle((0, 0), Rs, color='black')
ax.add_artist(black_hole)

# رسم پرتوها
b_vals = np.linspace(2 * Rs, 10 * Rs, num_rays)
for i, theta0 in enumerate(theta_range):
    b = b_vals[i]
    r, phi = light_path_approx(theta0, b)
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    ax.plot(x, y, label=f"b = {b:.2e} m")

ax.legend()
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_aspect('equal')
plt.grid(True)
plt.tight_layout()
plt.show()