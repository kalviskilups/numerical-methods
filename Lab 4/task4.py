import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    theta = np.pi / 6
    tau_period = 1.3 * 2 * np.pi
    omega = 2 * np.pi / tau_period
    omega_0 = 1
    max_iter = 50
    tolerance = 1e-6

    tau = np.linspace(0, tau_period, 500)
    n_max = 20
    A_n = np.zeros(2 * n_max + 1, dtype=complex)
    A_n[n_max - 1] = theta / 2
    A_n[n_max + 1] = theta / 2

    for k in range(max_iter):
        alpha_k = np.zeros_like(tau, dtype=complex)
        for n in range(-n_max, n_max + 1):
            alpha_k += A_n[n + n_max] * np.exp(1j * n * omega * tau)
        
        sin_alpha_k = np.sin(alpha_k.real)
        
        B_n = np.zeros_like(A_n, dtype=complex)
        for n in range(-n_max, n_max + 1):
            B_n[n + n_max] = np.trapz(sin_alpha_k * np.exp(-1j * n * omega * tau), tau) / tau_period
        
        A_n_next = np.zeros_like(A_n, dtype=complex)
        for n in range(-n_max, n_max + 1):
            if n != 0:
                A_n_next[n + n_max] = (omega_0**2 / (omega**2 * n**2)) * B_n[n + n_max]
        
        if np.max(np.abs(A_n_next - A_n)) < tolerance:
            break
        
        A_n = A_n_next

    alpha_final = np.zeros_like(tau, dtype=complex)
    for n in range(-n_max, n_max + 1):
        alpha_final += A_n[n + n_max] * np.exp(1j * n * omega * tau)

    plt.figure(figsize=(8, 5))
    plt.plot(tau, alpha_final.real, label=r"$\alpha(\tau)$ (Galīgais risinājums)", linewidth=2, color='red')
    plt.xlabel(r"$\tau$", fontsize=12)
    plt.ylabel(r"$\alpha(\tau)$", fontsize=12)
    plt.grid(True)
    plt.legend(fontsize=10)
    plt.show()

    dominant_harmonics = [(n, np.abs(A_n[n + n_max])) for n in range(-n_max, n_max + 1) if np.abs(A_n[n + n_max]) > tolerance]
    dominant_harmonics_sorted = sorted(dominant_harmonics, key=lambda x: x[1], reverse=True)
    dominant_harmonics_sorted[:10]
