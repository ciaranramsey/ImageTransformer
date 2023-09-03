
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import argparse
from triangleDraw import drawImage, drawTriangle, drawPoint, \
    axis
from pixelAllocation import triangleColour, filterGaussian
from pointGeneration import edgePoint, \
    genRandPoint, genMaxEntropyPoint


def process(imageLocation, outputLocation, n_points):
    size1 = os.path.getsize(imageLocation)
    image = plt.imread(imageLocation)
    points = genMaxEntropyPoint(image, n_points=n_points)
    points = np.concatenate([points, edgePoint(image)])

    tri = Delaunay(points)

    f, ax = plt.subplots()
    ax.invert_yaxis()
    colours = triangleColour(tri, image)
    drawTriangle(ax, tri.points, tri.vertices, colours)

    ax.axis("tight")
    ax.set_axis_off()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ratio = image.shape[0] / image.shape[1]
    f.set_size_inches(5, 5*ratio)

    f.savefig(outputLocation, bbox_inches='tight', pad_inches=0)
    size2 = os.path.getsize(outputLocation)
    size1 = size1/1000
    size2 = size2/1000
    print("INFORMATION CONTENT OF IMAGES AS FOLLOWS")
    print("Size of input image is "+str(size1)+"kb")
    print("Size of output image is "+str(size2)+"kb")

# run by open file location type cmd into top and then run line python triangleMethod.py IMAGE.jpg IMAGE1.jpg -n2000
# -n___ after typing -n you type in the amount of points you wish to use in the point generation the default = 100
# using a large -n value can result in long loading times anything above 3000 will take a long time so if you wish to use high number of points just wait a few minutes :)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Triangle filter")
    parser.add_argument("image1")
    parser.add_argument("image2")
    parser.add_argument("-n", "--n_points", nargs='?', help="number of points to use", default=100)

    ns = parser.parse_args()

    image1 = ns.image1
    image2 = ns.image2
    n_points = int(ns.n_points)

    process(imageLocation=image1, outputLocation=image2, n_points=n_points)



