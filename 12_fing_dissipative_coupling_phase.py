import matplotlib.pyplot as plt
import numpy as np
import math as m
import cmath as cm
import skrf as rf
import time
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
MHz=1e6*2*np.pi
GHz=1e9*2*np.pi
omega_c=8.2741*GHz
kappa_in=8.22*MHz
ktime=5.44*MHz**2
kplus=3.6*MHz
kappa=kappa_in+kplus
fre_start=8.2*GHz
fre_stop=8.34*GHz
number=6001
frequencys1=np.linspace(fre_start, fre_stop, number)
frequencys2=np.linspace(8*GHz,8.6*GHz,6001)
lf=len(frequencys1)
lf2=len(frequencys2)




''' find the parameters of cavity'''
# Se= np.loadtxt(r'C:\Users\Administrator\Desktop\data\20200921\two_ports_to_find_dissipative_ele_6.5\S21_0_11.4.txt')
# Ss=np.zeros(lf)
# for i in range(lf):
#     S=np.sqrt(ktime)/(-1j*(frequencys1[i]-omega_c)+kappa/2)
#     Ss[i]=rf.mag_2_db(np.abs(S))
#
# def func(x,c,omegac, gamma_in,gtime,gplus):
#     return c+rf.mag_2_db(np.abs(np.sqrt(gtime*MHz**2)/(-1j*(x-omegac*GHz)+(gamma_in+gplus)*MHz/2)))
# popt, pcov = curve_fit(func, frequencys1, Se,bounds=([0,8,0,0,0],[20.,9.,10.,10.,20. ]))
# print(popt)
#
# fig, axes = plt.subplots(1, 1, figsize=(10, 6))
# axes.plot(frequencys1/GHz, Ss-13,label='simulation')
# axes.plot(frequencys1/GHz,Se,label='experiment')
# axes.legend(loc=0)
# axes.set_xlabel('frequency')
# axes.set_ylabel('S21')
# axes.set_title('S21')
# plt.show()


'''find the parameter'''
# Sm= np.loadtxt(r'C:\Users\Administrator\Desktop\data\20200921\two_ports_to_find_dissipative_ele_6.5\S21_5.544_5.txt')
Ss1=np.zeros(lf)
omega_m=8.2747*GHz
gamma=1.6*MHz
# g=7.5*MHz
# for i in range(lf):
#     S=np.sqrt(ktime)/(-1j*(frequencys1[i]-omega_c)+kappa/2+g**2/(-1j*(frequencys1[i]-omega_m)+gamma/2))
#     Ss1[i]=rf.mag_2_db(np.abs(S))
# def func1(x,c, omegac,omegam,gammax,gg):
#     return c+rf.mag_2_db(np.abs(np.sqrt(ktime)/(-1j*(x-omegac*GHz)+kappa/2+(gg*MHz)**2/(-1j*(x-omegam*GHz)+gammax*MHz/2))))
# popt, pcov = curve_fit(func1, frequencys1, Sm, bounds=( [0,8,8,0,0],[5.,9.,9.,20.,10.]))
# print(popt)
# fig, axes = plt.subplots(1, 1, figsize=(10, 6))
# axes.plot(frequencys1/GHz, Ss1-13,label='simulation')
# axes.plot(frequencys1/GHz,Sm,label='experiment')
# axes.legend(loc=0)
# axes.set_xlabel('frequency')
# axes.set_ylabel('S21')
# axes.set_title('S21')
# plt.show()


