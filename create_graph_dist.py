# importing the required module
import matplotlib.pyplot as plt

def create_the_graph(distance_list):
    list_distance_no_zero = []
    # plotting the points
    indexes = []
    for i, point in enumerate(distance_list):
        list_distance_no_zero.append(point)
        indexes.append(i)

    plt.plot(indexes, list_distance_no_zero)


    # naming the x axis
    plt.xlabel('File Index')
    # naming the y axis
    plt.ylabel('Entropy Distance')

    # giving a title to my graph
    plt.title('Anomaly Detector')

    # function to show the plot
    plt.show()
