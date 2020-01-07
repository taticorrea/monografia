import numpy as np 
import matplotlib.pyplot as plt

######## CODIGO ANTIGO POR PREUCUÇÃO ########

################# Caso relativistico ################# 
alfa = 1.473
beta = 52.46
gamma = 4/3 
u = 1/gamma
N = 10000
#h = 4.84484484484483 #(10-14)
h = 0.86008919 #(10-15)
#h = 1.508151 #(10-16)

#dp/dr = -alfap^(1/gamma)M/r^2
#f = f(r,P,M)
def f(r,P,M):
    return (-alfa*np.power(P,u)*M)/np.power(r,2)

#dM/dr = beta r^2p^(1/gamma)
#g = g(r,P,M)
def g(r,P,M):
    return beta*np.power(r,2)*np.power(P,u)

#Listas que não ficam salvas
P = np.empty(N)
M = np.empty(N)
r = np.empty(N)
k1P = np.empty(N)
k2P = np.empty(N)
k3P = np.empty(N)
k4P = np.empty(N)
k1M = np.empty(N)
k2M = np.empty(N)
k3M = np.empty(N)
k4M = np.empty(N)

#Listas que ficam salvas e são plotadas
eixoP = []
eixoM = []
eixor = []
eixok1P = []
eixok2P = []
eixok3P = []
eixok4P = []
eixok1M = []
eixok2M = []
eixok3M = []
eixok4M = []

#Condicoes iniciais
r[0] = 0.0000000000000000000001
P[0] = 1E-15
M[0] = 0

#Condicao para P[R] > 0
#while(P[9999] > 0):
    #Iteracao
for i in np.arange(N-1):                #(N-1) pois as listas com N elementos tem a forma u[0]..u[N-1]
    #Calculando valores de r e salvando na lista
    r[i+1] = r[i] + h                   
    eixor.insert(i,r[i+1])              
    #Calculando coef. RK4 e salvando em listas
    k1P[i] = h*f(r[i],       P[i],              M[i] )
    eixok1P.insert(i,k1P[i])
    k1M[i] = h*g(r[i],       P[i],              M[i])
    eixok1M.insert(i,k1M[i])
    k2P[i] = h*f(r[i] + h/2, P[i] + k1P[i]/2, M[i] + k1M[i]/2)
    eixok2P.insert(i,k2P[i])  
    k2M[i] = h*g(r[i] + h/2, P[i] + k1P[i]/2, M[i] + k1M[i]/2)
    eixok2M.insert(i,k2M[i])
    k3P[i] = h*f(r[i] + h/2, P[i] + k2P[i]/2, M[i] + k2M[i]/2)
    eixok3P.insert(i,k3P[i])  
    k3M[i] = h*g(r[i] + h/2, P[i] + k2P[i]/2, M[i] + k2M[i]/2)
    eixok3M.insert(i,k3M[i]) 
    k4P[i] = h*f(r[i] + h,   P[i] + k3P[i], M[i] + k3M[i])
    eixok4P.insert(i,k4P[i])  
    k4M[i] = h*g(r[i] + h,   P[i] + k3P[i], M[i] + k3M[i])
    eixok4M.insert(i,k4M[i])
    #Calculando Pn+1, Mn+1 e salvando nas respectivas listas
    P[i+1] = P[i] + (1/6)*(k1P[i] + 2*k2P[i] + 2*k3P[i] + k4P[i])
    eixoP.insert(i,P[i])
    M[i+1] = M[i] + (1/6)*(k1M[i] + 2*k2M[i] + 2*k3M[i] + k4M[i])
    eixoM.insert(i,M[i])

#Printando valores
print('\n Caso Relativístico \n')
print ('P(0) : ',P[0])
print ('P[R] : ',P[9999])
print ('M[R] : ',M[9999])
print ('R    : ',r[9999])


################# Caso NAO relativistico ################# 
alfan = 0.05 
betan = 0.005924
gamman = 5/3 
un = 1/gamman
Nn = 10000           #numero de pontos no grafico
hn =  1.0614          #C.I P[0] = 10E-15
#hn = 1.336139         #C.I P[0] = 10E-16

#dp/dr = -alfap^(1/gamma)M/r^2
#f = f(r,P,M)
def fn(rn,Pn,Mn):
    return (-alfan*np.power(Pn,un)*Mn)/np.power(rn,2)

#dM/dr = beta r^2p^(1/gamma)
#g = g(r,P,M)
def gn(rn,Pn,Mn):
    return betan*np.power(rn,2)*np.power(Pn,un)

