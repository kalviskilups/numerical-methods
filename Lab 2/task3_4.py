import math
import matplotlib.pyplot as plt

# Constants
L_over_s = 1.3
k = 1 / L_over_s
tol = 1e-10
max_iter = 100


def f(lambda_):
    return lambda_ - math.sinh(k * lambda_)


def df(lambda_):
    return 1 - k * math.cosh(k * lambda_)


def bisection_method(a, b):
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        return None, []
    approximations = []
    for iteration in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        approximations.append(c)
        if abs(fc) < tol or (b - a) / 2 < tol:
            return c, approximations
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return c, approximations


def secant_method(x0, x1):
    approximations = [x0, x1]
    for iteration in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        if abs(f1 - f0) < tol:
            return None, approximations
        x_new = x1 - f1 * (x1 - x0) / (f1 - f0)
        approximations.append(x_new)
        if abs(f(x_new)) < tol:
            return x_new, approximations
        x0, x1 = x1, x_new
    return x_new, approximations


def newton_method(x0):
    approximations = [x0]
    for iteration in range(max_iter):
        f0 = f(x0)
        df0 = df(x0)
        if abs(df0) < tol:
            return None, approximations
        x_new = x0 - f0 / df0
        approximations.append(x_new)
        if abs(f(x_new)) < tol:
            return x_new, approximations
        x0 = x_new
    return x_new, approximations


# Bisection method initial values
lambda_bisection, approx_bisect = bisection_method(1.5, 2.0)

# Secant method initial values
lambda_secant, approx_secant = secant_method(1.5, 2.0)

# Newtona method initial value
lambda_newton, approx_newton = newton_method(1.75)

# Assume that the exact value is the one found by Newton's method
lambda_exact = lambda_newton

# Error calculation
errors_bisect = [abs(l - lambda_exact) for l in approx_bisect]
errors_secant = [abs(l - lambda_exact) for l in approx_secant]
errors_newton = [abs(l - lambda_exact) for l in approx_newton]

# Error graph
plt.figure(figsize=(8, 6))
plt.semilogy(
    range(1, len(errors_bisect) + 1), errors_bisect, "o-", label="Bisekcijas metode"
)
plt.semilogy(
    range(1, len(errors_secant) + 1), errors_secant, "s-", label="Sekantes metode"
)
plt.semilogy(
    range(1, len(errors_newton) + 1), errors_newton, "^-", label="Ņūtona metode"
)
plt.xlabel("Iterāciju skaits")
plt.ylabel("Kļūda (logaritmiskā mērogā)")
plt.legend()
plt.grid(True)
plt.show()

# Calculate the results
a_bisection = 1 / (2 * lambda_bisection)
a_secant = 1 / (2 * lambda_secant)
a_newton = 1 / (2 * lambda_newton)

print(a_bisection, a_secant, a_newton)
