print("n:")
n = int(raw_input())

print("m:")
m = int(raw_input())

count = 0
# stop at lower, so optimize loop:
if m>n:
    limit = n
else:
    limit = m

i = 2
while i<limit:
    if n % i == 0 and n  % i == 0 :
        print(i)
        count+=1
    i+=1
        
if count==0 : 
    print("No common dividers")


