## MONOGRAFIA 
Programas em python para um breve estudo sobre a estrutura das Estrelas Compactas


## Objetivos
Estudar brevemente:
<li> O processo de formação e evolução estelar, bem como a formação dos objetos compactos </li>
<li> A estrutura, a composição e as características peculiares das estrelas compactas </li>


## Metodologia
<li> Derivar as equações de estrutura a partir do formalismo clássico</li>
<li> Encontrar a EoS exata para uma AB/EN composta por um gás de Fermi de elétrons/nêutrons degenerados  à $T = 0$ K</li>
<li> Derivar as EoS's politrópicas a partir dos limites não-relativístico e ultra-relativístico da EoS exata.</li>
<li> Derivar EoS politrópica para regime qualquer de velocidades</li>
<li> Implementar uma rotina do método de Runge Kutta de 4ª ordem em Python3 para resolver as equações de estrutura numericamente a partir do formalismo clássico e a partir das equações TOV, bem como para solução numérica das EoS's</li>


## Equação de estado - Gás de Fermi
<img src="https://render.githubusercontent.com/render/math?math=e^{i \pi} = -1">







## Método de Runge Kutta de 4 ordem para um sistema acoplado de EDO 

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
