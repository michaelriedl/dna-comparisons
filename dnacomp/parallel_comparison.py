import itertools
import multiprocessing
from collections.abc import Callable


def parallel_comparison(
    seq_list_1: list,
    seq_list_2: list,
    comparison_function: Callable[[str, str], list],
    MAX_PROCESSES: int = 8,
    CHUNK_SIZE: int = 1000,
) -> dict:
    """A comparison function that uses multiprocessing to compare two lists of sequences.

    Parameters
    ----------
    seq_list_1 : list
        A list of sequences to compare to seq_list_2.
    seq_list_2 : list
        A list of sequences to compare to seq_list_1.
    comparison_function : Callable[[str, str], list]
        The function to use to compare the sequences in seq_list_1
        and seq_list_2. Must take two strings as arguments and return a list.
    MAX_PROCESSES : int, optional
        The maximum number of processes to run in parallel, by default 8.
    CHUNK_SIZE : int, optional
        The chunk size to use in the multiprocessing, by default 1000.

    Returns
    -------
    dict
        A dictionary of the results of the comparison function. The keys are the
        sequences in seq_list_1 and the values are dictionaries with keys "sequence"
        and "measure". The "sequence" key contains the sequences in seq_list_2 and
        the "measure" key contains the results of the comparison function.
    """
    comparison_dict = {}
    with multiprocessing.Pool(processes=MAX_PROCESSES) as pool:
        iterator = pool.imap(
            comparison_function,
            itertools.product(seq_list_1, seq_list_2),
            chunksize=CHUNK_SIZE,
        )
        for x in iterator:
            if x[0] not in comparison_dict.keys():
                comparison_dict[x[0]] = {}
                comparison_dict[x[0]]["sequence"] = []
                comparison_dict[x[0]]["measure"] = []
            comparison_dict[x[0]]["sequence"].append(x[1])
            comparison_dict[x[0]]["measure"].append(x[2])

    return comparison_dict
