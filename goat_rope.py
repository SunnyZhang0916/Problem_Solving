import math

def calculate_distance(x, y, x1, y1, x2, y2):
    # x on the left side
    if x < x1:
        # outside of line
        if y < y1:
            return math.sqrt((x1 - x)**2 + (y1 - y)**2)
        elif y > y2:
            return math.sqrt((x1 - x)**2 + (y2 - y)**2)
        else:
            return x1 - x
    
    # x on the right side
    elif x > x2:
        #outside of line
        if y > y2:
            return math.sqrt((x - x2)**2 + (y - y2)**2)
        elif y < y1:
            return math.sqrt((x - x2)**2 + (y - y1)**2)
        else:
            return x - x2
    
    else:
        if y < y1:
            return y1 - y
        elif y > y2:
            return y - y2
        else:
            return 0

x, y, x1, y1, x2, y2 = map(int, input().split())

min_distance = calculate_distance(x, y, x1, y1, x2, y2)

print(f"{min_distance:.3f}")