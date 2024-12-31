import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    theta = np.pi / 6
    tau_period = 1.3 * 2 * np.pi
    omega = 2 * np.pi / tau_period

    tau = np.linspace(0, tau_period, 500)

    alpha_0 = theta / 2 * (np.exp(1j * omega * tau) + np.exp(-1j * omega * tau)).real

    plt.figure(figsize=(8, 5))
    plt.plot(tau, alpha_0, label=r"$\alpha^{(0)}(\tau)$ (Bezdimensiju)", linewidth=2)
    plt.xlabel(r"$\tau$", fontsize=12)
    plt.ylabel(r"$\alpha(\tau)$", fontsize=12)
    plt.grid(True)
    plt.legend(fontsize=10)
    plt.show()
