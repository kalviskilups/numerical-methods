import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt


def small_angle_period() -> float:
    """
    Small angle approximation for the period.
    """

    return 2 * np.pi * np.sqrt(L / g)


def integrand(theta: float | int, k: float | int) -> float:
    """
    Pendulum function that goes in the integral.
    """

    return 1 / np.sqrt(1 - k**2 * np.sin(theta)**2)


def calculate_period(alpha_0) -> float:
    """
    Calculate the pendulum period for a given alpha_0.
    """

    k = np.sin(alpha_0 / 2)
    integral_value, _ = integrate.quad(integrand, 0, np.pi / 2, args=(k,))
    T = 4 * np.sqrt(L / g) * integral_value
    return T


if __name__ == "__main__":

    # Constants
    
    # Acceleration due to gravity (m/s^2)
    g = 9.81
    # Length of the pendulum (m)
    L = 1.0

    # Values of alpha_0 (displacement angle)
    alpha_values_deg = np.linspace(4, 90, 100)
    alpha_values_rad = np.radians(alpha_values_deg)

    # Calculate the period for each alpha_0 value
    periods = [calculate_period(alpha_0) for alpha_0 in alpha_values_rad]

    # Calculate the small-angle approximation (constant for all small alpha_0)
    T_small_angle = small_angle_period()

    # Plot the results
    plt.plot(alpha_values_deg, periods, label='Periods')
    plt.axhline(y=T_small_angle, color='r', linestyle='--', label='Mazu svārstību robeža')
    plt.xlabel(r'Sākuma leņķis $\alpha_0$ (grādi)')
    plt.ylabel(r'Periods T($\alpha_0$)')

    # Add legend and grid
    plt.legend()
    plt.grid(True)

    # Show the plot
    #plt.savefig("test.png")
    plt.show()
