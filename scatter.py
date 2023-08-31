import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

x = [0.4005, 0.2148, 0.3457, 0.2652, 0.0789, 0.4548]
y = [0.5306, 0.3854, 0.3156, 0.1875, 0.4139, 0.3022]

xy = [[0.4005, 0.5306], [0.2148, 0.3854], [0.3457, 0.3156], [0.2652, 0.3156], [0.2652, 0.1875], [0.0789,0.4139], [0.4548,0.3002]]

z = linkage(xy, method='single', metric='euclidean')

plt.subplot(), dendrogram(Z=z)

plt.show()