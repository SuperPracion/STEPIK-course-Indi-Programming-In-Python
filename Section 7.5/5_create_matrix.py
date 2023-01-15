def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list:
    filed_matrix = []

    for i in range(size):
        temp = []
        for j in range(size):
            if i < j:
                temp += [up_fill]
            elif i > j:
                temp += [down_fill]
            else:
                temp += [i + 1]
        filed_matrix.append(temp)

    return filed_matrix
