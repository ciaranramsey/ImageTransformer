import pandas as pd
import numpy as np


def triangleColour(triangles, image, agg_func=np.median):
    
    ymax, xmax = image.shape[:2]
    xx, yy = np.meshgrid(np.arange(xmax), np.arange(ymax))
    
    
    pixel = np.c_[xx.ravel(), yy.ravel()]
    pixleTriangle = triangles.find_simplex(pixel)
    
    df = pd.DataFrame({ "triangle": pixleTriangle, "r": image.reshape(-1, 3)[:, 0], "g": image.reshape(-1, 3)[:, 1], "b": image.reshape(-1, 3)[:, 2] })
    triangleCount = triangles.vertices.shape[0]

    rGB = (df.groupby("triangle") [["r", "g", "b"]].aggregate(agg_func).reindex(range(triangleCount), fill_value=0) )   
    return rGB.values / 256

def filterGaussian(x, y, shape, amp=1, sigma=15):
    xv, yv = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
    g = amp * np.exp(-((xv - x) ** 2 + (yv - y) ** 2) / (2 * sigma ** 2))
    return g

def default(value, default_value): 
    if value is None:
        return default_value
    return value
