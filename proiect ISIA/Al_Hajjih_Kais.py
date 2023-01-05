from sklearn import neural_network
import pandas as pd
import numpy as np

# INCARCARE DATE
data = pd.read_csv('soybean-large.data')
data_t = pd.read_csv('soybean-large.test')
data['clase'] = data['clase'].astype('category')
data_t['clase'] = data_t['clase'].astype('category')

# IMPARTIRE IN TRAIN SI TEST
categ = np.array(data['clase'].cat.codes.values).reshape(-1, 1)
categ_t = np.array(data_t['clase'].cat.codes.values).reshape(-1, 1)

date_train = np.array(data.drop(['clase'], axis=1))
date_test = np.array(data_t.drop(['clase'], axis=1))

etichete_train = np.array(data['clase'].values)
etichete_test = np.array(data_t['clase'].values)

# print('Date de antrenare:\n', date_train)
# print('Etichete de antrenare:\n', etichete_train)
# print('\nDate de testare:\n', date_test)
# print('Etichete de testare:\n', etichete_test)


# CREARE SI ANTRENARE MLP
clf = neural_network.MLPClassifier(hidden_layer_sizes=(35,), learning_rate_init=0.01)
clf.fit(date_train, etichete_train)

# TESTARE MLP
predictii = clf.predict(date_test)

acc = 0
# ACURATETE
for i in range(len(etichete_test)):
    if etichete_test[i] == predictii[i]:
        acc = acc + 1
print('Acuratetea=' + str((acc / len(etichete_test)) * 100) + '%')