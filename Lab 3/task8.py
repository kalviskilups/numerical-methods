import math

hbar = 1.0545718e-34  # (J·s)
amu_to_kg = 1.6605e-27  # kg
cm_to_J = 1.986e-23  # cm^-1 uz J
D_e_cm = 79890  # cm^-1
D_e = D_e_cm * cm_to_J  # J
k_angstrom = 2.6889  # Å^-1
k = k_angstrom * 1e10  # m^-1
mass_nitrogen = 14  # amu
mu = (mass_nitrogen * amu_to_kg) / 2  # kg

n_max = math.floor((math.sqrt(2 * mu * D_e) / (hbar * k)) - 0.5)
print(n_max)
