import numpy as np 
import matplotlib.pyplot as plt


c=2.998E+10 #cm/s
m=9.1094E-28 #g
h=6.62607E-34 #J.s
herg=h*np.power(10,7) #erg.s
hcortado=herg/(2*np.pi) #erg.s
e_zero=1.4407405E+24 #ergs/cm³

#Listas que correspondem aos valores de x e y
eixox= []
eixoy= []

#Gerando os valores de k 
k = np.arange(0,2,0.0002)
for i in range( 0,len(k) ):
    valor = k[i]
    
    #Calculando os pontos para cada valor de k
    x= (3*e_zero)*((2*np.power(k[i],3) + k[i] )*( np.sqrt( 1+ np.power( k[i],2 ) ))- np.arcsinh(k[i])     )
    y= (e_zero/24)*((2*np.power(k[i],3) - 3*k[i] )*( np.sqrt( 1+ np.power( k[i],2 ) ))+ 3*np.arcsinh(k[i]) )
    
    #Salvando os pontos nas listas
    eixox.insert(i,x)
    eixoy.insert(i,y)
    
    #Cuspindo os pontos na tela
    print(f'Para k = 'f'{k[i]}'f', temos:({eixox[i]},{eixoy[i]})')

        
#Plotando e personalizando o gráfico
plt.plot(eixox,eixoy)
plt.title(r'P($\epsilon$)')
plt.xlabel('Densidade de energia (erg/cm³)')
plt.ylabel('Pressao')
plt.show()
