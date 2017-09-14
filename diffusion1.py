import numpy as np
import matplotlib.pyplot as plt

def initialBell(x):
    return np.where(x%1.<0.5, np.power(np.sin(2*x*np.pi),2),0)

d =0.6
nx = 40
x = np.linspace(0.0,1.0,nx+1)
phi=initialBell(x)
phiNew=phi.copy()


nt = 40

for n in xrange(0,nt):
    for j in xrange(0,nx):
        phiNew[j] = phi[j] + d*(phi[j+1] - 2*phi[j]+phi[j-1])
    
    phiNew[0] = phi[0] + d*(phi[1] - 2*phi[0]+phi[nx-1])
    phiNew[nx] = phiNew[0]
    
    phi = phiNew.copy()


plt.plot(x, initialBell(x), 'k', label='analytic')
plt.plot(x,phi,'b',label='CTCS, d=0.2')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0,linestyle=':',color='black')
plt.show()
