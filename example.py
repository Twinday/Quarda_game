n = 3
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = [[x[i] for x in a] for i in range(1, n)]
b = list()
for j in a:
    b.append(j[-1::-1])
print(a)
print(b)


original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = tuple(zip(*original[::-1]))
print(rotated)