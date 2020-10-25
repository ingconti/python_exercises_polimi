N = 3
M = 3
limit = 30
i =0

while M<limit:
    N = 3
    while N<limit:
        i = 3
        while i<limit*limit:
            if N*N + M*M == i*i and N != M: 
                print(M, N , i)
            i+=1
        N+=1
    M+=1
        

