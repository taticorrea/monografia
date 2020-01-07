# MONOGRAFIA

Programas em python para um Breve Estudo sobre a Estrutura de Estrelas Compactas





## Runge Kutta
dP/dr = f(r, P(r), M(r))
dM/dr = g(r, P(r), M(r))
P(r0) = P0
M(x0) = M0


k1 = h*f(rn, Pn, Mn)
l1 = h*g(rn, Pn, Mn)
k2 = h*f(rn + h/2, Pn + k1/2, Mn + l1/2)
l2 = h*g(rn + h/2, Pn + k1/2, Mn + l1/2)
k3 = h*f(rn + h/2, Pn + k2/2, Mn + l2/2)
l3 = h*g(rn + h/2, Pn + k2/2, Mn + l2/2)
k4 = h*f(rn + h, Pn + k3, Mn + l3)
l4 = h*g(rn + h, Pn + k3, Mn + l3)

k = (1/6) *(k1 + 2k2 + 2k3 + k4)
l = (1/6) *(l1 + 2l2 + 2l3 + l4)

rn+1 = rn + h
Pn+1 = Pn + k
Mn+1 = Mn + l

r(0) = 0.0000001
P(0) e [10^-16,10^-14]
M(0) = 0
