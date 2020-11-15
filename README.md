## MONOGRAFIA 
Programas em python para um breve estudo sobre a estrutura das Estrelas Compactas


## Objetivos
Estudar brevemente:
<li> O processo de formação e evolução estelar, bem como a formação dos objetos compactos </li>
<li> A estrutura, a composição e as características peculiares das estrelas compactas </li>


## Metodologia
<li> Derivar as equações de estrutura a partir do formalismo clássico</li>
<li> Encontrar a EoS exata para uma AB/EN composta por um gás de Fermi de elétrons/nêutrons degenerados  à <img src="https://render.githubusercontent.com/render/math?math=T = 0"> K</li>
<li> Derivar as EoS's politrópicas a partir dos limites não-relativístico e ultra-relativístico da EoS exata.</li>
<li> Derivar EoS politrópica para regime qualquer de velocidades</li>
<li> Implementar uma rotina do método de Runge Kutta de 4ª ordem em Python3 para resolver as equações de estrutura numericamente a partir do formalismo clássico e a partir das equações TOV, bem como para solução numérica das EoS's</li>


## Equação de Estrutura
<h1>Formalismo clássico</h1>
<img src="https://render.githubusercontent.com/render/math?math=\frac{dp(r)}{dr}=-\frac{G\epsilon(r)M(r)}{c^2 r^2}\\ \frac{dM(r)}{dr} = \frac{4\pi r^2\epsilon(r)}{c^2}">

<h1>Equações TOV</h1>
<img src="https://render.githubusercontent.com/render/math?math=\frac{dp(r)}{dr}= -  \frac{GM(r)\epsilon(r)}{c^2r^2}\Big[1+\frac{p(r)}{\epsilon(r)}\Big]\Big[1+\frac{4\pi r^3p(r)}{M(r)c^2}\Big]\Big[{1-\frac{2GM(r)}{c^2r}}\Big]^{-1}">




## Equação de estado - Gás de Fermi
<h1>Anã Branca</h1>
<li>Pressão dominada por um gás quântico de elétrons livres e completamente degenerados</li>
<img src="https://render.githubusercontent.com/render/math?math=p(k_F) = \frac{\epsilon_0}{24}\Big[(2x^3 - 3x)\sqrt{(1 + x^2)} + 3senh^{-1}(x)\Big]">
<li>Densidade de energia dominada pelos nucleões</li>
<img src="https://render.githubusercontent.com/render/math?math=\epsilon(k)_{N} = x^3\frac{m_e^3m_{N}c^5}{3\pi^2\hbar^3}\Big(\frac {A}{Z}\Big)">
onde <img src="https://render.githubusercontent.com/render/math?math=\epsilon_0 = \frac{m_e^4c^5}{\pi^2\hbar^3}">


<h1>Estrela de Nêutrons</h1>
<li>Pressão dominada por um gás quântico de nêutrons livres e completamente degenerados</li>
<img src="https://render.githubusercontent.com/render/math?math=p(k_F) = \frac{\epsilon_0}{24}\Big[(2x^3 - 3x)\sqrt{(1 + x^2)} + 3senh^{-1}(x)\Big]">
<li>Densidade de energia dominada pelos nêutrons</li>
<img src="https://render.githubusercontent.com/render/math?math=\epsilon(k)_{N} = x^3\frac{m_e^3m_{N}c^5}{3\pi^2\hbar^3}\Big(\frac {A}{Z}\Big)">
onde <img src="https://render.githubusercontent.com/render/math?math=\epsilon_0 = \frac{m_N^4c^5}{\pi^2\hbar^3}">



## Método de Runge Kutta de 4 ordem para um sistema acoplado de EDO 

dP/dr = f(r, P(r), M(r)) <br/>
dM/dr = g(r, P(r), M(r)) <br/>
P(r0) = P0 > 0 <br/>
M(x0) = 0 <br/>

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
