import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import ellipk


def integrand(theta):
    """
    Function that goes in the trapezoidal rule.
    """

    numerator = np.cos(theta)
    denominator = np.sqrt(1 - (3/4) * np.sin(theta)**2)
    return numerator / denominator


if __name__ == "__main__":

    # Compute the exact value of the integral using elliptic integral
    alpha0 = np.pi / 3
    k = np.sin(alpha0 / 2)
    I_exact = np.sqrt(2) * ellipk(k**2)
    print(f"Exact value of the integral (using elliptic integral): {I_exact:.10f}")

    # List of N values (number of intervals)
    N_values = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

    errors = []

    # Loop over N values to compute the integral and error
    for N in N_values:
        # Create array of theta values from 0 to pi/2
        theta = np.linspace(0, np.pi/2, N+1)
        # Evaluate the integrand at each theta
        f_theta = integrand(theta)
        # Apply the trapezoidal rule
        I_N = np.sqrt(2) * np.trapz(f_theta, theta)
        # Calculate the absolute error
        error = abs(I_N - I_exact)
        errors.append(error)
        print(f"N = {N:<5d} Integral = {I_N:.10f} Error = {error:.10e}")

    # Plotting the error versus N on a log-log scale
    plt.figure(figsize=(8, 6))
    plt.loglog(N_values, errors, 'o-', label='Error')
    plt.xlabel('Intervālu skaits N')
    plt.ylabel('Kļūda')
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.show()

    # Convergence rate
    log_N = np.log(N_values)
    log_errors = np.log(errors)
    # Fit a straight line to the log-log data
    coefficients = np.polyfit(log_N, log_errors, 1)
    p = -coefficients[0]  # The negative of the slope
    print(f"Observed order of convergence p = {p:.2f}")
