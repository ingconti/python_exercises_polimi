#ex 1
print("insert n:")
n = int(raw_input())
initial_n = n # save to exclude printing the same number we wrote in input

#skip first if not even: (we will decrement by 2)
remainder = n % 2
if remainder != 0:
    n-=1

while n>=0:
    remainder = n % 2
    if remainder == 0:
        if n != initial_n:
            print(n)
        n-=2
    else:
        n=-1


