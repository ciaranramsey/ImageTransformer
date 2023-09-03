import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def axis(ax):
    
    ax.axis("off")
    ax.axis("tight")
    ax.set_aspect("equal")
    ax.autoscale(False)


def drawImage(ax, image):
    ax.imshow(image)


def drawPoint(ax, points):
    ax.scatter(x=points[:, 0], y=points[:, 1], color="k")


def drawTriangle(ax, points, vertices, colours=None, **kwargs):

    if colours is None:
        triangleColour = len(vertices) * ["none"]
        lineColours = len(vertices) * ["black"]
    else:
        triangleColour = colours
        lineColours = colours

    for triangle, fc, ec in zip(vertices, triangleColour, lineColours):
        p = Polygon([points[i] for i in triangle], closed=True, facecolor=fc, edgecolor=ec, **kwargs)
        ax.add_patch(p)
