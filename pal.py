def palind(r):
    e = len(r)-1
    s = 0
    while (s<e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r = (14,537,52,764,746,72,75873,93,727,2,7,5,776)

if(palind(r)):
    print("the tuple is flip flop")
else:
    print("the tuple is not flip flop")