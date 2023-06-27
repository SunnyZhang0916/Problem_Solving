# if the longest stick is smaller than the sum of the other two sticks 
n = int(input())
sticks = list(map(int, input().split()))
sticks.sort()

possible = False

# only compare the nearby
for i in range(n - 2):
    if sticks[i] + sticks[i + 1] > sticks[i + 2]:
        possible = True
        break

if possible:
    print("possible")
else:
    print("impossible")

