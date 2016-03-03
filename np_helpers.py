import numpy as np


# Figure out the name for what this actually does.
def coeffs(*args):
    """Returns the coefficients that solve the equation a0*x0 + ... + an-1*xn-1
 = xn.
    
    Keyword arguments:
    *args -- vectors to be used in the equation.
    """
    A = np.matrix(args[:-1], dtype=float).T
    b = np.matrix(args[-1], dtype=float).T
    return np.linalg.lstsq(A, b)[0]


def isArrayLike(x):
    """Return True if x has length and is not a string.
    
    Keyword arguments:
    x -- anything
    """
    return hasattr(x, '__len__') and not isinstance(x, str)


# Need to either write own function or credit SciPy Cookbook.
def nullspace(A, atol=1e-13, rtol=0):
    """Compute an approximate basis for the nullspace of A.

    The algorithm used by this function is based on the singular value
    decomposition of `A`.

    Parameters
    ----------
    A : ndarray
        A should be at most 2-D.  A 1-D array with length k will be treated
        as a 2-D with shape (1, k)
    atol : float
        The absolute tolerance for a zero singular value.  Singular values
        smaller than `atol` are considered to be zero.
    rtol : float
        The relative tolerance.  Singular values less than rtol*smax are
        considered to be zero, where smax is the largest singular value.

    If both `atol` and `rtol` are positive, the combined tolerance is the
    maximum of the two; that is::
        tol = max(atol, rtol * smax)
    Singular values smaller than `tol` are considered to be zero.

    Return value
    ------------
    ns : ndarray
        If `A` is an array with shape (m, k), then `ns` will be an array
        with shape (k, n), where n is the estimated dimension of the
        nullspace of `A`.  The columns of `ns` are a basis for the
        nullspace; each element in numpy.dot(A, ns) will be approximately
        zero.
    """

    A = np.atleast_2d(A)
    u, s, vh = np.linalg.svd(A)
    tol = max(atol, rtol * s[0])
    nnz = (s >= tol).sum()
    ns = vh[nnz:].conj().T
    return ns
