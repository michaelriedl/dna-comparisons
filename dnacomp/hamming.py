from scipy.spatial.distance import hamming


def hamming_distance(seq1: str, seq2: str) -> float:
    """Calculate the hamming distance between two sequences. The sequences must be
    of the same length.

    Parameters
    ----------
    seq1 : str
        The first sequence.
    seq2 : str
        The second sequence.

    Returns
    -------
    float
        The hamming distance between the two sequences.
    """
    assert len(seq1) == len(seq2), "Sequences must be of the same length."
    return hamming(list(seq1), list(seq2)) * len(seq1)


def hamming_distance_parallel(tuple_seqs: tuple[str, str]) -> tuple[str, str, float]:
    """Calculate the hamming distance between two sequences. This function is
    designed to be used in parallel.

    Parameters
    ----------
    tuple_seqs : tuple[str, str]
        A tuple of two sequences.

    Returns
    -------
    tuple[str, str, float]
        A tuple of the sequences in the input tuple and the hamming distance
        between the two input sequences. The sequences must be of the same length.
    """
    seq1, seq2 = tuple_seqs
    assert len(seq1) == len(seq2), "Sequences must be of the same length."
    return seq1, seq2, hamming_distance(seq1, seq2)
