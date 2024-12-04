import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt

# Parameteri
xi_min = -10
xi_max = 10
N = 100

xi = np.linspace(xi_min, xi_max, N)
h = (xi_max - xi_min) / (N - 1)

H = np.zeros((N, N))

for i in range(N):
    H[i, i] = 1 / h**2 + 0.5 * xi[i] ** 2
    if i > 0:
        H[i, i - 1] = -0.5 / h**2
    if i < N - 1:
        H[i, i + 1] = -0.5 / h**2

eigenvalues, eigenvectors = eigh(H)

print(eigenvalues[:5])

for n in range(5):
    plt.plot(xi, eigenvectors[:, n], label=f"n={n}")
plt.xlabel("ξ")
plt.ylabel("ψ(ξ)")
plt.legend()
plt.grid()
plt.savefig("fig1.png")
plt.show()
