import numpy as np


a = 3.1
w = 1
b = 1.8
t = 3,1

# Equações horárias da velocidade, derivadas das equações de posição
Vx = -a*np.sin(t)
Vy = a*np.cos(t)
Vz = 2*b*t

v = np.array([Vx, Vy, Vz])
print(np.linalg.norm(v))
 
