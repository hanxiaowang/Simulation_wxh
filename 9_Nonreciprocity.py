import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import skrf as rf
import cmath
from matplotlib import cm

pipi=2*np.pi
# frequencys=np.linspace(5.5e9,6.1e9,2001)*pipi
# omega_c=5.8e9*pipi
# kappa=1.3e9*pipi
# # kappa=1.3e6*pipi
# beta=32.6e6*pipi
# J=6.5e6*pipi
# Gamma=29e6*pipi
# alpha=5e6*pipi
# gamma=804*pipi
# omega_ms=np.linspace(5.5e9,6.1e9,2001)*pipi
# lf=len(frequencys)
# lm=len(omega_ms)
# S21=np.zeros([lf,lm])
# S12=np.zeros([lf,lm])
# s21=np.zeros(lm)
# for i in range(lf):
#     for j in range(lm):
#         S=1+kappa/(1j*(frequencys[i]-omega_c)-kappa-beta+(J-1j*Gamma)**2/(1j*(frequencys[i]-omega_ms[j])-alpha-gamma))
#         S21[i][j]=rf.mag_2_db(np.abs(S))
#
# extent=(min(omega_ms)/(1e9*pipi), max(omega_ms)/(1e9*pipi), min(frequencys)/(1e9*pipi), max(frequencys)/(1e9*pipi))
# plt.figure(figsize=(9, 9))
# ax1 = plt.subplot(111)
# gci = ax1.imshow(S21, extent=extent, origin='lower', aspect='auto')
# cbar = plt.colorbar(gci)
# cbar.set_label('S21')
# ax1.set_xlabel('omega_m[GHz]')
# ax1.set_ylabel('probe frequency [GHz]')
# plt.show()

# for i in range(lf):
#     for j in range(lm):
#         S=1+kappa/(1j*(frequencys[i]-omega_c)-kappa-beta+(J+1j*Gamma)**2/(1j*(frequencys[i]-omega_ms[j])-alpha-gamma))
#         S12[i][j]=rf.mag_2_db(np.abs(S))
#
# extent=(min(omega_ms)/(1e9*pipi), max(omega_ms)/(1e9*pipi), min(frequencys)/(1e9*pipi), max(frequencys)/(1e9*pipi))
# plt.figure(figsize=(9, 9))
# ax1 = plt.subplot(111)
# gci = ax1.imshow(S21, extent=extent, origin='lower', aspect='auto')
# cbar = plt.colorbar(gci)
# cbar.set_label('S12')
# ax1.set_xlabel('omega_m[GHz]')
# ax1.set_ylabel('probe frequency [GHz]')
# plt.show()
# for k in range(lm):
#     S = 1 + kappa / (1j * (frequencys[i] - omega_c) - kappa - beta + (J - 1j * Gamma) ** 2 / (
#                 1j * (frequencys[i] - omega_c) - alpha - gamma))
#     s21[k] = rf.mag_2_db(np.abs(S))
# fig, axes = plt.subplots(1, 1, figsize=(10, 6))
# axes.plot(frequencys-omega_c/(1e9*pipi), s21)
# axes.legend(loc=0)
# axes.set_xlabel('delta')
# axes.set_ylabel('S21')
# axes.set_title('S21')
# plt.show()


omega_c=4.724e9*pipi
kappa=880e6*pipi
# kappa=np.linspace(850,900,6)*1e6*pipi
beta=13e6*pipi
# beta=np.linspace(10,16,7)*1e6*pipi
J=7.9e6*pipi
Gamma=7.9e6*pipi
alpha=1.5e6*pipi
# alpha=np.linspace(0.9,2,12)*1e6*pipi
# gamma=0.071e6*pipi
gamma=np.linspace(0.065,0.075,11)*1e6*pipi
omega_ms=np.linspace(omega_c-0.2e9*pipi,omega_c+0.2e9*pipi,2001)
frequencys=np.linspace(omega_c-0.12e9*pipi,omega_c-0.1e9*pipi,2001)
lf=len(frequencys)
lm=len(omega_ms)
S21=np.zeros(lf)
S12=np.zeros(lf)
l=len(gamma)
# S21=np.zeros([lf,lm])
# S12=np.zeros([lf,lm])
# s21=np.zeros(lm)
# for i in range(lf):
#     for j in range(lm):
#         S=1+kappa/(1j*(frequencys[i]-omega_c)-kappa-beta+(J-1j*Gamma)**2/(1j*(frequencys[i]-omega_ms[j])-alpha-gamma))
#         S21[i][j]=rf.mag_2_db(np.abs(S))
# extent=(min(omega_ms-omega_c)/(1e9*pipi), max(omega_ms-omega_c)/(1e9*pipi), min(frequencys-omega_c)/(1e9*pipi), max(frequencys-omega_c)/(1e9*pipi))
# plt.figure(figsize=(9, 9))
# ax1 = plt.subplot(111)
# gci = ax1.imshow(S21, extent=extent, origin='lower', aspect='auto')
# cbar = plt.colorbar(gci)
# cbar.set_label('S21')
# ax1.set_xlabel('omega_m[GHz]')
# ax1.set_ylabel('probe frequency [GHz]')
# plt.show()

# for i in range(lf):
#     S=1+kappa/(1j*(frequencys[i]-omega_c)-kappa-beta+(J-1j*Gamma)**2/(1j*(frequencys[i]-4.833e9*pipi)-alpha-gamma))
#     S21[i]=rf.mag_2_db(np.abs(S))
# for i in range(lf):
#     S=1+kappa/(1j*(frequencys[i]-omega_c)-kappa-beta+(J+1j*Gamma)**2/(1j*(frequencys[i]-4.833e9*pipi)-alpha-gamma))
#     S12[i]=rf.mag_2_db(np.abs(S))
# fig, axes = plt.subplots(1, 1, figsize=(10, 6))
# axes.plot((frequencys-omega_c)/(1e9*pipi), S21,label='S21')
# axes.plot((frequencys-omega_c)/(1e9*pipi), S12,label='S12')
# axes.legend(loc=0)
# axes.set_xlabel('frequency')
# axes.set_ylabel('S')
# axes.set_title('S')
# plt.show()


for j in range(l):
    for i in range(lf):
        S=1+kappa/(1j*(frequencys[i]-omega_c)-kappa-beta+(J-1j*Gamma)**2/(1j*(frequencys[i]-4.615e9*pipi)-alpha-gamma[j]))
        S21[i]=rf.mag_2_db(np.abs(S))
    for i in range(lf):
        S=1+kappa/(1j*(frequencys[i]-omega_c)-kappa-beta+(J+1j*Gamma)**2/(1j*(frequencys[i]-4.615e9*pipi)-alpha-gamma[j]))
        S12[i]=rf.mag_2_db(np.abs(S))
    fig, axes = plt.subplots(1, 1, figsize=(10, 6))
    axes.plot((frequencys-omega_c)/(1e9*pipi), S21,label='S21')
    axes.plot((frequencys-omega_c)/(1e9*pipi), S12,label='S12')
    axes.legend(loc=0)
    axes.set_xlabel('frequency')
    axes.set_ylabel('S')
    axes.set_title(gamma[j]/(1e6*pipi))
    plt.savefig(r'C:\Users\Administrator\Desktop\python\simulation_wxh\application\Ninth_Nonreciprocity\gamma\kappa=%s.png'%(gamma[j]/(1e6*pipi)))
    # plt.show()