import numpy as np
from scipy.integrate import quad
import pandas as pd

def integrand(theta: float | int, k: float | int) -> float:
    """
    Pendulum function that goes in the integral.
    """

    return 1 / np.sqrt(1 - k**2 * np.sin(theta)**2)

# Function to calculate the integral for a given alpha_0
def calculate_integral(alpha_0) -> float:
    """
    Actual integral calculation.
    """

    k = np.sin(alpha_0 / 2)
    
    # Numerical integration using quad
    result, _ = quad(integrand, 0, np.pi/2, args=(k))

    return result

if __name__ == "__main__":

    # Values of alpha_0 (displacement angle)
    alpha_0_values_deg = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]  # Degrees
    alpha_0_values_rad = np.radians(alpha_0_values_deg)

    # Calculate integrals for each alpha_0
    integrals = [calculate_integral(alpha_0) for alpha_0 in alpha_0_values_rad]

    df = pd.DataFrame({
        'alpha_0 (degrees)': alpha_0_values_deg,
        'alpha_0 (radians)': alpha_0_values_rad,
        'Integral Value': integrals
    })

    print(df)
