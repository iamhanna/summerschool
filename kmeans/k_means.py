import matplotlib.pyplot as plt
import numpy as np

mean_1 = (500, 2)
std_1 = 70

mean_2 = (200, 100)
std_2 = 50

mean_3 = (-100, 100)
std_3 = 100

n_cluster = 2000
# GENERATE THE DATA
data_1 = np.random.normal(loc=mean_1, scale=std_1, size=(n_cluster, 2))
data_2 = np.random.normal(loc=mean_2, scale=std_2, size=(n_cluster, 2))
data_3 = np.random.normal(loc=mean_3, scale=std_3, size=(n_cluster, 2))
data = np.concatenate((data_1, data_2))
data = np.concatenate((data, data_3))

x = data[:, 0]
y = data[:, 1]

nb_datapoints = len(x)

plt.plot(x, y, 'o')
plt.savefig('images/data.pdf')
plt.close()

# we dont initialize the centroids completely randomly
x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)
# print(x_min, x_max, y_min, y_max)

N_centroids = 3
# initialize
x_centroids = np.random.uniform(x_min, x_max, 3)
y_centroids = np.random.uniform(y_min, y_max, 3)
# print(x_centroids, y_centroids)

# randomly assign the centroids
# here just used to created a datastructure containing the assignments
centroids_assignments = np.random.randint(0, 3, nb_datapoints)

N_iterations = 20

for iteration in range(0, N_iterations):
            # VORONOI
    print("------")
    print("step: {}".format(iteration))
    for datapoint in range(nb_datapoints):
        x_point = x[datapoint]
        y_point = y[datapoint]
        distance_0 = (x_point - x_centroids[0]
                      )**2 + (y_point - y_centroids[0])**2
        distance_1 = (x_point - x_centroids[1]
                      )**2 + (y_point - y_centroids[1])**2
        distance_2 = (x_point - x_centroids[2]
                      )**2 + (y_point - y_centroids[2])**2
        distances = [distance_0, distance_1, distance_2]
        # get the index of the closest centroid
        centroid = distances.index(max(distances))
        centroids_assignments[datapoint] = centroid

    cluster_0 = np.where(centroids_assignments == 0)
    cluster_1 = np.where(centroids_assignments == 1)
    cluster_2 = np.where(centroids_assignments == 2)

    plt.plot(x[cluster_0], y[cluster_0], 'go')
    plt.plot(x[cluster_1], y[cluster_1], 'yo')
    plt.plot(x[cluster_2], y[cluster_2], 'bo')
    plt.plot(x_centroids, y_centroids, 'ro')
    title = 'voronoi : iteration  ' + str(iteration) + ' (centroids in red)'
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('images/it_' + str(iteration) + '_assign_voronoi.pdf')
    plt.close()

    # UPDATE CENTROIDS
    # EDIT HERE
    x_centroids[0] = np.sum(x[cluster_0])
    x_centroids[1] = np.sum(x[cluster_1])
    x_centroids[2] = np.sum(x[cluster_2])
    y_centroids[0] = np.sum(y[cluster_0])
    y_centroids[1] = np.sum(y[cluster_1])
    y_centroids[2] = np.sum(y[cluster_2])
    print("centroids positions")
    print("x0: {}  y0: {}".format(round(x_centroids[0], 2),
                                  round(y_centroids[0], 2)))
    print("x1: {}  y1: {}".format(round(x_centroids[1], 2),
                                  round(y_centroids[1], 2)))
    print("x2: {}  y2: {}".format(round(x_centroids[2], 2),
                                  round(y_centroids[2], 2)))
    # plot the result
    plt.plot(x[cluster_0], y[cluster_0], 'go')
    plt.plot(x[cluster_1], y[cluster_1], 'yo')
    plt.plot(x[cluster_2], y[cluster_2], 'bo')
    plt.plot(x_centroids, y_centroids, 'ro')
    title = "update centroids : iteration {} (centroids in red)".format(
        iteration)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('images/it_' + str(iteration) + '_move_centroids.pdf')
    plt.close()
