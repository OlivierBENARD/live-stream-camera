import numpy as np

converter = {0:' ', 17:'*', 34:'-', 51:'_', 68:'~', 85:'/', 102:'3', 119:'4', 136:'5',
            153:'6', 170:'£', 187:'&', 204:'$', 221:'B', 238:'8', 255:'@'}

def nb_colors(matrix):
    unique_values = set(value for row in matrix for value in row)
    return len(unique_values)

def invert_gray_colors(matrix):
    return 255 - matrix

def reduce_gray_scale(matrix, niveaux=256): # guaranteed to get a min new_value of 0 and a max new_value of 255
    try:
        assert(niveaux>1 and niveaux<257)
    except e as AssertionError:
        print(e)
    else:
        d = 256 / niveaux
        m = 255 / (niveaux - 1)
        converter = lambda value : (value//d)*m
        return np.array(list(map(converter, matrix)), dtype=np.uint8)

def convert_to_char(matrix):
    print('\n'.join((''.join(map(lambda item : converter[item], row[::5])) for row in matrix[::7])))
