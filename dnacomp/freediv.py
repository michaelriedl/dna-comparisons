import numpy as np


def _free_divergence_matrix(s1: str, s2: str) -> np.ndarray:
    assert len(s1) == len(s2), "Free divergence requires strings of equal length."
    n = len(s1) + 1
    M = np.zeros((n, n), dtype=np.uint8)

    # First row and column
    M[0, :] = np.arange(n)
    M[:, 0] = np.arange(n)

    # Inner square
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if s1[i - 1] == s2[j - 1]:
                diag_penalty = M[i - 1, j - 1]
            else:
                diag_penalty = M[i - 1, j - 1] + 1
            M[i, j] = min(diag_penalty, M[i - 1, j] + 1, M[i, j - 1] + 1)

    # Last row
    for i in range(1, n - 1):
        if s1[n - 2] == s2[i - 1]:
            diag_penalty = M[n - 2, i - 1]
        else:
            diag_penalty = M[n - 2, i - 1] + 1
        M[n - 1, i] = min(
            diag_penalty, M[n - 2, i] + 1, M[n - 1, i - 1]
        )  # No penalty along last row

    # Last column
    for i in range(1, n - 1):
        if s1[i - 1] == s2[n - 2]:
            diag_penalty = M[i - 1, n - 2]
        else:
            diag_penalty = M[i - 1, n - 2] + 1
        M[i, n - 1] = min(
            diag_penalty, M[i - 1, n - 1], M[i, n - 2] + 1  # No penalty along last col
        )

    # Last elt
    if s1[n - 2] == s2[n - 2]:
        diag_penalty = M[n - 2, n - 2]
    else:
        diag_penalty = M[n - 2, n - 2] + 1
    M[n - 1, n - 1] = min(
        diag_penalty, M[n - 2, n - 1], M[n - 1, n - 2]  # No penalty along last col
    )  # No penalty along last row

    return M


def free_divergence(s1: str, s2: str) -> float:
    """Calculate the free divergence between two sequences. The sequences must be
    of the same length.

    Parameters
    ----------
    s1 : str
        The first sequence.
    s2 : str
        The second sequence.

    Returns
    -------
    int
        The free divergence between the two sequences.
    """
    M = _free_divergence_matrix(s1, s2)
    return float(M[-1, -1])


def free_divergence_parallel(tuple_seqs: tuple[str, str]) -> tuple[str, str, float]:
    """Calculate the free divergence between two sequences. This function is
    designed to be used in parallel.

    Parameters
    ----------
    tuple_seqs : tuple[str, str]
        A tuple of two sequences.

    Returns
    -------
    tuple[str, str, float]
        A tuple of the sequences in the input tuple and the free divergence
        between the two input sequences. The sequences must be of the same length.
    """
    seq1, seq2 = tuple_seqs
    return seq1, seq2, free_divergence(seq1, seq2)
