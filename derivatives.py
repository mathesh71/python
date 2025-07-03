import numpy as np
import matplotlib.pyplot as plt
from autograd import grad
import autograd.numpy as anp

# Define the function
def f(x):
    return x**3 - 3*x**2 + 2

# Derivative using autograd
df = grad(f)

# Range of x values
x_vals = np.linspace(-2, 4, 400)
y_vals = f(x_vals)

# Point to evaluate derivative/gradient at
x0 = 1.0
y0 = f(x0)
slope = df(x0)

# Tangent line at x0
tangent_line = slope * (x_vals - x0) + y0

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.plot(x_vals, tangent_line, '--', label=f'Tangent at x={x0}', color='orange')
plt.scatter(x0, y0, color='red', zorder=5)
plt.quiver(x0, y0, 1, slope, angles='xy', scale_units='xy', scale=1, color='green', label='Gradient vector')

plt.title("Function, Derivative (Tangent), and Gradient Visualization")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
