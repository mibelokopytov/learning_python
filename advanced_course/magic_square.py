n = int(input())

matrix = [[int(i) for i in input().split()] for i in range(n)]
sample = sum(matrix[0])
sample2 = matrix[0][0]

def sumrow(matrix, sample):
    temp = []
    for row in matrix:
        temp.append(row)
    for i in range(n):

        if sum(temp[i]) == sample:
            continue

        else:
            return False
            break
    return True


def sumcols(matrix, sample):
    temp = []
    for r in range(n):
        for c in range(n):
            temp.append(matrix[c][r])
    while len(temp) >= 3:
        if sum(temp[:n]) == sample:
            del temp[:n]

        else:
            return False
            break
        return True


def sumdiag(matrix, sample):
    total1 = 0
    total2 = 0

    for i in range(n):
        total1 += matrix[i][i]
        total2 += matrix[i][n - i - 1]

    if total1 == sample and total2 == sample:
        return True
    else:
        return False

def same(matrix, sample2):
    for r in range(n):
        for c in range(1, n):
            if matrix[r][c] != sample2 and matrix[r][c] != 0:
                continue
            else:
                return False
    return True

if sumdiag(matrix, sample) and sumrow(matrix, sample) and sumcols(matrix, sample) and same(matrix, sample2):
    print('YES')
else:
    print('NO')