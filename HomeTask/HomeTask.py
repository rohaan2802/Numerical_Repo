import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# -----------------------------
# 1. Original Polynomial (3rd order)
# -----------------------------
def f(x):
    return 2*x**3 - 3*x**2 + x - 5   # cubic polynomial

# 5 data points from the polynomial
x_points = np.linspace(-2, 2, 5)
y_points = f(x_points)

# -----------------------------
# 2. Manual Lagrange Interpolation
# -----------------------------
def lagrange_manual(x, xp, yp):
    total = 0
    n = len(xp)
    for i in range(n):
        term = yp[i]
        for j in range(n):
            if i != j:
                term *= (x - xp[j]) / (xp[i] - xp[j])
        total += term
    return total

# -----------------------------
# 3. SciPy Lagrange Interpolation
# -----------------------------
poly_scipy = lagrange(x_points, y_points)

# -----------------------------
# 4. Evaluate both methods
# -----------------------------
x_vals = np.linspace(-2, 2, 200)
y_true = f(x_vals)

y_manual = np.array([lagrange_manual(x, x_points, y_points) for x in x_vals])
y_scipy = poly_scipy(x_vals)

# -----------------------------
# 5. Error Analysis
# -----------------------------
rmse = np.sqrt(np.mean((y_manual - y_scipy) ** 2))
print("Root Mean Square Error (RMSE) between Manual and SciPy:", rmse)

# -----------------------------
# 6. Plot Results
# -----------------------------
plt.figure(figsize=(8,6))
plt.plot(x_vals, y_true, 'k--', label="Original Polynomial (True)")
plt.plot(x_vals, y_manual, 'b', label="Manual Lagrange")
plt.plot(x_vals, y_scipy, 'r', linestyle="dotted", label="SciPy Lagrange")
plt.scatter(x_points, y_points, color='g', marker='o', label="Data Points")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Lagrange Interpolation: Manual vs SciPy")
plt.legend()
plt.grid(True)
plt.show()