#Listas que não ficam salvas
Pn = np.empty(Nn)
Mn = np.empty(Nn)
rn = np.empty(Nn)
k1Pn = np.empty(Nn)
k2Pn = np.empty(Nn)
k3Pn = np.empty(Nn)
k4Pn = np.empty(Nn)
k1Mn = np.empty(Nn)
k2Mn = np.empty(Nn)
k3Mn = np.empty(Nn)
k4Mn = np.empty(Nn)

#Listas que ficam salvas e são plotadas
eixoPn = []
eixoMn = []
eixorn = []
eixok1Pn = []
eixok2Pn = []
eixok3Pn = []
eixok4Pn = []
eixok1Mn = []
eixok2Mn = []
eixok3Mn = []
eixok4Mn = []

#Condicoes iniciais
rn[0] = 0.0000000000000000000001
Pn[0] = 1E-15
Mn[0] = 0

#Condicao para P[R] > 0
#while(P[9999] > 0):
    #Iteracao
for i in np.arange(Nn-1):                #(N-1) pois as listas com N elementos tem a forma u[0]..u[N-1]
    #Calculando valores de r e salvando na lista
    rn[i+1] = rn[i] + hn                   
    eixorn.insert(i,rn[i+1])              
    #Calculando coef. RK4 e salvando em listas
    k1Pn[i] = hn*fn(rn[i],       Pn[i],              Mn[i] )
    eixok1Pn.insert(i,k1Pn[i])
    k1Mn[i] = hn*gn(rn[i],       Pn[i],              Mn[i])
    eixok1Mn.insert(i,k1Mn[i])
    k2Pn[i] = hn*fn(rn[i] + hn/2, Pn[i] + k1Pn[i]/2, Mn[i] + k1Mn[i]/2)
    eixok2Pn.insert(i,k2Pn[i])  
    k2Mn[i] = hn*gn(rn[i] + hn/2, Pn[i] + k1Pn[i]/2, Mn[i] + k1Mn[i]/2)
    eixok2Mn.insert(i,k2Mn[i])
    k3Pn[i] = hn*fn(rn[i] + hn/2, Pn[i] + k2Pn[i]/2, Mn[i] + k2Mn[i]/2)
    eixok3Pn.insert(i,k3Pn[i])  
    k3Mn[i] = hn*gn(rn[i] + hn/2, Pn[i] + k2Pn[i]/2, Mn[i] + k2Mn[i]/2)
    eixok3Mn.insert(i,k3Mn[i]) 
    k4Pn[i] = hn*fn(rn[i] + hn,   Pn[i] + k3Pn[i], Mn[i] + k3Mn[i])
    eixok4Pn.insert(i,k4Pn[i])  
    k4Mn[i] = hn*gn(rn[i] + hn,   Pn[i] + k3Pn[i], Mn[i] + k3Mn[i])
    eixok4Mn.insert(i,k4Mn[i])
    #Calculando Pn+1, Mn+1 e salvando nas respectivas listas
    Pn[i+1] = Pn[i] + (1/6)*(k1Pn[i] + 2*k2Pn[i] + 2*k3Pn[i] + k4Pn[i])
    eixoPn.insert(i,Pn[i])
    Mn[i+1] = Mn[i] + (1/6)*(k1Mn[i] + 2*k2Mn[i] + 2*k3Mn[i] + k4Mn[i])
    eixoMn.insert(i,Mn[i])

#Printando valores
print('\n Caso não Relativístico\n')
print ('P(0) : ',Pn[0])
print ('P[R] : ',Pn[9999])
print ('M[R] : ',Mn[9999])
print ('R    : ',rn[9999])

#Plotando grafico 
plt.figure(1) #cria janela
plt.subplot(2,1,1)
# primeiro grafico
plt.plot(eixor,eixoP,color ='red',label ='Caso Relativístico') 
plt.plot(eixorn,eixoPn,color ='blue',label ='Caso não Relativístico') 
plt.legend()
#plt.xlabel('Radius (km)')
plt.title('Estrela Anã Branca - Gás de Fermi de elétrons',fontsize=9.5)
plt.ylabel('Pressão')
#segundo grafico
plt.subplot(2,1,2)
plt.plot(eixor,eixoM,color ='green',label ='Caso Relativístico')
plt.plot(eixorn,eixoMn,color ='orange',label ='Caso não-Relativístico')
plt.legend()
plt.ylabel('Massa')
plt.xlabel('Raio (km)')


plt.legend()
plt.show()
