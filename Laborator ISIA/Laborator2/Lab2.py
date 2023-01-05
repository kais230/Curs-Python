# IMPORT FUNCTII
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster,datasets


m1=np.array([[2,2,2],[3,3,3],[1,5,5]])
m2=np.array([[6,6,6],[1,1,1],[1,4,5]])
m3=np.array([[6,6,6],[1,1,1],[1,4,5]])

# GENERARE DATE
clust = datasets.make_biclusters([200,2],2)
# [200,2] se citeste ca 200 de esantioane cu 2 coordonate (ca sa poata fi desenate)
# 2 reprezinta numarul de clustere reale
# 4 este marimea zgomotului aplicat

# VIZUALIZARE DATE
data = clust[0] # clust[1] contine etichetele esantioanelor, dar nu sunt necesare pentru clustering
plt.figure(), plt.scatter(data[:,0],data[:,1])
plt.title('Punctele generate')

# CREARE OBIECT KMeans SI CLUSTERING PE DATELE GENERATE
km = cluster.KMeans(n_clusters = 2)
labels = km.fit_predict(clust[0])
# Metoda fit_predict face clustering pe datele din clust[0] si intoarce etichetele
# Matricea de intrare trebuie sa fie N X M, cu N esantioane si M trasaturi per esantion

# AFISAREA PUNCTELOR CU CLUSTERELE AFERENTE SI A CENTROIZILOR
plt.figure(), plt.scatter(data[:,0],data[:,1], c = labels)
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1])
plt.title('Rezultatul clustering-ului si centroizii calculati')

# AFISAREA PUNCTELOR SI CLASELOR REALE
real_labels = np.array([np.argmax(x) for x in np.transpose(clust[1])])
plt.figure(), plt.scatter(data[:,0],data[:,1], c = real_labels)
plt.title('Clusterele reale')
plt.show()


#ex 4
print("Diferenta dintre elementul de pe cea de-a doua linie si cea de-a treia coloana din m1 si elementul de pe prima linie si cea de-a doua coloana din m2.\nRezultatul este", m1[1,2]-m2[0,1]);

#ex 5

