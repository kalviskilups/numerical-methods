import numpy as np
import matplotlib.pyplot as plt


def calculate_h(L_s_ratio: float) -> float:
    L: int = 1
    s: float = L / L_s_ratio
    a_L_ratio: float = 0.299
    a: float = a_L_ratio * L

    # Calculate the height difference
    h: float = a * (np.cosh(s / (2 * a)) - 1)
    return h


L_s_ratios = np.linspace(1.01, 3, 100)
h_values = [calculate_h(L_s) for L_s in L_s_ratios]

# Generate the graph
plt.figure(figsize=(8, 6))
plt.plot(L_s_ratios, h_values, label="h atkarība no $L/s$")
plt.xlabel("$L/s$ attiecība")
plt.ylabel("Augstuma starpība $h$")
plt.legend()
plt.grid(True)
plt.show()

# Show h value when L/s -> 1
h_near_1 = calculate_h(1.01)
print(f"Augstuma starpība h, kad L/s -> 1: {h_near_1:.6f} vienībās")

h_actual = calculate_h(1.3)
print(f"Augstuma starpība h (starp piekāršanas punktu un zemāko punktu) = {h_actual:.6f} vienībās")
