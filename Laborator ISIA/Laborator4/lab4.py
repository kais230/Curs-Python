import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets, tree

# Incarcarea datelor
circles = datasets.make_circles(n_samples=150)
date = circles[0]
etichete = circles[1]


# Crearea clasificatorului
clf = tree.DecisionTreeClassifier()

# Antrenarea clasificatorului
clf.fit(date,etichete)

# Prezicere din datele setului de antrenare
# (Etichetele originale folosite la antrenare
# sunt in variabila etichete)
preds = clf.predict(date)


# Colorarea spatiului pentru vizualizarea impartirii facute de arbore
x_min, x_max = date[:, 0].min() - 1, date[:, 0].max() + 1
y_min, y_max = date[:, 1].min() - 1, date[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))


Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)


# Vizualizarea datelor de antrenare in graficul colorat
plt.scatter(date[:,0],date[:,1],c=preds)

# Instructiunea care deseneaza figurile
plt.show()