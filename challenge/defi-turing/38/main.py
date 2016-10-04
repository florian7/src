#!/usr/bin/python3 

def T(n):

    new_n = ""
    
    i = 0
    while i < len(n):
        c = n[i]
        j = 1

        while i + j < len(n) and n[i + j] == c:
            j += 1
        
        i += j
        new_n += str(j) + c

    return new_n


t = "1"
i_max = 75
for i in range(1, i_max):
    t = T(t)


for i in range(1, 10):
    print("There are {} '{}' in T{}".format(t.count(str(i)), i, i_max))
