cimport cython


cdef fish(n: cython.int):
    i: cython.int
    f: cython.int[9]

    f = [0, 83, 51, 56, 60, 50, 0, 0, 0]

    for i in range(n):
        f[(i+7) % 9] += f[i%9]
    return sum(f)

print(fish(256))