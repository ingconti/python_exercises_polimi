print("N:")
N = int(input())

print("M:")
M = int(input())

count = 0

i = 2
limit = 30 * 30
while i<limit:
    if N*N + M *M == i : 
        print(M, N , i)
    i+=1
        

