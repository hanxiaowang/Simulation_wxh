import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import cmath
from matplotlib import cm
import skrf as rf
from scipy.optimize import curve_fit
# Se= np.loadtxt(r'C:\Users\Administrator\Desktop\findingg.txt')
pipi=2*np.pi

# kappa_in=1.30554595e6*pipi
# kappa_int=1.09369e6*pipi
kappa_in=1.31e6*pipi
kappa_int=1.09e6*pipi


omega_c=8.2856e9*pipi
# omega_c=8.29e9*pipi
omega_m=8.28574e9*pipi
g=9.6e6*pipi
gamma=3.25e6*pipi
# g=5.5e6*pipi
# gamma=5e6*pipi
frequencys=np.linspace(8.2e9*pipi,8.35e9*pipi,10000)
lf=len(frequencys)
Ss=np.zeros(lf)
for i in range(lf):
    s=-1+kappa_in/(-1j*(frequencys[i]-omega_c)+(kappa_in+kappa_int)/2+g**2/(-1j*(frequencys[i]-omega_m)+gamma/2))
    Ss[i]=rf.mag_2_db(np.abs(s))
# def func(x,gg,gammam):
#     return rf.mag_2_db(np.abs(-1+kappa_in/(-1j*(x-omega_c)+(kappa_in+kappa_int)/2+(gg*1e6*pipi)**2/(-1j*(x-omega_m*1e9)+gammam*pipi*1e6/2))))
# popt, pcov = curve_fit(func, frequencys, Se, bounds=([1.,0.],[10.,10. ]))
# print(popt)
# print(pcov)

fig, axes = plt.subplots(1, 1, figsize=(10, 6))
axes.plot(frequencys/(1e9*pipi), Ss-0.04,label='simulation')
# axes.plot(frequencys/(1e9*pipi),Se,label='experiment')
# axes.plot(frequencys2/(1e9*pipi),)
axes.legend(loc=0)
axes.set_xlabel('frequency')
axes.set_ylabel('S11')
axes.set_title('S11')

plt.show()