import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# پارامترها
G = 6.67430e-11               # ثابت گرانش
M = 10 * 1.989e30             # جرم سیاه‌چاله (10 برابر خورشید)
dt = 1                        # گام زمانی (1 ثانیه)
total_time = 50000            # کل زمان شبیه‌سازی (ثانیه)
steps = int(total_time / dt)

# موقعیت اولیه ستاره (یک فاصله مشخص از سیاه‌چاله)
r0 = np.array([1e10, 0, 0])  # فاصله اولیه: 10 میلیارد متر از مرکز
v0 = np.array([0, 3e4, 0])   # سرعت اولیه: 30 کیلومتر بر ثانیه

# لیست‌ها برای ذخیره مسیر
positions = []
velocities = []

# تنظیمات اولیه
r = r0.copy()
v = v0.copy()

# شبیه‌سازی با استفاده از روش اویلر
for _ in range(steps):
    distance = np.linalg.norm(r)
    acceleration = -G * M * r / distance**3
    v += acceleration * dt
    r += v * dt
    positions.append(r.copy())
    velocities.append(v.copy())

# تبدیل به آرایه و ذخیره CSV
positions = np.array(positions)
df = pd.DataFrame(positions, columns=["x", "y", "z"])
df.to_csv("star_orbit_near_blackhole.csv", index=False)

# نمایش نمودار دوبعدی مسیر برای بررسی
plt.plot(positions[:, 0], positions[:, 1], color="yellow")
plt.scatter(0, 0, color="black", label="Black Hole")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Star Orbit Near Black Hole")
plt.axis("equal")
plt.legend()
plt.grid()
plt.show()