import numpy as np
from matplotlib import pyplot as plt, animation
from plot_utils import  plot_face

# Load the average face and flattened faces
Average_Face = np.load('Average_landmarks/average_face.npy')
U_k = np.load('U_k.npy')
S_k = np.load('S_k.npy')
Mode = 1

num_modes = 16
animation_frames = 30

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_title("Mode of Variation")
scatter = ax.scatter([], [], color='blue')

def update(frame, mode):
    sigma = np.sqrt(S_k[mode])
    a = np.linspace(-sigma, sigma, animation_frames)[frame]
    new_face = Average_Face.ravel() + a * U_k[:, mode]
    new_face = new_face.reshape(-1, 2)
    ax.clear()
    plot_face(ax, new_face, color='blue', title=f'Mode {mode + 1}')
    return scatter,

for mode in range(num_modes):
    ani = animation.FuncAnimation(fig, update, frames=animation_frames, fargs=(mode,), repeat=True)
    ani.save(f"mode_{mode+1}.gif", writer='pillow', fps=10)
    print(f'saving mode {mode}')

plt.show()

