import numpy as np
from scipy.integrate import quad
import pandas as pd


def integrand(theta: float | int, k: float | int) -> float:
    """
    Pendulum function that goes in the integral.
    """

    return 1 / np.sqrt(1 - k**2 * np.sin(theta)**2)


def calculate_integral_4_1_15(alpha_0, N=10) -> float:
    """
    Numerical integration using the modified trapezoidal rule (formula 4.1.15).
    """

    k = np.sin(alpha_0 / 2)
    theta_values = np.linspace(0, np.pi/2, N)
    h = theta_values[1] - theta_values[0]
    
    f_values = integrand(theta_values, k)
    integral = (3/2 * f_values[0] + 3/2 * f_values[-1] + np.sum(f_values[1:-1])) * h
    
    return integral


def calculate_integral_4_1_16(alpha_0: float | int, N: int = 10) -> float:
    """
    Numerical integration using the improved (formula 4.1.16).
    """

    k = np.sin(alpha_0 / 2)
    theta_values = np.linspace(0, np.pi/2, N)
    h = theta_values[1] - theta_values[0]
    
    f_values = integrand(theta_values, k)
    integral = (23/12 * f_values[0] + 7/12 * f_values[1] +
                np.sum(f_values[2:-2]) + 
                7/12 * f_values[-2] + 23/12 * f_values[-1]) * h
    
    return integral


def calculate_integral_gaussian(alpha_0: float | int) -> float:
    """
    Integral calculation using Gaussian quadrature.
    """

    k = np.sin(alpha_0 / 2)
    result, _ = quad(integrand, 0, np.pi/2, args=(k))
    return result


if __name__ == "__main__":

    # Values of alpha_0 (displacement angle in degrees)
    alpha_0_values_deg = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
    alpha_0_values_rad = np.radians(alpha_0_values_deg)

    # Calculate integrals for each alpha_0 using both methods
    integrals_4_1_15 = [calculate_integral_4_1_15(alpha_0) for alpha_0 in alpha_0_values_rad]
    integrals_4_1_16 = [calculate_integral_4_1_16(alpha_0) for alpha_0 in alpha_0_values_rad]
    integrals_gaussian = [calculate_integral_gaussian(alpha_0) for alpha_0 in alpha_0_values_rad]

    # Create a DataFrame for comparison
    df = pd.DataFrame({
        'alpha_0 (degrees)': alpha_0_values_deg,
        'alpha_0 (radians)': alpha_0_values_rad,
        'Integral 4.1.15': integrals_4_1_15,
        'Integral 4.1.16': integrals_4_1_16,
        'Integral Gaussian': integrals_gaussian
    })

    print(df)
