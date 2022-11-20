import numpy as np
import matplotlib.pyplot as plt
import pandas as pan
import scipy.stats.mstats as ms
import pydataset as data

from scipy.stats import bernoulli, binom, geom, poisson; import scipy.stats as st
from datetime import datetime

'''____________________________________________________________________________'''
'''Exo 2.1'''
'''____________________________________________________________________________'''

'''
#Renvoie la racine carré de (x^2 + y^2)
def r(x,y):
    z = np.sqrt(x**2+y**2)
    return(z)

def g(N,p,k):
    fonction = ((np.math.factorial(N))/((np.math.factorial(k)*(np.math.factorial(N-k)))))*(p**k)*(1-p)**(N-k)
    return(fonction)
'''

'''____________________________________________________________________________'''
'''Exo 2.2'''
'''____________________________________________________________________________'''

'''
N=10**4
t0 = datetime.now()
s=0
for i in range(1, N):
    if(i%2==0):
        s=s+i**2
t1=datetime.now()
t=np.arange(1,N)
s2=np.sum(t[t%2==0]**2)
t2=datetime.now()
print("Valeur obtenus :\n s = ",s,"temps : ",t1-t0,"\n s2 = ",s2,"temps : ", t2-t1,"\n")

def somme_carre_inverse(nb):
    somme=0
    for i in range(1, nb):
        if(i%2==1):
            somme=somme+(1/(i**2))
    return(somme)
'''

'''____________________________________________________________________________'''
'''Exo 2.3'''
'''____________________________________________________________________________'''

'''
n, p = 10, 0.25
ProbasB=binom.pmf(range(n+1),n, p)
plt.bar(range(n+1), ProbasB, width=0.1)
plt.show()

n, p = 10, 0.5
ProbasB=binom.pmf(range(n+1),n, p)
plt.bar(range(n+1), ProbasB, width=0.1)
plt.show()

n, p = 100, 0.25
ProbasB=binom.pmf(range(n+1),n, p)
plt.bar(range(n+1), ProbasB, width=0.5)
plt.show()

p = 2
ProbasB=poisson.pmf(range(10), p)
plt.bar(range(10), ProbasB, width=0.5)
plt.show()

p = 10
ProbasB=poisson.pmf(range(20), p)
plt.bar(range(20), ProbasB, width=0.5)
plt.show()

p = 0.75
ProbasB=geom.pmf(range(10), p)
plt.bar(range(10), ProbasB, width=0.5)
plt.show()

p = 0.25
ProbasB=geom.pmf(range(25), p)
plt.bar(range(25), ProbasB, width=0.5)
plt.show()

n,q=50,0.2
s,t=250,0.04
u,v=500, 0.02
p=10
ProbasB=binom.pmf(range(25),n, q)
plt.bar(range(25), ProbasB, width=0.5)
ProbasB=binom.pmf(range(25),s,t)
plt.bar(range(25), ProbasB, width=0.5)
ProbasB=binom.pmf(range(25),u, v)
plt.bar(range(25), ProbasB, width=0.5)
ProbasB=geom.pmf(range(25), p)
plt.bar(range(25), ProbasB, width=0.5)
plt.show()

n,p = 10,0.5
b=binom.rvs(n,p,size=1000)
tab=pan.crosstab(b, columns="freq",normalize=True).values
x=range(int(min(tab)), int(min(tab))+len(tab))
plt.bar(x,np.reshape(tab,len(tab)), width=0.05)
plt.plot(x, binom.pmf(x,n,p), 'r+')
plt.title("Diagramme en baton d'une simulation de la loi B(10,0.5)")

'''
'''____________________________________________________________________________'''
'''Exo 2.4'''
'''____________________________________________________________________________'''

'''
n, p = 10, 0.25
ProbasB=binom.cdf(range(50),n, p)
plt.step(range(n+1), ProbasB)
plt.show()

n, p = 50, 0.2
ProbasB=binom.cdf(range(n+1),n, p)
plt.step(range(n+1), ProbasB)
q = 3
ProbasB=poisson.cdf(range(n+1), q)
plt.step(range(n+1), ProbasB)
plt.show()
'''

'''____________________________________________________________________________'''
'''Exo 2.5'''
'''____________________________________________________________________________'''
'''
u = st.uniform.rvs(0,1,size=1000)
u[1:10];m = np.mean(u)
print("Moyenne empirique :",m)
plt.hist(u)


U = st.uniform.rvs(-3,6,size=10000)
plt.hist(U)
V=U[U>0]

plt.hist(V,density=True)
x=np.linspace(-1,4,500)
plt.plot(x,st.uniform.pdf(x,0,3),color="red")
'''
'''____________________________________________________________________________'''
'''Exo 2.6'''
'''____________________________________________________________________________'''

U=st.uniform.rvs(size=10000,loc=-1,scale=2)
V=st.uniform.rvs(size=10000,loc=-1,scale=2)
S=U**2+V**2; Cas=(S<1)
U0=U[Cas]; V0 = V[Cas]

plt.axis('equal')
plt.plot(U,V,marker=',',linestyle='')
plt.plot(U0,V0,marker=',',linestyle='')
plt.show()

valeur = np.sqrt(U0**2+V0**2)
plt.hist(valeur, density=True)
plt.show()

valeur2 = (np.sqrt(-np.log(valeur)))*(U0/valeur)
plt.hist(valeur2, density=True)
plt.show()














    
