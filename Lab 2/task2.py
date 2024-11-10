import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 1
N = 1000
x_start = -2 * a
x_end = 2 * a
h = (x_end - x_start) / N

x = np.linspace(x_start, x_end, N + 1)
y = a * np.cosh(x / a) - a

y_prime_3pt = np.zeros_like(y)
for i in range(1, N):
    y_prime_3pt[i] = (y[i + 1] - y[i - 1]) / (2 * h)

y_double_prime_3pt = np.zeros_like(y)
for i in range(1, N):
    y_double_prime_3pt[i] = (y[i + 1] - 2 * y[i] + y[i - 1]) / (h**2)

y_prime_5pt = np.zeros_like(y)
for i in range(2, N - 2):
    y_prime_5pt[i] = (-y[i + 2] + 8 * y[i + 1] - 8 * y[i - 1] + y[i - 2]) / (12 * h)

y_double_prime_5pt = np.zeros_like(y)
for i in range(2, N - 2):
    y_double_prime_5pt[i] = (
        -y[i + 2] + 16 * y[i + 1] - 30 * y[i] + 16 * y[i - 1] - y[i - 2]
    ) / (12 * h**2)

rhs_3pt = np.sqrt(1 + y_prime_3pt**2) / a
rhs_5pt = np.sqrt(1 + y_prime_5pt**2) / a

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(
    x[1:N], y_double_prime_3pt[1:N], label="Skaitliski $y''$ (3-punktu)", color="red"
)
plt.plot(
    x[1:N],
    rhs_3pt[1:N],
    label="$\\frac{\\sqrt{1 + (y')^2}}{a}$ (3-punktu)",
    linestyle="-.",
)
plt.xlabel("x")
plt.ylabel("$y''$ un $\\frac{\\sqrt{1 + (y')^2}}{a}$")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(
    x[2 : N - 2], y_double_prime_5pt[2 : N - 2], label="Skaitliski $y''$ (5-punktu)"
)
plt.plot(
    x[2 : N - 2],
    rhs_5pt[2 : N - 2],
    label="$\\frac{\\sqrt{1 + (y')^2}}{a}$ (5-punktu)",
    linestyle="--",
)
plt.xlabel("x")
plt.ylabel("$y''$ un $\\frac{\\sqrt{1 + (y')^2}}{a}$")
plt.legend()
plt.grid(True)
plt.show()
