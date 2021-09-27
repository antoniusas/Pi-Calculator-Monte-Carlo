import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import random


def generate_rnd_points(n_samples=10, quad_length_box=2, circle_radius=1):
    return np.random.uniform(low=0.0, high=quad_length_box, size=(n_samples,2))

def visualize(quad_length_box=2, circle_radius=1, left_coord_box=(0,0), rnd_points=None):
    figure = plt.figure()
    currentAxis = plt.gca(); plt.grid(True)
    currentAxis.add_patch(Rectangle(left_coord_box, quad_length_box, quad_length_box, fill=None, color='r', linewidth=5.5))
    currentAxis.add_patch(Circle((1,1), circle_radius, color='b', linewidth=5.5, fill=None))
    number_circle, number_box, limit = 0, 0, 10000
    for coordinate in rnd_points:
        coord_x, coord_y = coordinate[0], coordinate[1]
        if np.sqrt((coord_x-1)**2+(coord_y-1)**2) <= 1:
            if number_circle <= limit:
                inside_circle = plt.Circle((coord_x, coord_y),0.01, color='b')
                currentAxis.add_patch(inside_circle)
            number_circle += 1
        else:
            if number_circle <= limit:
                outside_circle = plt.Circle((coord_x, coord_y),0.01, color='r')
                currentAxis.add_patch(outside_circle)
        number_box += 1
    pi = (4*number_circle/number_box)
    print("\nPoints in Circle: ", number_circle, "\n--------------------------","\nPoints in Boxes:  ", number_box)
    print("Estimated Pi-value: ~", pi, "~")
    plt.show()
    return

def main(*args):
    print("Estimating the PI-value using Monte-Carlo")
    if bool(args[0][1]):
        test_points = generate_rnd_points(n_samples=int(args[0][2]))
        visualize(rnd_points=test_points)
    else:
        test_points = generate_rnd_points(n_samples=1000)
        visualize(rnd_points=test_points)
    return

if __name__ == '__main__':
    main(sys.argv) # List of keywordsarguments
