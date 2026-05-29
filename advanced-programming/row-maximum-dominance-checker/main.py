matrix = []

for _ in range(4):
    row = list(map(int, input().split()))
    matrix.append(row)

# check uniqueness and range
flat = [x for row in matrix for x in row]

if len(flat) != len(set(flat)) or any(x >= 100 for x in flat):
    exit()

for i in range(4):
    max_val = max(matrix[i])
    col = matrix[i].index(max_val)

    ok = True
    for j in range(4):
        if j != i and matrix[j][col] >= max_val:
            ok = False
            break

    if ok:
        print(i + 1)
        break
