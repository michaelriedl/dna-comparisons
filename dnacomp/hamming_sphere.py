import itertools


def hamming_sphere(seq: str, distance: int) -> list:
    """
    Return the Hamming sphere around a sequence.

    Parameters
    ----------
    seq : str
        The sequence to create the Hamming sphere around.
    distance : int
        The Hamming distance from the sequence.

    Returns
    -------
    list
        A list of all sequences within the Hamming sphere.

    Raises
    ------
    ValueError
        If the length of the sequence is less than the distance.
    """
    # Check that the length of the string is less than the distance
    if len(seq) < distance:
        raise ValueError(
            "The length of the sequence must be greater than the distance."
        )
    # Iterate over all possible position combinations
    seq_sphere = []
    for positions in itertools.combinations(range(len(seq)), distance):
        # Iterate over all possible nucleotide combinations
        for replacements in itertools.product("ACGT", repeat=distance):
            # Create a copy of the sequence
            new_seq = list(seq)
            # Replace the nucleotides
            for position, replacement in zip(positions, replacements):
                new_seq[position] = replacement
            # Add the new sequence to the sphere
            seq_sphere.append("".join(new_seq))

    return list(set(seq_sphere))
