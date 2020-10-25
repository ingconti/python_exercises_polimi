
iterations=3
MAX=0
happenHere = 0
while iterations>0:
    print("N: ")
    N = int(input())
    if N>MAX:
        MAX = N
        happenHere = iterations
    iterations-=1
    
    
print("max is: ", MAX, " iteration: ", happenHere)
