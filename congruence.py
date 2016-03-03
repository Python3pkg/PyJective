import numpy as np
from transformation import *


def areCongruent(f1, f2, eps=0.001):
    """Return True if given figures are congruent, otherwise False.
    
    
    Keyword arguments:
    f1 -- the first figure
    f2 -- the second figure
    eps -- epsilon value for floating-point math (default 0.001)
    """
    allAreTransformations = isTransformation(f1) and isTransformation(f2)
    noneAreTransformations = not isTransformation(f1) or isTransformation(f2)
    
    if allAreTransformations:
        return all(areCongruent(e1, e2, eps) for e1, e2 in zip(f1, f2))
    elif noneAreTransformations:
        ratios = []
        for e1, e2 in zip(f1, f2):
            if e1 and e2:
                ratios.append(e1 / e2)
            elif e1 or e2:
                return False
        return all(abs(ratio - ratios[0]) < eps for ratio in ratios)
    else:
        return False


# Goal: make this work in n dimensions.
def areIncident(c1, c2, c3):
    """Return True if given points/lines are incident, otherwise False.
    
    Keyword arguments:
    c1 -- the first point/line
    c2 -- the second point/line
    c3 -- the third point/line
    """
    return np.linalg.det(coords) == 0


def containingLine(c1, c2):
    """Return the line that contains the provided points.
    
    Keyword arguments:
    c1 -- the first point
    c2 -- the second point
    """
    return np.cross(c1, c2)


def pointOfIntersection(c1, c2):
    """Return the point where the provided lines intersect.
    
    Keyword arguments:
    c1 -- the first line
    c2 -- the second line
    """
    return np.cross(c1, c2)