'''find the phase'''
# Sf= np.loadtxt(r'C:\Users\Administrator\Desktop\data\20200921\two_ports_to_find_dissipative_ele\S21_ele_10.91_1.txt')
omegam=np.linspace(fre_start, fre_stop, 401)
# omegam=np.linspace(8*GHz,8.6*GHz,601)
Gamma=8.15*MHz
g=1
current=np.linspace(5.5,5.7,401)
degree=m.pi/180
lm=len(omegam)
Ss2=np.zeros([lf,lm])
# start=time.time()
# for g in np.arange(1.5,2.1,0.1):
#     for k in range(0,181):
for i in range(lm):
    for j in range(lf):
        S=np.sqrt(ktime)/(-1j*(frequencys1[j]-omega_c+1j*kappa_in)+kappa/2+(g*MHz)**2*cm.exp(1j*120*degree)/(-1j*(frequencys1[j]-omegam[i]+1j*gamma)+gamma/2))
        # S=(np.sqrt(ktime)/(-1j*(frequencys1[j]-omega_c)+kappa/2+(g+1j*Gamma)**2/(-1j*(frequencys1[j]-omegam[i])+gamma/2)))
        Ss2[j][i]=rf.mag_2_db(np.abs(S))
extent=(min(omegam)/GHz, max(omegam)/GHz, min(frequencys1)/GHz, max(frequencys1)/GHz)
plt.figure(figsize=(6, 6))
ax1 = plt.subplot(111)
gci = ax1.imshow(Ss2, extent=extent, origin='lower', aspect='auto')
cbar = plt.colorbar(gci)
cbar.set_label('S_21')
ax1.set_xlabel('omega_m[GHz]')
ax1.set_ylabel('probe frequency [GHz]')
        # ax1.set_title()
#         plt.savefig(r'C:\Users\Administrator\Desktop\python\simulation_wxh\application\12_fing_dissipative_coupling_phase\g=%s\degree=%d.png' %(g ,k))

plt.show()
# C:\Users\Administrator\Desktop\python\simulation_wxh\application\12_fing_dissipative_coupling_phase
# print(Sf)
# def func2(x,y,c,gg,k,z):
#     return c+rf.mag_2_db(np.sqrt(ktime)/(-1j*(x-omega_c)+kappa/2+(gg*MHz)**2*cm.exp(1j*k*degree)/(-1j*(x-z*y*GHz)+gamma/2)))
# p1, success= leastsq(func2, args=(frequencys2, current,Sf))
#
# print(p1)
# print(Ss2.shape)
# print(Sf.shape)
# extent=(min(current), max(current), min(frequencys1)/GHz, max(frequencys1)/GHz)
# plt.figure(figsize=(6, 6))
# ax1 = plt.subplot(111)
# gci = ax1.imshow(Sf, extent=extent, origin='lower', aspect='auto')
# cbar = plt.colorbar(gci)
# cbar.set_label('S_21')
# ax1.set_xlabel('omega_m[GHz]')
# ax1.set_ylabel('probe frequency [GHz]')
# ax1.set_title()
# plt.show()
# stop=time.time()
# print(stop-start)

# def func3(x,omegam,gg,k):
#      return rf.mag_2_db(np.abs(np.sqrt(ktime)/(-1j*(x-omega_c*GHz)+kappa/2+(gg*MHz)**2*cm.exp(1j*k*degree)/(-1j*(x-omegam*GHz)+gamma*MHz/2))))
# popt, pcov = curve_fit(func3, frequencys2, Sf[:,201], bounds=( [8,0,0],[9.,5.,180.]))
# print(popt)
# Ss3=np.zeros(lf2)
# g=5*MHz
# gamma_1=7*MHz
# for i in range(lf2):
#     S=np.sqrt(ktime)/(-1j*(frequencys2[i]-8.267*GHz)+kappa/2+g**2*cm.exp(1j*150*degree)/(-1j*(frequencys2[i]-8.29*GHz)+gamma_1/2))
#     Ss3[i]=rf.mag_2_db(np.abs(S))
# #
# fig, axes = plt.subplots(1, 1, figsize=(10, 6))
# axes.plot(frequencys2/GHz, Ss3,label='simulation')
# axes.plot(frequencys2/GHz,Sf[:,201],label='experiment')
# axes.legend(loc=0)
# axes.set_xlabel('frequency')
# axes.set_ylabel('S21')
# axes.set_title('S21')
# # plt.savefig(r'C:\Users\Administrator\Desktop\python\simulation_wxh\application\12_fing_dissipative_coupling_phase\2D\degree=%d.png'%k)
# plt.show()