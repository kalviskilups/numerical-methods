import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipkinc

def integrand(theta: float | int, k: float | int) -> float:
    """
    Pendulum function that goes in the integral.
    """

    return 1 / np.sqrt(1 - k**2 * np.sin(theta)**2)

if __name__ == "__main__":

    # Compute the exact value of the integral using the incomplete elliptic integral
    alpha0 = np.pi / 3
    k = np.sin(alpha0 / 2)
    I_exact = np.sqrt(2) * ellipkinc(alpha0, k**2)
    print(f"Exact value of the integral (using incomplete elliptic integral): {I_exact:.10f}")

    # List of N values (number of intervals)
    N_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152]

    errors = []

    # Loop over N values to compute the integral and error
    for N in N_values:
        # Create array of theta values from 0 to alpha0
        theta = np.linspace(0, alpha0, N+1)
        # Evaluate the integrand at each theta
        f_theta = integrand(theta, k)
        # Apply the trapezoidal rule
        I_N = np.sqrt(2) * np.trapz(f_theta, theta)
        # Calculate the absolute error
        error = abs(I_N - I_exact)
        errors.append(error)
        print(f"N = {N:<5d} Integral = {I_N:.10f} Error = {error:.10e}")

    # Convert lists to numpy arrays for convenience
    N_values = np.array(N_values)
    errors = np.array(errors)

    # Compute logarithms of N and errors
    log_N = np.log(N_values)
    log_errors = np.log(errors)

    # Fit a straight line to the log-log data
    slope, intercept = np.polyfit(log_N, log_errors, 1)
    convergence_rate = -slope
    print(f"\nComputed convergence rate: {convergence_rate:.4f}")

    # Plotting the log-log plot
    plt.figure(figsize=(8, 6))
    plt.loglog(N_values, errors, 'o-', label='Kļūda')
    plt.xlabel('Intervālu skaits (N)')
    plt.ylabel('Absolūtā kļūda')
    plt.grid(True, which="both", ls="--")
    plt.legend()

    # Annotate the convergence rate on the plot
    plt.text(N_values[1], errors[1], f'Konverģences kļūdas kārta ≈ {convergence_rate:.4f}')
    plt.savefig('task_4.png')

    plt.show()