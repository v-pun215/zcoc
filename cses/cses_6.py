def calculate(x,y):
    z = max(x,y) # z = layer
    if z%2==0: # z is even
        if y < x:
            value = ((z-1)**2) + y
        elif y >= x:
            value = (z**2) - x +1
    else:
        if x < y:
            value = ((z-1)**2) + x
        elif x>= y:
            value = (z**2) - y + 1

    return value 


T = int(input())
answers = []
for _ in range(T):
    y, x = map(int, input().split())
    answers.append(calculate(x, y))
for _ in answers:
    print(_)