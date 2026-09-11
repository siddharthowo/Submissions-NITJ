from itertools import zip_longest
import numpy as np


def get_dimensions(matrix):
    return [len(matrix),len(matrix[0])]


def find_determinant(matrix):
    dim = get_dimensions(matrix)
    if dim[0] == 1:
        return matrix[0][0]
    if dim == [2, 2]:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(dim[1]):
        submatrix = [
            [matrix[r][c] for c in range(dim[1]) if c != col]
            for r in range(1, dim[0])
        ]
        sign = (-1) ** col
        det += sign * matrix[0][col] * find_determinant(submatrix)
    return det


def list_multiply(list1,list2):
    #polynomial list, with indices indicating power of variable ([0]->x^0,[1]->x^1 and so on)
    res = [0 for i in range(len(list1)+len(list2)-1)]
    for idx,a in enumerate(list1):
        for jdx,b in enumerate(list2):
            res[idx+jdx] += a*b
    return res


def list_add(list1,list2,sub=1):
    #addition of polynomial lists
    return [(a or 0) + sub * (b or 0) for a,b in zip_longest(list1,list2,fillvalue=0)]


def determinant_equation(matrix):
    #return determinant equation as a list
    dim = get_dimensions(matrix)

    if dim==[1, 1]:
        return matrix[0][0]

    if dim==[2, 2]:
        ad = list_multiply(matrix[0][0], matrix[1][1])
        bc = list_multiply(matrix[0][1], matrix[1][0])
        return list_add(ad, bc, sub=-1)

    result = [0]
    for col in range(dim[1]):
        submatrix = [[matrix[r][c] for c in range(dim[1]) if c != col] for r in range(1, dim[0])]
        minor_det = determinant_equation(submatrix)
        term = list_multiply(matrix[0][col],minor_det)
        sign = (-1) ** col
        result = list_add(result,term,sub=sign)

    return result


def identity_matrix(dimensions):
    return [[1 if i == j else 0 for j in range(dimensions[1])] for i in range(dimensions[0])]


def characteristic_equation(matrix):
    dims = get_dimensions(matrix)
    I = identity_matrix(dims)
    return [[[matrix[i][j], -I[i][j]] for j in range(dims[1])] for i in range(dims[0])]

def find_cubic_roots(coeffs):
    #uses cardano's method to find roots of cubic equations
    a,b,c,d = coeffs
    if a==0:
        raise ValueError("Leading coefficient 'a' cannot be zero for a cubic.")

    B=b/a
    C=c/a
    D=d/a

    p=C-(B**2)/3
    q=(2 * (B**3))/27 - (B*C)/3 + D

    d = (q/2)**2 + (p/3)**3
    sqrt_d = d**0.5
    u = (-q/2 + sqrt_d)**(1/3)

    if abs(u)==0:
        v = (-q/2 - sqrt_d)**(1/3)
    else:
        v = -p/(3 * u)

    w1 = complex(-0.5, (3**0.5) / 2)
    w2 = complex(-0.5, -(3**0.5) / 2)

    t1 = u+v
    t2 = u*w1 + v*w2
    t3 = u*w2 + v*w1

    sft = B / 3
    roots = []
    for t in (t1, t2, t3):
        root = t - sft
        real = root.real if isinstance(root,complex) else root
        imag = root.imag if isinstance(root,complex) else 0.0

        if abs(imag) < 1e-8:
            roots.append(round(real, 8))
        else:
            roots.append(complex(round(real,8),round(imag,8)))

    return roots


def find_eigenvalues(matrix):
    dt_equation = determinant_equation(characteristic_equation(matrix))
    return find_cubic_roots(dt_equation[::-1])


if __name__ == "__main__":
    A = [[6, 1, -1],
         [0, 7,  0],
         [3, -1, 2]]

    eigenvalues = find_eigenvalues(A)
    print("Eigenvalues:", sorted(np.round(eigenvalues, 4)))
    print("np answers:", sorted(np.round(np.linalg.eigvals(A), 4)))