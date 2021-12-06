import numpy as np
with open('day6_input.txt') as f:
    day6_input, *_ = f.read().splitlines()
day6_input = [int(num) for num in day6_input.split(',')]


mat = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int64)

part1 = np.linalg.matrix_power(mat, 80).sum(axis=0)
part2 = np.linalg.matrix_power(mat, 256).sum(axis=0)

print(sum(part1[i] + part2[i] * 1j for i in day6_input))
