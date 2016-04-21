from conic import *


# E is a projective conic described in Ch4Ex2.
e = [[ 2.0,  1.0, -2.5],
     [ 1.0, -1.0,  0.5],
     [-2.5,  0.5,  1.0]]

# p, q, & r are 3 points on E.
p, q, r = [1, 1, 1], [1, 2, 2], [1, 2, 1]

# From Ch4Ex2, the projective transformation that takes E to the standard conic
# is:
# [[2, -1,  0],
#  [1,  0, -1],
#  [0,  1, -1]]
# (or any multiple of this)
print(threePointsToStandard(e, p, q, r))


# Print the projective transformation that takes E to the conic x^2 + y^2 = z^2:
print(mapToStandard(e))
