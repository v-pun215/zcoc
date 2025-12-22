with open("word.in", "r") as inp:
    inpu = inp.read().splitlines()
nk = list(map(int, inpu[0].split()))

n = nk[0]
k = nk[-1]
words = inpu[1].split()

output = []

for i in words:
    if output==[]:
        output.append([i])
    else:
        last_entry = output[-1]
        total_len = 0
        for word in last_entry:
            total_len+=len(word)
        if total_len+len(i)<=k:
            output[-1].append(i)
        else:
            output.append([i])
with open("word.out", "w") as out:
    ooty = ""
    for i in output:
        cutty = ""
        for e in i:
            cutty+=e+" "
        ooty+=cutty.rstrip()+"\n"
    out.write(ooty.rstrip())