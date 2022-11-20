import numpy as np
import matplotlib.pyplot as plt
import pandas as pan
import scipy.stats.mstats as ms
import pydataset as data

from pydataset import data
pydata=data()

cars=data('cars')
data('cars', show_doc=True)

print(cars.speed)
print(cars.dist)

#print("moyenne de la vitesse :",sum(cars.speed)/50) #moyenne de speed
#print("moyenne de la distance :",sum(cars.dist)/50) #moyenne de dist
#print("variance empirique de la vitesse",np.var(cars.speed)) #variance empirique de speed
#print("variance empirique de la distance",np.var(cars.dist)) #variance empirique de dist
#print("variance empirique nb de la vitesse",np.var(cars.speed, ddof=1)) #variance empirique nb de speed
#print("variance empirique nb de la distance",np.var(cars.dist, ddof=1)) #variance empirique nb de dist
#print("mediane de la vitesse",np.median(cars.speed))#medianne de speed
#print("mediane de la distance",np.median(cars.dist))#medianne de dist
#print("équart type de la vitesse",np.std(cars.speed))#équart type de speed
#print("équart type de la distance",np.std(cars.dist))#équart type de dist

#for i in [0.25,0.50,0.75]:
#   print("quartille", i, "de la vitesse",np.quantile(cars.speed, i,interpolation="lower"))#quartille i de speed

#for i in [0.25,0.50,0.75]:
#   print("quartille", i, "de la distance",np.quantile(cars.dist, i,interpolation="lower"))#quartille i de dist

#print(cars.describe())#fait tous ce que l'on a fait plus haut
#print(plt.hist(cars.speed, color="blue")) #affiche l'histogramme de la vitesse

##################################-- TP 1.2

iris=data('iris')
#data('iris', show_doc=True)

#print(plt.pie(iris["Species"].value_counts(), labels = ["Setosa", "Versicolor", "Virginica"]))#diagramme circulaire des espèces
#print(iris.describe()) # descriptions de iris
#print(plt.boxplot(iris["Sepal.Length"])) #diagramme à moustache de "Sepal.Length"

##################################-- TP 1.3
x = np.array([1,8,5,1])
y = np.array([0,1,3,5,7,9])

#pair = []
#impair = []

#for i in y:
#    if(i>=1):
#        pair.append(i)
#    else:
#        impair.append(i)

#print(pair)

#X = np.repeat(x, reshape(1,4), 25, axis=0).reshape(100)
#print(X)


##################################-- TP 1.4
x = np.array([1,8,5,1,3,5])
y = np.array([0,1,3,5,7,9])

moyX=(sum(x)/6)
moyY=(sum(y)/6)

#print(moyX, moyY)

#plt.plot(x,y)#La commande retourne une erreur car les deux vecteursne sont pas de meme dimension
plt.scatter(moyX, moyY, c="red")
plt.scatter(x,y)
print(np.corrcoef(x,y))

##################################-- TP 1.5

women=data('women')

#plt.scatter(women.height, women.weight)

##################################-- TP 1.6

Don=pan.read_csv("http://math.univ-lyon1.fr/~dabrowski/Donnees.csv",sep="\t")

#plt.scatter(women.height, women.weight)
#plt.boxplot()


























