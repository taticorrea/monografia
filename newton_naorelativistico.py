import numpy as np 
import matplotlib.pyplot as plt

alfa = 0.05 
beta = 0.005924
gama = 5/3 
n = 10000           #numero de pontos no grafico
#h =                 #C.I P[0] = 10E-15
h = 1.336139         #C.I P[0] = 10E-16


def f(r,P,M):
    return -(alfa*(P**(1/gama))*M)/(r**2)

def g(r,P,M):
    return beta*(r**2)*(P**(1/gama))

r = np.empty(n)
P = np.empty(n)
M = np.empty(n)


r[0] = 0.00000000000000001
P[0] = 10**(-16)
M[0] = 0

def rk4():
  for i in range(n-1):

      k1 = h*f(r[i], P[i], M[i])
      l1 = h*g(r[i], P[i], M[i])

      k2 = h*f(r[i] + h/2, P[i] + k1/2, M[i] + l1/2)
      l2 = h*g(r[i] + h/2, P[i] + k1/2, M[i] + l1/2)

      k3 = h*f(r[i] + h/2, P[i] + k2/2, M[i] + l2/2)
      l3 = h*g(r[i] + h/2, P[i] + k2/2, M[i] + l2/2)

      k4 = h*f(r[i] + h, P[i] + k3, M[i] + l3)
      l4 = h*g(r[i] + h, P[i] + k3, M[i] + l3)

      k = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
      l = (1/6)*(l1 + 2*l2 + 2*l3 + l4)

      r[i+1] = r[i] + h
      P[i+1] = P[i] + k
      M[i+1] = M[i] + l

rk4()

plt.plot(r,M)
plt.show()
