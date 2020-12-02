import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import cmath

omega_ms=np.linspace(0,2,201)
omega_c=1
g=0.15

a=tensor(destroy(2),qeye(2))
adag=a.dag()
c=tensor(qeye(2),destroy(2))
cdag=c.dag()
Es=[]
# 不考虑耗散的情况
for omega_m in omega_ms:
    H=(omega_c*adag*a+omega_m*cdag*c+g*(adag*c+a*cdag))
    E=[H.eigenenergies()[1],H.eigenenergies()[2]]
    Es.append(E)

fig, axes = plt.subplots(1, 1, figsize=(10, 6))
axes.plot(omega_ms-omega_c, Es)
axes.legend(loc=0)
axes.set_xlabel('omega_m')
axes.set_ylabel('prob frequency')
axes.set_title('level')
plt.show()
