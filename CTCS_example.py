import numpy as np
import matplotlib.pyplot as plt

def initialBell(x):
    return np.where(x%1.<0.5, np.power(np.sin(2*x*np.pi),2),0)

nx = 40
c = 1
x = np.linspace(0.0,1.0,nx+1)
phi=initialBell(x)

phiOld=phi.copy()

nt = 40

for n in xrange(0,nt):
    for j in xrange(0,nx):
        phi[j] = phiOld[j] - 0.5*c*(phiOld[j+1] - phiOld[j-1])
    
    phi[0] = phiOld[0] - 0.5*c*(phiOld[1] - phiOld[nx-1])
    phi[nx] = phi[0]
    
    phiOld = phi.copy()
    
u = 1.
dx = 1./nx
dt = c*dx/u
t = nt*dt

plt.plot(x, initialBell(x - u*t), 'k', label='analytic')
plt.plot(x,phi,'b',label='FTCS')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0,linestyle=':',color='black')
plt.show()
