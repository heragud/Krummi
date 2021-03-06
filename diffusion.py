import numpy as np
import matplotlib.pyplot as plt

def initialBell(x):
    return np.where(x%1.<0.5, np.power(np.sin(2*x*np.pi),2),0)

d = 0.1   
nx = 40
c = 0.2
x = np.linspace(0.0,1.0,nx+1)
phi=initialBell(x)
phiNew=phi.copy()
phiOld=phi.copy()

nt = 40

for n in xrange(0,nt):
    for j in xrange(0,nx):
        phiNew[j] = phi[j] - d*(phi[j+1] - 2*phi[j]+phi[j-1])
    
    phiNew[0] = phi[0] - d*(phi[1] - 2*phi[0]+phi[nx-1])
    phiNew[nx] = phiNew[0]
    
    phiOld = phi.copy()
    phi = phiNew.copy()
    
u = 1.
dx = 1./nx
dt = c*dx/u
t = nt*dt

plt.plot(x, initialBell(x - u*t), 'k', label='analytic')
plt.plot(x,phi,'b',label='CTCS')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0,linestyle=':',color='black')
plt.show()
