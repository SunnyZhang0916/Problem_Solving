# https://math.stackexchange.com/questions/1010591/what-is-the-number-of-intersections-of-diagonals-in-a-convex-equilateral-polygon
# https://en.wikipedia.org/wiki/Polygon

N = int(input())

result = N * (N - 1) * (N - 2) * (N - 3) // 24

print(result)
