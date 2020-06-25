import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#Primer punto

rho_w=1

def resistividad(m,phi):
	return (rho_w*phi**(-m))

phi=np.linspace(0.01,1,100)
plt.plot(np.log(phi),np.log(resistividad(1.2,phi)),label="m=1.2")
plt.plot(np.log(phi),np.log(resistividad(1.3,phi)),label="m=1.3")
plt.plot(np.log(phi),np.log(resistividad(1.4,phi)),label="m=1.4")
plt.plot(np.log(phi),np.log(resistividad(1.5,phi)),label="m=1.5")
plt.plot(np.log(phi),np.log(resistividad(1.6,phi)),label="m=1.6")
plt.plot(np.log(phi),np.log(resistividad(1.7,phi)),label="m=1.7")
plt.plot(np.log(phi),np.log(resistividad(1.8,phi)),label="m=1.8")
plt.plot(np.log(phi),np.log(resistividad(1.9,phi)),label="m=1.9")
plt.plot(np.log(phi),np.log(resistividad(2.0,phi)),label="m=2.0")
plt.plot(np.log(phi),np.log(resistividad(2.1,phi)),label="m=2.1")
plt.plot(np.log(phi),np.log(resistividad(2.2,phi)),label="m=2.2")
plt.plot(np.log(phi),np.log(resistividad(2.3,phi)),label="m=2.3")
plt.plot(np.log(phi),np.log(resistividad(2.4,phi)),label="m=2.4")
plt.plot(np.log(phi),np.log(resistividad(2.5,phi)),label="m=2.5")
plt.show()

rho_1=1000
rho_2=1

def serie(phi):
	return (rho_1+(rho_2-rho_1)*phi)

def paralelo(phi):
	para=((rho_1*rho_2)/(phi*rho_1 + (1-phi)*rho_2))
	return para

plt.plot(phi,serie(phi),c="blue",label="serie")
plt.plot(phi, paralelo(phi),c="red",label="paralelo")
plt.plot(phi, resistividad(1,phi),c="red",label="m=1")
plt.plot(phi, resistividad(2,phi),c="red",label="m=2")
plt.yscale('log')

plt.show()

















