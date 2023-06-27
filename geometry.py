import math

# The function dot() calculates the dot product of two vectors v1 and v2. 
# The dot product is a vector operation that returns the scalar product of two vectors.
# It can be used to compute angles between vectors, determine orthogonality of vectors, calculate projections, and more.
def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def len_v(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2)

def direction_v(l):
    return (l[1][0] - l[0][0], l[1][1] - l[0][1])

# 计算这两个点之间的距离
def point_distance(p1, p2):
    return len_v(direction_v((p1, p2)))


point1 = (1, 1)
point2 = (3, 4)
distance = point_distance(point1, point2)
print(distance)  # 输出: 5.0 这是因为这两个点形成的线段是一个直角三角形，
                 # 两点之间的距离就是直角边的长度，即斜边长为5.0。

test = dot(point1, point2)
print(test)


