import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ثابت‌ها
G = 6.67430e-11            # ثابت گرانش
c = 3e8                    # سرعت نور
M = 10 * 1.989e30          # جرم سیاه‌چاله (10 برابر جرم خورشید)
Rs = 2 * G * M / c**2      # شعاع شوارتزشیلد

# معادلات حرکت نسبیتی (تقریبی برای مدار در صفحه)
def equations(t, y):
    x, y_pos, vx, vy = y
    r = np.sqrt(x**2 + y_pos**2)
    ax = -G * M * x / r**3 * (1 + (3 * Rs) / (2 * r))
    ay = -G * M * y_pos / r**3 * (1 + (3 * Rs) / (2 * r))
    return [vx, vy, ax, ay]

# شرایط اولیه
x0 = 6 * Rs
y0 = 0
vx0 = 0
vy0 = 0.5 * np.sqrt(G * M / x0)  # سرعت مداری اولیه

y_init = [x0, y0, vx0, vy0]
t_span = (0, 2e5)  # زمان شبیه‌سازی
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# حل معادلات دیفرانسیل
sol = solve_ivp(equations, t_span, y_init, t_eval=t_eval, rtol=1e-8)

# ترسیم نتایج
plt.figure(figsize=(8, 8))
plt.plot(sol.y[0], sol.y[1], label='Trajectory', color='blue')
plt.plot(0, 0, 'ko', markersize=10, label='Black Hole')  # موقعیت سیاه‌چاله
circle = plt.Circle((0, 0), Rs, color='black', fill=True, label='Event Horizon')
plt.gca().add_patch(circle)

plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Orbit of a Star Near a Black Hole (Relativistic Correction)')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.show()