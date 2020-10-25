print("N:")

# N = int(input())
N = input()

print(".....")
while N>=0:
    N-=1 # skip N itself, as per text and use it to decrement in loop, too
    remainder = N % 2
    if remainder == 0:
        print(N)
    
print("done-")
