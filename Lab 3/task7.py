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

omega = (2 * D_e * k**2 / mu) ** 0.5

n_values = [0, 1, 2, 3, 4]
eigenenergies = []
for n in n_values:
    energy = hbar * omega * (n + 0.5) - (hbar * omega * (n + 0.5)) ** 2 / (4 * D_e)
    eigenenergies.append(energy)

eigenenergies_cm = [energy / cm_to_J for energy in eigenenergies]

print(eigenenergies_cm)

# Vērtības no 3. uzdevuma
harmonic_oscillator_energies = [0.4987, 1.4936, 2.4833, 3.4678, 4.4471]

scaling_factor_cm = (hbar * omega) / cm_to_J
harmonic_oscillator_energies_cm = [
    e * scaling_factor_cm for e in harmonic_oscillator_energies
]

print(harmonic_oscillator_energies_cm)

# Papilduzdevums
n_max = math.floor((math.sqrt(2 * mu * D_e) / (hbar * k)) - 0.5)

print(n_max)
