import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import cmath
from matplotlib import cm
import skrf as rf
from scipy.optimize import curve_fit
Se= np.loadtxt(r'C:\Users\Administrator\Desktop\try1.txt')

pipi=2*np.pi
# kappa_in=1.30554595e6*pipi
# kappa_int=1.09094782e6*pipi

kappa_in=1.30554595e6*pipi
kappa_int=1.08869e6*pipi

fre_start=8.25e9*pipi
fre_stop=8.32e9*pipi
number=10001
omega_c=8.2855556e9*pipi
frequencys1=np.linspace(fre_start  ,fre_stop,number)
frequencys2=np.linspace(8.25e9*pipi,8.32e9*pipi,10000)
lf=len(frequencys1)
Ss=np.zeros(lf)
# Se=[]
for i in range(lf):
    S=-1+kappa_in/(-1j*(frequencys1[i]-omega_c)+(kappa_in+kappa_int)/2)
    Ss[i]=rf.mag_2_db(np.abs(S))

def func(x,gamma_in,gamma_int):
    return rf.mag_2_db(np.abs(-1+(gamma_in*pipi)/(-1j*(x-omega_c)+(gamma_in*pipi+gamma_int*pipi)/2)))
popt, pcov = curve_fit(func, frequencys2, Se,bounds=(-1,[ 20000000.,20000000.]))
print(popt/pipi)


fig, axes = plt.subplots(1, 1, figsize=(10, 6))
axes.plot(frequencys1/(1e9*pipi), Ss-0.07,label='simulation')
axes.plot(frequencys2/(1e9*pipi),Se,label='experiment')
# axes.plot(frequencys2/(1e9*pipi),)
axes.legend(loc=0)
axes.set_xlabel('frequency')
axes.set_ylabel('S11')
axes.set_title('S11')
plt.show()
# f1 = np.polyfit(frequencys2, Se, 3)
# a=np.poly1d(f1)
# print(a)