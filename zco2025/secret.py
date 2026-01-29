from collections import defaultdict
import queue
first_line = list(map(int, input().split()))
N = first_line[0] # number of people in class
M = first_line[-1] # m is pairs of friends in class
days_list = list(map(int, input().split()))

friend_list = defaultdict(lambda: defaultdict(list))
all_friends = set()
for i in range(M):
    values = list(map(int, input().split()))
    for z in values:
        all_friends.add(z)
    friend_list[values[0]][1].append(values[1])
    friend_list[values[1]][1].append(values[0])
consolidated_li = defaultdict(lambda: defaultdict(list))
for key in friend_list:
    consolidated_key = defaultdict(list)

    values = friend_list[key]
    consolidated_key = values

    last_key = next(reversed(values))
    first_key = next(iter(values))

    marked = set()
    marked.add(key)
    marked.update(values[first_key])

    for i in values[first_key]:
        friends_i = friend_list[i]
        for key_i in friends_i:
            values_i = friends_i[key_i]
            for z in values_i:
                if not z in marked:
                    consolidated_key[key_i+1].append(z)
                    marked.add(z)
    print(consolidated_key)
    consolidated_li[key] = consolidated_key

print(dict(consolidated_li))
exit
'''
Eg.
N=6 M=5
10 6 4 3 -1 6
1 2
2 6
1 6
3 4
4 6

friend_list = {
    1: {1: [2, 6]},
    2: {1: [1, 6]},
    6: {1: [2, 1, 4]},
    3: {1: [4]},
    4: {1: [3, 6]}
}

updated_friend_list = {
    1: {1: [2, 6], 2: [4], 3: [3]},
    2: {1: [1, 6], 2: [4], 3: [3]},
    6: {1: [2, 1, 4], 2: [3]},
    3: {1: [4]},
    4: {1: [3, 6]}
}

We start a queue.
We start a set named marked
put first key (1) from friend_list in queue ---- queue = [1]
mark 1 ----------------------------------------- marked = [1]
level = 1
while queue is not empty:
    size = queue size
    for i in range(size):
        u = pull first in queue
        friends = get friend dict from friend_list of u
        for every key in friends:
            for every unmarked guy in key:
                queue.put(guy)
    level+=1

for ever key in friend list:
    last = last dict key in value dict
    marked = set(last_key)
    for ever i in last_value:
        marked.add(i)
        friends_i = get i friend_list
        
        for every key, value in friends_i:
            for every z in value:
                
    


'''


r'''
SOLUTION TO PROBLEMO:
1. get friends list of every guy 1 to N
2. then we iterate through every guy and check when he can first be told from second_line
3. then in the same iteration we go through all his friends checking the date they can first be told
4. we know that if we tell bro on day, say, 1, he'll tell all his broskis on day 2.
5. so using that we basically get the max time of his brojowskis, and subtract 1 from it. that will be bros earliest date we can tell that nub. if this date is somehow before we can tell him himself, then we just right the date we can tell him himself. 
NOTE: if we know we cant EVER tell chubjauski, we cant tell him ever. same with friends. if broski will eventually tell another bro that we cant tell, we cant tell bro either.


'''
friend_list = dict(friend_list)
print("days list:", days_list)
print("friends list:", friend_list)
print("all friends:", all_friends)
