print("N:")
N = int(input())

print("M:")
M = int(input())

count = 0
# stop at lower,so optimize loop:
if M>N:
    limit = N
else:
    limit = M

i = 2
while i<limit:
    if N % i == 0 and M  % i == 0 : 
        print(i)
        count+=1
    i+=1
        
if count==0 : 
    print("NO common dividers")


