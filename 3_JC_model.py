import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from matplotlib import *
import cmath

a = tensor(destroy(2), qeye(2))
adag = a.dag()
sigmap = tensor(qeye(2), sigmap())
sigmam = tensor(qeye(2), sigmam())
sigmaz = tensor(qeye(2), sigmaz())
# omega_rs=np.linspace(0,1,10)
omega_qs = np.linspace(0, 1, 1000)
#gs=np.linspace(0,1,10)
omega_r = 1
#omega_q = 1
#for g in gs:
g = 0.15
Es = []
# for omega_r in omega_rs:
for omega_q in omega_qs:
    # for g in gs:
    H = omega_r * adag * a + omega_q * sigmaz + g * (adag * sigmam + a * sigmap)

    E=[H.eigenenergies()[1],H.eigenenergies()[2]]
    #E = H.eigenenergies()
    Es.append(E)
fig, axes = plt.subplots(1, 1, figsize=(10, 6))

axes.plot(omega_qs, Es)
axes.legend(loc=0)
axes.set_xlabel('')
axes.set_ylabel('f')
axes.set_title(g)
plt.show()