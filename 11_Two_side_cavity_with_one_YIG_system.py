import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import cmath
# from matplotlib import cm
import math as m
import cmath as cm
import skrf as rf
import time
pipi=2*np.pi
degree=m.pi/180
omega_c=8.286e9*pipi
# omega_m=omega_c

kappa_int=1.08e6*pipi
kappa_add=1e6*pipi
# kappa_add=np.linspace(0,30,300)*1e6*pipi
gamma=3.25e6*pipi
# gamma=20e6*pipi
# g=9.6*1e6*pipi
g=1.6*1e6*pipi
# kappa_in=1.31e6*pipi
kappa_1=1e6*pipi
kappa_2=kappa_1
kappa=kappa_int+kappa_1+kappa_2+kappa_add
f_start=8e9*pipi
f_stop=8.6e9*pipi
number=601
omega_m=np.linspace(f_start,f_stop,number)
omega=np.linspace(8.1e9,8.5e9,401)*pipi
S21=np.zeros([len(omega),len(omega_m)])
t_start=time.time()
# for k in range(len(kappa_add)):
#     kappa = kappa_int + kappa_1 + kappa_2 + kappa_add[k]
for i in range(len(omega)):
    for j in range(len(omega_m)):
        s=rf.mag_2_db(abs(np.sqrt(kappa_1*kappa_2)/(-1j*(omega[i]-omega_c)+kappa/2+(g)**2*cm.exp(1j*120*degree)/(-1j*(omega[i]-omega_m[j])+gamma/2))))

        S21[i][j]=s

extent=(min(omega_m)/(1e9*pipi), max(omega_m)/(1e9*pipi), min(omega)/(1e9*pipi), max(omega)/(1e9*pipi))
plt.figure(figsize=(6, 6))
ax1 = plt.subplot(111)
gci = ax1.imshow(S21, extent=extent, origin='lower', aspect='auto')
cbar = plt.colorbar(gci)
cbar.set_label('S21[dB]',size=20)
cbar.ax.tick_params(labelsize=20)
ax1.set_xlabel('magnon frequency[GHz]',size=20)
ax1.set_ylabel('probe frequency [GHz]',size=20)
ax1.set_title('S21',size=20)
plt.tick_params(labelsize=20)


# plt.savefig(r'C:\Users\Administrator\Desktop\python\simulation_wxh\application\Eleventh_Two_side_cavity_with_one_YIG_system\kappa_add\kappa_add=%s.png' % (kappa_add / (1e6 * pipi)))
# plt.savefig(r'C:\Users\Administrator\Desktop\python\simulation_wxh\application\Eleventh_Two_side_cavity_with_one_YIG_system\gamma\gamma=%s.png' % (gamma/ (1e6 * pipi)))

t_stop=time.time()
print(t_stop-t_start)
plt.show()

