import numpy as np
import matplotlib.pyplot as plt

# Load the average face and flattened faces (assumed to be in the given directory)
Average_Face = np.load('Average_landmarks/average_face.npy')  # Shape (n_features,)
Flattened_Faces = np.load('Average_landmarks/Flattened_Faces.npy')  # Shape (n_samples, n_features)

Flattened_Faces_centered = Flattened_Faces - Average_Face.ravel()

U_svd, S_svd, Vt_svd = np.linalg.svd(Flattened_Faces_centered, full_matrices=False)
explained_variance_svd = (S_svd**2) / np.sum(S_svd**2)

cov_matrix = np.cov(Flattened_Faces_centered.T)

eigvals, eigvecs = np.linalg.eigh(cov_matrix)
print("Covariance_matrix shape:", cov_matrix.shape)

sorted_indices = np.argsort(eigvals)[::-1]
eigvals = eigvals[sorted_indices]
eigvecs = eigvecs[:, sorted_indices]
print("Eigenvalues shape:", eigvals.shape)
print("Eigenvectors shape:", eigvecs.shape)

explained_variance_ed = eigvals / np.sum(eigvals)
print("Covariance_matrix shape:", cov_matrix.shape)

num_components = 16
U_k_ed = eigvecs[:, :num_components]
S_k_ed = eigvals[:num_components]

np.save('U_k_ed.npy', U_k_ed)
np.save('S_k_ed.npy', S_k_ed)

plt.figure(figsize=(8, 5))
plt.plot(np.cumsum(explained_variance_svd), label="SVD Explained Variance", marker='o')
plt.plot(np.cumsum(explained_variance_ed), label="ED Explained Variance", marker='x')
plt.xlabel("Number of Principal Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("PCA: SVD vs Eigen Decomposition")
plt.legend()
plt.grid()
plt.show()

