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

for i in range(2, limit):
    if n % i == 0 and n  % i == 0 :
        print(i)
        count+=1
        
if count==0 : 
    print("No common dividers")


