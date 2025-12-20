import sys
inp = sys.stdin.read().splitlines()
n = inp[0]
opinion = []
for i in inp[1:]:
    opinion.append(list(map(int, i.split())))
attempted = 0

for i in opinion:
    c = 0
    for z in i:
        if z==1:
            c+=1
    if c>=2:
        attempted+=1

print(attempted)