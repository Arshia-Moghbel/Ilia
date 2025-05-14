import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ثابت‌ها
G = 6.67430e-11  # ثابت گرانش (m^3 kg^-1 s^-2)
M = 1.989e30     # جرم جسم مرکزی (kg)، مثلاً خورشید

# شرایط اولیه
r = np.array([1e11, 0])  # موقعیت اولیه (متر)
v = np.array([0, 3e4])   # سرعت اولیه (متر بر ثانیه)
dt = 3600                # گام زمانی (ثانیه)، مثلاً 1 ساعت
total_steps = 1000       # تعداد کل گام‌های شبیه‌سازی

# تابع محاسبه شتاب گرانشی
def gravitational_acceleration(r, M, G):
    r_norm = np.linalg.norm(r)
    if r_norm == 0:
        return np.array([0.0, 0.0])  # جلوگیری از تقسیم بر صفر
    return -G * M * r / r_norm**3

# شبیه‌سازی حرکت با روش اویلر
positions = [r.copy()]
for _ in range(total_steps):
    a = gravitational_acceleration(r, M, G)
    v += a * dt
    r += v * dt
    positions.append(r.copy())
positions = np.array(positions)

# تنظیم شکل و محورها برای نمایش
fig, ax = plt.subplots()
ax.set_xlim(-1.5e11, 1.5e11)
ax.set_ylim(-1.5e11, 1.5e11)
ax.set_xlabel('X (متر)')
ax.set_ylabel('Y (متر)')
ax.set_title('شبیه‌سازی ساده مدار گرانشی')
ax.grid(True)

# رسم جسم مرکزی (ثابت در مبدا)
central_body, = ax.plot(0, 0, 'ro', label='جرم مرکزی (مثلاً سیاه‌چاله)')

# رسم جسم مداری (در موقعیت اولیه)
orbiting_body, = ax.plot([positions[0, 0]], [positions[0, 1]], 'bo', label='جسم مداری')
ax.legend()

# تابع به‌روزرسانی برای انیمیشن
def update(frame):
    orbiting_body.set_data([positions[frame, 0]], [positions[frame, 1]])
    return orbiting_body,

# ایجاد انیمیشن
ani = FuncAnimation(fig, update, frames=len(positions), interval=50, blit=True)

# ذخیره تصویر ثابت از حالت اولیه
plt.savefig('orbit_simulation.png')

# نمایش انیمیشن
plt.show()