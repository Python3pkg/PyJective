import numpy as np
import np_helpers
import transformation


def fromFivePoints(p1, p2, p3, p4, p5):
    """Return the projective conic defined by the given points.
    
    Keyword arguments:
    p1 -- the first point
    p2 -- the second point
    p3 -- the third point
    p4 -- the fourth point
    p5 -- the fifth point
    """
    A = []
    for p in (p1, p2, p3, p4, p5):
        A += [[p[0]**2, p[0]*p[1], p[0]*p[2], p[1]**2, p[1]*p[2], p[2]**2]]
    return np_helpers.nullspace(A)

def mapToStandard(e, p, q, r):
    """Return a projective transformation that maps three points on a conic to
the conic xy + xz + yz = 0.
    
    Keyword arguments:
    e -- a projective conic
    p -- the first point on e
    q -- the second point on e
    r -- the third point on e
    """
    A = np.matrix([p, q, r])
    
    p = np.matrix(p)
    q = np.matrix(q)
    r = np.matrix(r)
    
    xxp = e[0] * np.dot(p.T, p)
    xyp = e[1] * np.dot(p.T, q)
    xzp = e[2] * np.dot(p.T, r)
    yyp = e[3] * np.dot(q.T, q)
    yzp = e[4] * np.dot(q.T, r)
    zzp = e[5] * np.dot(r.T, r)
    
    M = xxp + xyp + xzp + yyp + yzp + zzp
    
    b = M.item(0, 1) + M.item(1, 0)
    f = M.item(0, 2) + M.item(2, 0)
    g = M.item(2, 1) + M.item(1, 2)
    
    B = np.matrix([[1/g, 0  , 0  ],
                   [0  , 1/f, 0  ],
                   [0  , 0  , 1/b]])
    
    return np.dot(B, np.linalg.inv(A))

def mapThreePoints(e1, p1, q1, r1, e2, p2, q2, r2):
    """Return a projective transformation that maps three points on a conic to
three points on another conic.
    
    Keyword arguments:
    e1 -- a projective conic
    p1 -- the first point on e1
    q1 -- the second point on e1
    r1 -- the third point on e1
    e2 -- a projective conic
    p2 -- the first point on e2
    q2 -- the second point on e2
    r2 -- the third point on e2
    """
    t1 = mapToStandard(e1, p1, q1, r1)
    t2 = mapToStandard(e2, p2, q2, r2)
    return compose(np.linalg.inv(t2), t1)
