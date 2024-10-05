import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.interpolate import interp1d


def integrand(theta: float | int, k: float | int) -> float:
    """
    Pendulum function that goes in the integral.
    """

    return 1 / np.sqrt(1 - k**2 * np.sin(theta)**2)


def calculate_period(alpha_0):
    """
    Calculate the pendulum period for a given alpha_0.
    """

    k = np.sin(alpha_0 / 2)
    result, _ = quad(integrand, 0, np.pi / 2, args=(k))
    T = 4 * np.sqrt(L / g) * result
    return T

def alpha_t(t, alpha_0, T):
    """
    Approximate angular displacement as a function of time using sinusoidal-like behavior.
    """

    # Use modulo operation to repeat the periodic motion
    return alpha_0 * np.cos(2 * np.pi * (t % T) / T)


if __name__ == "__main__":

    # Constants

    # Acceleration due to gravity (m/s^2)
    g = 9.81
    # Length of the pendulum (m)
    L = 1.0
    # Initial angle in radians (pi/3)
    alpha_0 = np.pi / 3

    # Calculate the period for alpha_0 = pi/3
    T = calculate_period(alpha_0)
    print(f"Pendulum period for alpha_0 = pi/3: {T:.4f} seconds")

    t_values = np.linspace(0, 10, 50)

    # Compute the angular displacement alpha(t) over time
    alpha_values = alpha_t(t_values, alpha_0, T)

    # Interpolation using cubic splines to create a smooth line
    interpolator = interp1d(t_values, alpha_values, kind='cubic')
    t_smooth = np.linspace(0, 10, 1000)
    alpha_smooth = interpolator(t_smooth)

    # Plot the calculated points and the interpolated line
    plt.figure(figsize=(8, 6))
    plt.plot(t_values, np.degrees(alpha_values), 'ro', label='Aprēķinātie punkti')
    plt.plot(t_smooth, np.degrees(alpha_smooth), 'b-', label='Interpolētā līkne (Kubiskā splainu metode)')
    plt.xlabel('Laiks (s)')
    plt.ylabel(r'Leņķiskā novirze $\alpha(t)$ (leņķis grādos)')
    plt.title(r'Svārsta kustība: $\alpha(t)$ for $\alpha_0 = 60^\circ$ (10 seconds)')
    plt.grid(True)
    plt.legend()
    plt.show()
