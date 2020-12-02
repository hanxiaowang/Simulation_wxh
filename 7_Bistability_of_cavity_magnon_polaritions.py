import matplotlib.pyplot as plt
from qutip import *
import numpy as np
import cmath
import math
from matplotlib import cm
import sympy as sp
#PRL 120,057202(2018)


# 变drive功率
# gamma=10.65
# c=-4
# delta=17.2
# # D=np.zeros(351)
# D=[]
# D1=[]
# D2=[]
# P0=[]
# P1=[]
# P2=[]
# P=np.linspace(0,350,351)
# # Delta=[]
# for i in range(0,351):
#     Delta = sp.Symbol('Delta')
#     f=Delta**3+2*Delta**2*delta+Delta*(delta**2+(gamma/2)**2)-c*P[i]
#     Delta=sp.solve(f)
#     if abs(sp.im(Delta[0]))>1e-8:
#         pass
#     else:
#         D.append(sp.re(Delta[0]))
#         P0.append(P[i])
#
#     if abs(sp.im(Delta[1]))>1e-8:
#         pass
#     else:
#         D1.append(sp.re(Delta[1]))
#         P1.append(P[i])
#
#     if abs(sp.im(Delta[2]))>1e-8:
#         pass
#     else:
#         D2.append(sp.re(Delta[2]))
#         P2.append(P[i])
# # # print(Delta,type(Delta)
# # # print(D)
# # # print(shape(P))
# # # print(shape(D))
# # # print(shape(D1))
# # # print(shape(D2))
# fig, axes = plt.subplots(1, 1, figsize=(10,6))
# # axes.plot(P, D, label="0")
# # axes.plot(P, D1, label="1")
# # axes.plot(P, D2, label="2")
# plt.scatter(P0, D,label='0')
# plt.scatter(P1, D1,label='1')
# plt.scatter(P2, D2,label='2')
# axes.legend(loc=0)
# axes.set_xlabel('Power')
# axes.set_ylabel('Delta_LP')
# axes.set_title('delta_LP=17.2,c=-4')
# plt.show()



#变drive频率
gamma=10.65
c=-3.6
dbm=21
P=10**(dbm/10)
D=[]
D1=[]
D2=[]
delta0=[]
delta1=[]
delta2=[]
# D=np.zeros(121)
# D1=np.zeros(121)
# D2=np.zeros(121)
delta=np.linspace(60,-60,121)
for i in range(0,121):
    Delta=sp.Symbol('Delta')
    f = Delta ** 3 + 2 * Delta ** 2 * delta[i] + Delta * (delta[i] ** 2 + (gamma / 2) ** 2) - c * P
    Delta=sp.solve(f)
    if abs(sp.im(Delta[0]))>1e-8:
        pass
    else:
        D.append(sp.re(Delta[0]))
        delta0.append(delta[i])

    if abs(sp.im(Delta[1]))>1e-8:
        pass
    else:
        D1.append(sp.re(Delta[1]))
        delta1.append(delta[i])

    if abs(sp.im(Delta[2]))>1e-8:
        pass
    else:
        D2.append(sp.re(Delta[2]))
        delta2.append(delta[i])
# print(D1)
    # D.append(-abs(Delta[0]))
    # D1.append(-abs(Delta[1]))
    # D2.append(-abs(Delta[2]))
    # D[i]=Delta[0]
    # D1[i]=Delta[1]
    # D2[i]=Delta[2]
#     D1.append(Delta[1])
# print(np.real(D1[0]),type(D1[0]))
fig, axes = plt.subplots(1, 1, figsize=(10,6))
# axes.plot(delta, D, label="0")
# axes.plot(delta, D1, label="1")
# axes.plot(delta, D2, label="2")
plt.scatter(delta0, D,label='0')
plt.scatter(delta1, D1,label='1')
plt.scatter(delta2, D2,label='2')
axes.legend(loc=0)
axes.set_xlabel('delta')
axes.set_ylabel('Delta_LP')
axes.set_title('P=21,c=-3.6')
plt.show()