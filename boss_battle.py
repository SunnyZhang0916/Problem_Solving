# Just throw bomb i to pillar i + 2 mod n.
# Each bomb gives a new position where the boss cannot be.
# When only 3 pillars remain, a single bomb will defeat the boss
# Total is thus n − 3 + 1 = n − 2.

n = int(input())

if n <= 3:
    print(1)
else:
    print(n-2)
