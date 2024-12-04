import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt


def calculate_eigenvalues(xi_max, N):
    xi_min = -xi_max
    xi = np.linspace(xi_min, xi_max, N)
    h = xi[1] - xi[0]

    H = np.zeros((N, N))
    for i in range(N):
        H[i, i] = 1 / h**2 + 0.5 * xi[i] ** 2
        if i > 0:
            H[i, i - 1] = -0.5 / h**2
        if i < N - 1:
            H[i, i + 1] = -0.5 / h**2

    eigenvalues, _ = eigh(H)
    return eigenvalues


# Parameteri
xi_max_values = [10, 12, 15]
N_values = [100, 200, 300]
reference_xi_max = 10
reference_N = 100

reference_eigenvalues = calculate_eigenvalues(reference_xi_max, reference_N)

eigenvalues_xi_max = [
    calculate_eigenvalues(xi_max, reference_N) for xi_max in xi_max_values
]
errors_xi_max = [
    np.abs(eigenvalues[:5] - reference_eigenvalues[:5])
    / reference_eigenvalues[:5]
    * 100
    for eigenvalues in eigenvalues_xi_max
]

eigenvalues_N = [calculate_eigenvalues(reference_xi_max, N) for N in N_values]
errors_N = [
    np.abs(eigenvalues[:5] - reference_eigenvalues[:5])
    / reference_eigenvalues[:5]
    * 100
    for eigenvalues in eigenvalues_N
]

plt.figure(figsize=(10, 6))
for i, xi_max in enumerate(xi_max_values):
    plt.plot(range(5), errors_xi_max[i], label=f"$\\xi_{{\\text{{max}}}}$ = {xi_max}")
plt.xlabel("Enerģijas līmenis (n)")
plt.ylabel("Relatīvā kļūda (%)")
plt.legend()
plt.grid()
plt.savefig("eigenvalue_vs_ximax.png")
plt.show()

plt.figure(figsize=(10, 6))
for i, N in enumerate(N_values):
    plt.plot(range(5), errors_N[i], label=f"Režģa punkti $N$ = {N}")
plt.xlabel("Enerģijas līmenis (n)")
plt.ylabel("Relatīvā kļūda (%)")
plt.legend()
plt.grid()
plt.savefig("eigenvalue_vs_N.png")
plt.show()
