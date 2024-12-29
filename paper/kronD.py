def kron_delta(j, k):
    """
    Kronecker Delta Function
    
    Purpose:
    This function calculates the Kronecker delta from two given subscripts, j and k.
    If j == k, it returns 1. If j != k, it returns 0.
    
    Inputs:
    - j: The first subscript
    - k: The second subscript
    
    Outputs:
    - d: The Kronecker delta, 1 if j == k, 0 otherwise
    """
    if j is None or k is None:
        raise ValueError("Too few inputs. Both 'j' and 'k' must be provided.")
    
    return int(j == k)
