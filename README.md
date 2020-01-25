## MONOGRAFIA 

Programas em python para um Breve Estudo sobre a Estrutura das Estrelas Compactas

Python programs for a brief study of Compact Stars

## Método de Runge Kutta
Runge Kutta Method

dP/dr = f(r, P(r), M(r)) <br/>
dM/dr = g(r, P(r), M(r)) <br/>
P(r0) = P0 <br/>
M(x0) = M0 <br/>

k1 = h*f(rn, Pn, Mn) <br/>
l1 = h*g(rn, Pn, Mn) <br/>

k2 = h*f(rn + h/2, Pn + k1/2, Mn + l1/2) <br/>
l2 = h*g(rn + h/2, Pn + k1/2, Mn + l1/2) <br/>

k3 = h*f(rn + h/2, Pn + k2/2, Mn + l2/2) <br/>
l3 = h*g(rn + h/2, Pn + k2/2, Mn + l2/2) <br/>

k4 = h*f(rn + h, Pn + k3, Mn + l3) <br/>
l4 = h*g(rn + h, Pn + k3, Mn + l3) <br/>

k = (1/6) *(k1 + 2k2 + 2k3 + k4) <br/>
l = (1/6) *(l1 + 2l2 + 2l3 + l4) <br/>

rn+1 = rn + h <br/>
Pn+1 = Pn + k <br/>
Mn+1 = Mn + l <br/>
<br/><br/>

## Condições Iniciais
Initial Conditions


r(0) = 0.0000001 <br/>
P(0) e [10^-16,10^-14] <br/>
M(0) = 0
