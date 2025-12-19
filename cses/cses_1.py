#Weird Algorithm
n =int(input())
n_list = [n]

while n>1:
    if n%2==0:
        n=n//2
        n_list.append(n)
    elif n%2!=0:
        n = (3*n) + 1
        n_list.append(n)
print(" ".join(str(e) for e in n_list))