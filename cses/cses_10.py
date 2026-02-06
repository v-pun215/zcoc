import math

n = int(input())
s = 0
result = None
impl = 1
while result != 0:
    result = math.floor(n//5**impl)
    impl+=1
    s+=result

print(s)