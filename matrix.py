import numpy as np
import matplotlib.pyplot as plt

# Sample matrix (square or rectangular)
A = np.array([[3, 1],
              [1, 3]])

# --- SVD ---
U, S, VT = np.linalg.svd(A)
print("SVD:")
print("U matrix:\n", U)
print("Singular values:", S)
print("V^T matrix:\n", VT)

# --- Eigenvalues and Eigenvectors ---
eigvals, eigvecs = np.linalg.eig(A)
print("\nEigen Decomposition:")
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)

# --- Optional: Visualization for 2x2 matrix ---
def plot_vectors(vecs, colors, alpha=1):
    for i in range(len(vecs)):
        plt.quiver(0, 0, vecs[i][0], vecs[i][1],
                   color=colors[i], angles='xy', scale_units='xy', scale=1, alpha=alpha)

if A.shape == (2, 2):
    # Original space
    original_vecs = np.eye(2)
    transformed_vecs = A @ original_vecs

    plt.figure(figsize=(8, 6))
    plot_vectors(original_vecs, ['gray', 'gray'], alpha=0.5)
    plot_vectors(transformed_vecs.T, ['blue', 'blue'], alpha=0.8)
    plot_vectors(eigvecs.T, ['red', 'green'], alpha=0.8)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title("Matrix Action, Eigenvectors (Red/Green), and Transformed Axes (Blue)")
    plt.gca().set_aspect('equal')
    plt.legend(['Original basis', 'Transformed basis', 'Eigenvectors'])
    plt.show()
