import numpy as np
import matplotlib.pyplot as plt
from plot_utils import plot_face
import os
from Task1 import Register, plot_transformed_face
# from utils import save_landmarks, FaceRegister

Neutral_Face = np.load('images_landmarks/landmarks_0.npy')

# Folder containing landmarks .npy files
landmarks_folder = 'images_landmarks'  
transformed_landmarks_folder = 'transformed_landmarks'
Average_landmarks_folder = 'Average_landmarks'

# Create Output Folder if it doesn't exist
if not os.path.exists(transformed_landmarks_folder):
    os.makedirs(transformed_landmarks_folder)
    os.makedirs(Average_landmarks_folder)


# Initialize a list to hold the flattened transformed_face arrays
Flattened_Faces = [Neutral_Face.ravel()]

for filename in os.listdir(landmarks_folder):
    if filename != "landmarks_0.npy":
        face_path = os.path.join(landmarks_folder, filename)
        Face = np.load(face_path)
        transformed_face = Register(Neutral_Face, Face, Method="affine")
        Flattened_Faces.append(transformed_face.ravel())
        save_path = os.path.join(transformed_landmarks_folder, filename)
        np.save(save_path, transformed_face)
        print(f'plotting {filename}')
        # plot_transformed_face(Face, Neutral_Face, transformed_face)

Flattened_Faces = np.array(Flattened_Faces)
average_face = np.mean(Flattened_Faces, axis=0).reshape(-1, 2)

filename = os.path.join(Average_landmarks_folder, "average_face.npy")
np.save(filename, average_face)  

filename = os.path.join(Average_landmarks_folder, "Flattened_Faces.npy")
np.save(filename, Flattened_Faces)  

print('plotting avg face')
fig, ax = plt.subplots(figsize=(5, 5))
plot_face(ax, average_face, color='purple', title='Average Face')
plt.show()
