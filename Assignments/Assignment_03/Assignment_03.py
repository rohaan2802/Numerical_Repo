# assign3_PI.py
import numpy as np
import matplotlib.pyplot as plt
import control as ctl

# Plant
num = [1.0]
den = [1.0, 2.0, 0.0]  # s^2(s+2) in denominator => plant 1/(s(s+2))
G = ctl.tf(num, den)

# PI gains chosen from analysis
Kp = 2.0248861318247524
Ki = 0.06465479767351344

# Controller C(s) = Kp + Ki/s
C = ctl.tf([Kp, Ki], [1.0, 0.0])

# Open-loop and closed-loop
L = C * G
T = ctl.feedback(L, 1)

# 1) Step response
t = np.linspace(0, 20, 2000)
t_out, y_out = ctl.step_response(T, t)

# Compute metrics (rise time, overshoot, settling time, steady-state error)
final_value = y_out[-1]
# Rise time (10-90% of final)
ten_pct = 0.1 * final_value
ninety_pct = 0.9 * final_value
try:
    t_rise_idx = np.where((y_out >= ten_pct) & (y_out <= ninety_pct))[0]
    if t_rise_idx.size > 0:
        t_rise = t_out[t_rise_idx[-1]] - t_out[t_rise_idx[0]]
    else:
        # fallback: first time to 90% minus first time to 10%
        t10_idx = np.where(y_out >= ten_pct)[0][0]
        t90_idx = np.where(y_out >= ninety_pct)[0][0]
        t_rise = t_out[t90_idx] - t_out[t10_idx]
except Exception:
    t_rise = np.nan

overshoot = (np.max(y_out) - final_value) / final_value * 100.0
# Settling time (2% band)
tol = 0.02
settle_idx = np.where(np.abs(y_out - final_value) > tol * np.abs(final_value))[0]
if settle_idx.size == 0:
    settling_time = 0.0
else:
    settling_time = t_out[settle_idx[-1] + 1] if settle_idx[-1] + 1 < len(t_out) else np.nan

ss_error = 1.0 - final_value

# Plot step response
plt.figure(figsize=(8,4))
plt.plot(t_out, y_out, label='Closed-loop step')
plt.axhline(1.0, color='k', linestyle='--', linewidth=0.7)
plt.title('Step response: PI controller')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("Metrics:")
print(f"  Rise time (approx 10-90%): {t_rise:.3f} s")
print(f"  Overshoot: {overshoot:.3f} %")
print(f"  Settling time (2%): {settling_time:.3f} s")
print(f"  Steady-state error: {ss_error:.6f}")

# 2) Pole-zero map
plt.figure(figsize=(6,6))
ctl.pzmap(T, Plot=True, title='Closed-loop Pole-Zero Map')
plt.grid(True)
plt.show()

# 3) Bode plot
plt.figure()
mag, phase, omega = ctl.bode(T, dB=True, Plot=True, omega=np.logspace(-2, 2, 500))
plt.suptitle('Bode plot of closed-loop transfer function', y=1.02)
plt.show()

# Gain margin and phase margin from L (open-loop)
gm, pm, sm, wg, wp, ws = ctl.stability_margins(L)
print("Bode-based margins (open-loop L(s)=C(s)G(s)):")
print(f"  Gain margin: {20*np.log10(gm) if gm!=float('inf') else 'Inf dB'} dB at w = {wg}")
print(f"  Phase margin: {pm:.3f} deg at w = {wp}")

