import numpy as np

def index_nth_largest(a: np.ndarray, n: int) -> int:
    """
    Determine the flat index of the n'th biggest element of an array.
    1 yields argmax, a.length yields argmin.
    """
    if (n <= 0):
        raise ValueError("index_nth_largest: non-positive n")

    size = np.size(a)
    if (n > size):
        raise ValueError("index_nth_largest: n out of bounds")


    return np.argpartition(a, size - n, axis=None)[size - n]
