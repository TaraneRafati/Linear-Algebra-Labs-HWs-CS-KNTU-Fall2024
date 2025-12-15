import numpy as np

x_true = np.array([3, 1.5,-1.0, 2.4, -3, -.1, 2.2, 4.1, -3.2, 1.0])
n = x_true.size

m = 20
A = np.random.randn(m,n) 

y_true = A @ x_true

sigma = 0.01
measurement_noise = sigma * np.random.randn(m)
y_noisy = y_true + measurement_noise

errs = 0
for i in range(100):
    x_est = np.linalg.inv(A.T@A) @ A.T @ y_noisy
    errs += np.linalg.norm(x_est - x_true)
errs /= 100
print(errs)

