import numpy as np
import matplotlib.pyplot as plt
from utils import FaceRegister
from plot_utils import plot_face

def Register(Neutral_Face, Face, Method="affine"):
    faceRegister = FaceRegister(Face, Neutral_Face, Method)
    transformation_matrix = faceRegister.register()
    return np.dot(Face, transformation_matrix.T)


def plot_transformed_face(Face, Neutral_Face, transformed_face):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    plot_face(axes[0], Face, color='blue', title='Original Face')
    plot_face(axes[1], Neutral_Face, color='green', title='Neutral Face')
    plot_face(axes[2], transformed_face, color='red', title='Transformed Face')
    plt.show()
