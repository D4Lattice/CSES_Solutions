try:
    given_num = int(input())
except:
    print("ERROR:: Please input a positive integer.")
else:
    seq = []
    while given_num != 1:
        if given_num % 2 == 0:
            given_num = given_num//2
            seq.append(given_num)
        else:
            given_num = (3 * given_num) + 1
            seq.append(given_num)
            
    print(*seq)
        
