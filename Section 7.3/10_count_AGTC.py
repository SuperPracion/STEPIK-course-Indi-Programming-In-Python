def count_AGTC(dna):
    res = {'A': 0, 'G': 0, 'T': 0, 'C': 0}

    for element in dna:
        res[element] += 1

    return tuple(res.values())
