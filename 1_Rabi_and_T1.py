import numpy as np
from qutip import *
import matplotlib.pyplot as plt
import cmath
a=tensor(create(2),qeye(2))
adag=a.dag()
sigmap=tensor(qeye(2),sigmap())
sigmam=tensor(qeye(2),sigmam())
sigmaz=tensor(qeye(2),sigmaz())
sigmax=tensor(qeye(2),sigmax())
sigmay=tensor(qeye(2),sigmay())#create和annihilate算子以及几个Pauli算子
estate=tensor(basis(2,1),basis(2,0))#0,e态ket
gstate=tensor(basis(2,0),basis(2,1))#1,g态ket  这里要注意num算子和Pauli算子在不同本征值态的定义的区别
gT=gstate.dag()#1,g bra
eT=estate.dag()#0,e bra
omega_r=1*2*np.pi#腔频
omega_q=1*2*np.pi#比特频率
g=0.05*2*np.pi#耦合起来强度
kappa = 0.005#腔耗散比率
gamma = 0.05#原子耗散比率

n_th_a = 0.0#周围温度
H0=omega_r*adag*a+omega_q*sigmaz/2
V=g*(adag*sigmam+a*sigmap)
H=H0+V#Hamiltonian
tlist = np.linspace(0,25,101)#时间序列
tlist1=np.linspace(0,200,101)
c_ops = []#耗散项

# cavity relaxation
rate = kappa * (1 + n_th_a)
if rate > 0.0:
    c_ops.append(np.sqrt(rate) * a)

# cavity excitation, if temperature > 0
rate = kappa * n_th_a
if rate > 0.0:
    c_ops.append(np.sqrt(rate) * adag)

# qubit relaxation
rate = gamma
if rate > 0.0:
    c_ops.append(np.sqrt(rate) * sigmam)

output=mesolve(H,gstate,tlist,c_ops,[adag*a,sigmap*sigmam])#求解主方程
n_c = output.expect[0]
n_a = output.expect[1]

fig, axes = plt.subplots(1, 1, figsize=(10,6))#Rabi图
axes.plot(tlist, n_c, label="Cavity")
axes.plot(tlist, n_a, label="Atom excited state")
axes.legend(loc=0)
axes.set_xlabel('Time')
axes.set_ylabel('Occupation probability')
axes.set_title('Vacuum Rabi oscillations')

output1=mesolve(omega_q*sigmaz/2,estate,tlist1,np.sqrt(rate) * sigmam,sigmap*sigmam)
n=output1.expect[0]
#print(n)

fig, axes = plt.subplots(1, 1, figsize=(10,6))#测T1？
axes.plot(tlist1, n, label="|0,e>")
axes.legend(loc=0)
axes.set_xlabel('Time')
axes.set_ylabel('Occupation probability')
axes.set_title('|e>')
plt.show()


