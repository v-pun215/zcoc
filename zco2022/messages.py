from collections import defaultdict

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    msgs = []
    
    #freq_col[i][j] = frequency of j in i-th column
    #val_poss[i] = possible values for i-th column
    freq_col = [defaultdict(int) for _ in range(N)]
    val_poss = [[] for _ in range(N)]
    
    for _ in range(M):
        row = list(map(int, input().split()))
        msgs.append(row)
        
        for j in range(N):
            freq_col[j][row[j]] += 1
            if freq_col[j][row[j]] == (M // 2): #M / 2 may return float
                val_poss[j].append(row[j])
    
    valid = True
    for val in val_poss:
        if not val:
            valid = False
            break
    
    if not valid:
        print(0)
        print()
        continue
    
    poss_real_msgs = []     #answer
    msgs_binary = set()
    
    for msg_idx in range(M):
        msg = msgs[msg_idx]
        
        #msg_bin -> binary fingerprint of msg, relative to assumed real msg. 1 -> matches assumed real value, 0 -> different value than assumed real value
        
        msg_bin = 0
        
        valid_msg = True
        for col in range(N):
            poss_reals_col = val_poss[col]
            assumed_real_col = poss_reals_col[0]
            
            if msg[col] == assumed_real_col:
                #col will always be 0 (not processed previously)
                # '|' -> bitwise OR operator
                # here, equivalent to '^' -> bitwise XOR operator 
                
                msg_bin |= (1 << (N - col - 1))
            
            elif len(poss_reals_col) == 1:
                valid_msg = False
        
        msgs_binary.add(msg_bin)
        
        #check for duplicates
        if len(msgs_binary) != msg_idx + 1:
            valid = False
            break
        
        if valid_msg:
            poss_real_msgs.append(msg_idx)
    
    if valid:
        print(len(poss_real_msgs))
        print(*poss_real_msgs)
    else:
        print(0)
        print()