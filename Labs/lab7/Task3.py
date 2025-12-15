import numpy as np

# Load the average face and flattened faces (assumed to be in the given directory)
Average_Face = np.load('Average_landmarks/average_face.npy')  # Shape (n_features,)
Flattened_Faces = np.load('Average_landmarks/Flattened_Faces.npy')  # Shape (n_samples, n_features)

print("Flattened_Faces shape:", Flattened_Faces.shape)
print("Average_Face shape:", Average_Face.ravel().shape)

Flattened_Faces_centered = Flattened_Faces - Average_Face.ravel()

if Flattened_Faces_centered.shape[0] < Flattened_Faces_centered.shape[1]:
    Flattened_Faces_centered = Flattened_Faces_centered.T

print("Flattened_Faces shape:", Flattened_Faces.shape)

U, S, Vt = np.linalg.svd(Flattened_Faces_centered, full_matrices=False)

num_components = 16
U_k = U[:, :num_components]
S_k = S[:num_components]

np.save('U_k.npy', U_k)
np.save('S_k.npy', S_k)

print("U shape:", U.shape)
print("S shape:", S.shape)
print("Vt shape:", Vt.shape)
