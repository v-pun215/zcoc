'''
bronze = list(map(int, input().split()))
silver = list(map(int, input().split()))
gold = list(map(int, input().split()))
platinum = list(map(int, input().split()))'''
with open("promote.in", "r") as inp:
    file_inp = inp.read().splitlines()


bronze = list(map(int, file_inp[0].split()))
silver = list(map(int, file_inp[1].split()))
gold = list(map(int, file_inp[2].split()))
platinum = list(map(int, file_inp[3].split()))




scores = [bronze, silver, gold, platinum]


new= []
for sc_index, score in enumerate(scores):
    new.append(score[1]-score[0])


br2si = 0
si2go = 0
go2pla = 0

for index, i in enumerate(new):
    if index> 0:
        br2si+=i
    if index> 1:
        si2go+=i
    if index> 2:
        go2pla+=i

print(str(br2si) +"\n"+ str(si2go) +"\n"+ str(go2pla))

with open("promote.out", "w") as out:
    out.write(str(br2si) +"\n"+ str(si2go) +"\n"+ str(go2pla))