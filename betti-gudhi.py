import numpy as np
import pickle as pickle
import gudhi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open ('pointCloud', 'rb') as fp:
    pointCloud = pickle.load(fp)

fig = plt.figure()
plt.rcParams['figure.figsize'] = [12, 12]
ax = fig.add_subplot(111, projection = '3d')
ax.scatter([i[0] for i in pointCloud], [i[1] for i in pointCloud], [i[2] for i in pointCloud]);
plt.show()

skeleton = gudhi.RipsComplex(points = pointCloud, max_edge_length = 0.03)
Rips_simplex_tree_sample = skeleton.create_simplex_tree(max_dimension = 3)
print(Rips_simplex_tree_sample.dimension(),
        Rips_simplex_tree_sample.num_vertices(),
        Rips_simplex_tree_sample.num_simplices())
Rips_simplex_tree_sample.compute_persistence()
print("Betti Numbers - ", Rips_simplex_tree_sample.betti_numbers())
