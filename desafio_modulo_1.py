# -*- coding: utf-8 -*-
"""Desafio Modulo 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kpIQRLVRMHjA5pOYbvf1bd8qyJk_awmR

*IMPORTANDO AS BIBLIOTECAS NECESSÁRIAS*
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotly as py
import plotly.graph_objs as go
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

"""*FAÇA O UPLOAD DO DATASET Consumo.csv PARA O GOOGLE COLAB*

"""

df = pd.read_csv('Consumo.csv', sep=',', encoding='1252')
df.head()

"""**PLOTANDO O GRÁFICO DE RENDA X PONTUAÇÃO**"""

plt.style.use('fivethirtyeight')
plt.figure(1, figsize=[15,6])
plt.scatter(x = 'Salario Anual (milhares)', y = 'Score Gastos (0-100)', data = df, s=200, alpha=0.5)
plt.title('Renda Anual x Pontuação de Gastos')
plt.xlabel('Salario Anual (milhares)')
plt.ylabel('Score Gastos (0-100)')
plt.show()

"""**EXECUÇÃO DO KMEANS COM 2 CLUSTERS**"""

X2 = df[['Salario Anual (milhares)', 'Score Gastos (0-100)']].iloc[:,:].values
kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init=10)
pred_y = kmeans.fit_predict(X2)

plt.style.use('fivethirtyeight')
plt.figure(1, figsize=[15,6])
plt.scatter(X2[:,0], X2[:,1], c=pred_y, s=200, alpha=0.5)
plt.grid()

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=200, c='red')

plt.title('Renda Anual x Pontuação de Gastos')
plt.xlabel('Salario Anual (milhares)')
plt.ylabel('Score Gastos (0-100)')
plt.show()

"""**EXECUÇÃO DO KMEANS COM 6 CLUSTERS**"""

X6 = df[['Salario Anual (milhares)', 'Score Gastos (0-100)']].iloc[:,:].values
kmeans = KMeans(n_clusters=6, init='k-means++', max_iter=300, n_init=10)
pred_y = kmeans.fit_predict(X6)

plt.style.use('fivethirtyeight')
plt.figure(1, figsize=[15,6])
plt.scatter(X6[:,0], X6[:,1], c=pred_y, s=200, alpha=0.5)
plt.grid()

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=200, c='red')

plt.title('Renda Anual x Pontuação de Gastos')
plt.xlabel('Salario Anual (milhares)')
plt.ylabel('Score Gastos (0-100)')
plt.show()

"""*EXIBIÇÃO DA CURVA DO COTOVELO, MOSTRANDO AS ITERAÇÕES E O NÚMERO IDEAL DE CLUSTERS*"""

wcss = []
for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10)
    kmeans.fit(X6)
    wcss.append(kmeans.inertia_)

plt.style.use('fivethirtyeight')
plt.figure(1, figsize=[15,6])
plt.plot(range(1, 20), wcss)
plt.plot([1,19],[wcss[0], wcss[len(wcss)-1]])
plt.title('Curva do cotovelo')
plt.xlabel('Número de clusters')
plt.ylabel('WCSS')
plt.show()

"""**EXECUÇÃO DO KMEANS COM O NÚMERO IDEAL DE CLUSTERS**

*Número ideal de clusters basiado no gráfico Curva do Cotovelo é 5*
"""

kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10)
pred_y = kmeans.fit_predict(X2)

print('Coordenadas Cluster Centers')
print(kmeans.cluster_centers_)
print('')
print('Valor Inertia')
print(kmeans.inertia_)

plt.style.use('fivethirtyeight')
plt.figure(1, figsize=[15,6])
plt.scatter(X2[:,0], X2[:,1], c=pred_y, s=200, alpha=0.5)
plt.grid()

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=200, c='red')

plt.title('Renda Anual x Pontuação de Gastos')
plt.xlabel('Salario Anual (milhares)')
plt.ylabel('Score Gastos (0-100)')
plt.show()
