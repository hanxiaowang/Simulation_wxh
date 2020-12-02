import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from matplotlib import *
import cmath as cm
import math as m
plt.rc('figure', max_open_warning = 0)
degree=m.pi/180
GHz= 1e9*2*np.pi
MHz=1e6*2*np.pi
a = tensor(destroy(2), qeye(2))
adag = a.dag()
b=tensor(qeye(2),destroy(2))
bdag=b.dag()
omega_c=8.2*GHz
omega_ms=np.linspace(8.1,8.3,201)*GHz
alpha=8*MHz
beta=1.7*MHz
# alpha=0*MHz
# beta=0*MHz
k=130
g=10*MHz
# J=np.abs(g*m.cos(k/2*degree))
# Gamma=np.abs(g*m.sin(k/2*degree))

# for k in range(181):
E1s = []
E2s = []
J = -g * m.cos(k / 2 * degree)
Gamma = g * m.sin(k / 2 * degree)
for i in range(len(omega_ms)):
    H1=(omega_c-1j*alpha)*adag*a+(omega_ms[i]-1j*beta)*bdag*b+g*(adag*b+cm.exp(1j*degree*k)*a*bdag)
    H2=(omega_c-1j*alpha)*adag*a+(omega_ms[i]-1j*beta)*bdag*b+(J-1j*Gamma)*(adag*b+a*bdag)
    # E1 = [H1.eigenenergies()[0],H1.eigenenergies()[1], H1.eigenenergies()[2],H1.eigenenergies()[3]]
    # E2 = [H2.eigenenergies()[0],H2.eigenenergies()[1], H2.eigenenergies()[2],H2.eigenenergies()[3]]
    E1 = [H1.eigenenergies()[1], H1.eigenenergies()[2]]
    E2 = [H2.eigenenergies()[1], H2.eigenenergies()[2]]
    E1s.append(np.abs(E1))
    E2s.append(np.abs(E2))
fig, axes = plt.subplots(1, 1, figsize=(10, 6))
axes.plot(omega_ms/GHz,E1s,label='H1')
axes.plot(omega_ms/GHz,E2s,label='H2')
axes.legend(loc=0)
axes.set_xlabel('frequency')
axes.set_ylabel('S21')
axes.set_title(k)
# plt.savefig(r'C:\Users\Administrator\Desktop\python\simulation_wxh\application\13_two_different_kinds_of_dissipative_coupling\k=%s'%k)

plt.show()
# print(E1s)