import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import cmath
import math
from matplotlib import cm
# 基于PRL 123,127202(2019)
pi=np.pi
kappa=2e6*pi*880


gamma=2e6*pi*0.071
alpha=2e6*pi*1.1
beta=2e6*pi*15
omega_c=2e9*pi*4.724
omegas=2e9*pi*np.linspace(4.4,5,1001)
omega_ms=2e9*pi*np.linspace(4.4,5,1001)
l=len(omegas)
lm=len(omega_ms)
Ss=np.zeros([l,lm])
Sp=np.zeros([l,lm])
#
# Gamma=2e6*pi*7
# J=2e6*pi*25.5

Gamma=2e6*pi*0
J=2e6*pi*25.5
# Gamma=2e6*pi*30.5
# J=2e6*pi*5.5
# J=2e6*pi*0

# Gamma=2e6*pi*7.9
# J=2e6*pi*7.9
# Gamma=np.sqrt(3)*J
# J=np.sqrt(3)*Gamma


# S11
for i in range(l):
    for k in range(lm):
        a=(1+kappa/(1j*(omegas[i]-omega_c)-(kappa+beta)-(J)**2/(1j*(omegas[i]-omega_ms[k])-(alpha+gamma))))
        Ss[i][k]=10*math.log(abs(1+kappa/(1j*(omegas[i]-omega_c)-(kappa+beta)-(1j*J+Gamma)**2/(1j*(omegas[i]-omega_ms[k])-(alpha+gamma)))),10)
        if 180*math.atan(a.imag/a.real)<180 and 180*math.atan(a.imag/a.real)>-180:
            Sp[i][k]=180*math.atan(a.imag/a.real)
        if 180*math.atan(a.imag/a.real)<-180:
            Sp[i][k] = 180 * math.atan(a.imag / a.real)+180
        if 180*math.atan(a.imag/a.real)>180:
            Sp[i][k] = 180 * math.atan(a.imag / a.real) - 180


extent=(min(omega_ms)/(2e9*pi), max(omega_ms)/(2e9*pi), min(omegas)/(2e9*pi), max(omegas)/(2e9*pi))
plt.figure(figsize=(9, 9))
ax1 = plt.subplot(111)
gci = ax1.imshow(Ss, extent=extent, origin='lower', aspect='auto')
cbar = plt.colorbar(gci)
cbar.set_label('111')
ax1.set_xlabel('omega_m[GHz]')
ax1.set_ylabel('probe frequency [GHz]')
plt.show()

# extent=(min(omega_ms)/(2e9*pi), max(omega_ms)/(2e9*pi), min(omegas)/(2e9*pi), max(omegas)/(2e9*pi))
# plt.figure(figsize=(9, 9))
# ax2 = plt.subplot(111)
# gci2 = ax2.imshow(Sp, extent=extent, origin='lower', aspect='auto')
# cbar = plt.colorbar(gci2)
# cbar.set_label('111')
# ax2.set_xlabel('omega_m[GHz]')
# ax2.set_ylabel('probe frequency [GHz]')
# plt.show()
#
# fig, axes = plt.subplots(1, 1, figsize=(10, 6))
# axes.plot(omega_ms/(2e9*pi),Sp[:,200])
# axes.legend(loc=0)
# axes.set_xlabel('frequency')
# axes.set_ylabel('S11')
# axes.set_title('S11')
# plt.show()
# fig, axes = plt.subplots(1, 1, figsize=(10, 6))
# axes.plot(omega_ms/(2e9*pi),Ss[:,200])
# axes.legend(loc=0)
# axes.set_xlabel('frequency')
# axes.set_ylabel('S11')
# axes.set_title('S11')
# plt.show()