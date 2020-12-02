from qutip import *
import numpy as np
import matplotlib.pyplot as plt

w01=5 * 2 * np.pi
w12=4.7*2*np.pi
detuning=np.linspace(-0.15,0.15,30)
w01d=w01
w12ds=w12+detuning
# w01d=w01+0.02*2*np.pi
# w12d=w12+0.03*2*np.pi
for w12d in w12ds:
    sRate=20  # simple rate
    H0=Qobj([[0,0,0],[0,w01,0],[0,0,w01+w12]])
    H01=Qobj([[0,1,0],[1,0,0],[0,0,0]])
    H12=Qobj([[0,0,0],[0,0,1],[0,1,0]])
    t_p=20# pulse time
    delay=20
    buffer=10
    t_t=2*buffer+5*t_p+4*delay# ramsey time
    t_ts=np.linspace(0,t_t,sRate*t_t+1)

    # print(t_r)
    # H=H0+H01+H12
    # print(H)
    ramsey=np.zeros(sRate*t_t+1)
    se=np.zeros(sRate*t_t+1)
    def pulse(t,area):#方波
        amp=area/t
        return amp



    for i,t in enumerate(t_ts):
        if 0<t<=buffer:
            ramsey[i]=0
            se[i]=0
        elif buffer<t<=buffer+t_p:
            ramsey[i]=pulse(t_p,np.pi/2)
            se[i]=0
        elif buffer+t_p<t<=buffer+t_p+delay:
            ramsey[i]=0
            se[i]=0
        elif buffer+t_p+delay<t<=buffer+2*t_p+delay:
            ramsey[i]=0
            se[i]=pulse(t_p,np.pi/2)
        elif buffer+2*t_p+delay<t<=buffer+2*t_p+2*delay:
            ramsey[i]=0
            se[i]=0
        elif buffer+2*t_p+2*delay<t<=buffer+3*t_p+2*delay:
            ramsey[i]=0
            se[i]=pulse(t_p,np.pi)
        elif buffer+3*t_p+2*delay<t<=buffer+3*t_p+3*delay:
            ramsey[i]=0
            se[i]=0
        elif buffer+3*t_p+3*delay<t<=buffer+4*t_p+3*delay:
            ramsey[i]=0
            se[i]=pulse(t_p,np.pi/2)
        elif buffer+4*t_p+3*delay<t<=buffer+4*t_p+4*delay:
            ramsey[i]=0
            se[i]=0
        elif buffer+4*t_p+4*delay<t<=buffer+5*t_p+4*delay:
            ramsey[i]=pulse(t_p,np.pi/2)
            se[i]=0
        elif buffer+5*t_p+4*delay<t<=2*buffer+5*t_p+4*delay:
            ramsey[i]=0
            se[i]=0
    c_ops=[]
    ramsey=ramsey*np.cos(w12d*t_ts)
    se=se*np.cos(w01d*t_ts)
    H=[H0,[H01,se],[H12,ramsey]]
    d0=basis(3,0)*basis(3,0).dag()
    d1=basis(3,1)*basis(3,1).dag()
    d2=basis(3,2)*basis(3,2).dag()
    output=mesolve(H,basis(3,1),t_ts,c_ops=c_ops,e_ops=[d0,d1,d2])
    e0=output.expect[0]
    e1=output.expect[1]
    e2=output.expect[2]

    fig, axes = plt.subplots(1, 1, figsize=(10, 6))
    axes.plot(t_ts, e0,label='0')
    axes.plot(t_ts, e1,label='1')
    axes.plot(t_ts, e2,label='2')
    axes.legend(loc=0)
    axes.set_xlabel('time')
    axes.set_ylabel('population')
    axes.set_title('three levels')
    plt.show()
    # fig, axes = plt.subplots(1, 1, figsize=(10, 6))
    # axes.plot(t_ts, ramsey,label='ramsey')
    # axes.plot(t_ts, se,label='se')
    # axes.legend(loc=0)
    # axes.set_xlabel('time')
    # axes.set_ylabel('amp')
    # axes.set_title('pulse')
    # plt.show()