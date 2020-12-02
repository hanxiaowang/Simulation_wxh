import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import cmath
from matplotlib import cm
import skrf as rf
pi=np.pi



gamma_m=2e6*pi*1.5
g_m=2e6*pi*9.2
kappa_1=2e6*pi*1.72
kappa_2=2e6*pi*1.39
kappa_int=kappa_1+kappa_2-gamma_m
# kappa_int=2e6*pi*1.55
omega_c=2e9*pi*10.0317
omega_ms=2e9*pi*np.linspace(9.98,10.1,201)
lm=len(omega_ms)
omegas=2e9*pi*np.linspace(9.98,10.1,201)
l=len(omegas)
# print(kappa_int/(2e6*pi))
S_11s=np.zeros([l,lm])
S_22s=np.zeros([l,lm])
S_12s=np.zeros([l,lm])#S12=S21


# S11
# for i in range(l):
#     for j in range(lm):
#         a=(-1-2*kappa_1/(2j*(omegas[i]-omega_c)-(kappa_1+kappa_2+kappa_int)+g_m**2/(2j*(omegas[i]-omega_ms[j])-gamma_m)))
#         S_11s[i][j]=rf.mag_2_db(np.abs(a))
# extent=(min(omega_ms)/(2e9*pi), max(omega_ms)/(2e9*pi), min(omegas)/(2e9*pi), max(omegas)/(2e9*pi))
# plt.figure(figsize=(9, 9))
# ax1 = plt.subplot(111)
# gci = ax1.imshow(S_11s, extent=extent, origin='lower', aspect='auto')
# cbar = plt.colorbar(gci)
# cbar.set_label('S_11')
# ax1.set_xlabel('omega_m[GHz]')
# ax1.set_ylabel('probe frequency [GHz]')
# plt.show()



# #S22
# for i in range(l):
#     for j in range(lm):
#         S_22s[i][j]=(-1-2*kappa_2/(1j*(omegas[i]-omega_c)-(kappa_1+kappa_2+kappa_int)+g_m**2/(1j*(omegas[i]-omega_ms[j])-gamma_m))).real**2
# extent=(min(omega_ms)/(2e9*pi), max(omega_ms)/(2e9*pi), min(omegas)/(2e9*pi), max(omegas)/(2e9*pi))
# plt.figure(figsize=(9, 9))
# ax1 = plt.subplot(111)
# gci = ax1.imshow(S_22s, extent=extent, origin='lower', aspect='auto', cmap='hsv')
# cbar = plt.colorbar(gci)
# cbar.set_label('S_22')
# ax1.set_xlabel('omega_m[GHz]')
# ax1.set_ylabel('probe frequency [GHz]')
# plt.show()
# #


#S12=S21
for i in range(l):
    for j in range(lm):
        a=(-2*np.sqrt(kappa_1*kappa_2)/(1j*(omegas[i]-omega_c)-(kappa_1+kappa_2+kappa_int)+g_m**2/(1j*(omegas[i]-omega_ms[j])-gamma_m)))
        S_12s[i][j]=rf.mag_2_db(np.abs(a))
extent=(min(omega_ms)/(2e9*pi), max(omega_ms)/(2e9*pi), min(omegas)/(2e9*pi), max(omegas)/(2e9*pi))
plt.figure(figsize=(9, 9))
ax1 = plt.subplot(111)
gci = ax1.imshow(S_12s, extent=extent, origin='lower', aspect='auto')
cbar = plt.colorbar(gci)
cbar.set_label('S_12=S_21')
ax1.set_xlabel('omega_m[GHz]')
ax1.set_ylabel('probe frequency [GHz]')
plt.show()