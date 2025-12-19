inp = input()

previous = inp[0]
count = 1
repeated = []

for digit in inp[1:]:
    if digit == previous:
        count += 1
    else:
        repeated.append([previous, count])
        previous = digit
        count = 1

# append the last run
repeated.append([previous, count])


# find max repetition
maxe = repeated[0]
for element in repeated:
    if element[1] > maxe[1]:
        maxe = element

print(maxe[1])
