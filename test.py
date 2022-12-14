import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten
import matplotlib.pyplot as plt

list1 = [88.0, 74.0, 96.0, 85.0]
list2 = [92.0, 99.0, 95.0, 94.0]
list3 = [91.0, 87.0, 99.0, 95.0]
list4 = [78.0, 99.0, 97.0, 81.0]
list5 = [88.0, 78.0, 98.0, 84.0]
list6 = [100.0, 95.0, 100.0, 92.0]

data = np.array([list1,list2, list3, list4, list5, list6])
print(f'data is:\n{data}')

whiten = whiten(data)                #
print(f'whiten is :\n{whiten}')
centroids, _ = kmeans(whiten, 2)     # 中心聚类，num of clusters：2
print(f'centroids is :\n {centroids}')
result, _ = vq(whiten, centroids)
print(result)

t = np.arange(0, 4, 0.1)
print(t)
plt.plot(t, t, t, t+2, t**2, t**3)
plt.show()

