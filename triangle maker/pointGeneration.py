
from skimage import filters, morphology, color
from pixelAllocation import filterGaussian, default
import numpy as np

def edgePoint(image, varLength=200, horizPoint=None, vertPoint=None):
    
    ymax, xmax = image.shape[0:2]

    if horizPoint is None:
        horizPoint = int(xmax / varLength)

    if vertPoint is None:
        vertPoint = int(ymax / varLength)

    edgeX = xmax / horizPoint
    edgeY = ymax / vertPoint

    return np.array(
        [[0, 0], [xmax, 0], [0, ymax], [xmax, ymax]]
        + [[edgeX * i, 0] for i in range(1, horizPoint)]
        + [[edgeX * i, ymax] for i in range(1, horizPoint)]
        + [[0, edgeY * i] for i in range(1, vertPoint)]
        + [[xmax, edgeY * i] for i in range(1, vertPoint)]
    )

def genRandPoint(image, n_points=100):
    ymax, xmax = image.shape[0:2]
    points = np.random.uniform(size=(n_points, 2))
    points *= np.array([xmax, ymax])
    points = np.concatenate([points, edgePoint(image)])
    return points


def genMaxEntropyPoint(image, n_points=100, maxEntropyWidth=None, filterWidth=None, width1=None, test2=None):
    
    ymax, xmax = image.shape[0:2]
    varLength = np.sqrt(xmax*ymax / n_points)
    maxEntropyWidth = varLength * default(maxEntropyWidth, 0.2)
    filterWidth = varLength * default(filterWidth, 0.1)
    width1 = varLength * default(width1, 0.3)
    test2 = default(test2, 3)
    inputImage = color.rgb2gray(image)
    inputImage = ( 255 * filters.gaussian(inputImage, sigma=filterWidth, channel_axis=True)).astype("uint8")

    inputImage = filters.rank.entropy(inputImage, morphology.disk(maxEntropyWidth))

    points = []
    for _ in range(n_points):
        y, x = np.unravel_index(np.argmax(inputImage), inputImage.shape)
        inputImage -= filterGaussian(x, y, shape=inputImage.shape[:2], amp=test2,sigma=width1)
        points.append((x, y))

    points = np.array(points)
    return points
