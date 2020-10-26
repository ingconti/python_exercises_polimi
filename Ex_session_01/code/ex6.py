n = int(raw_input())
m = int(raw_input())

i = 2
limit = 30 * 30
while i<limit:
    if n * n + m * m == i * i:
        print(m, n, i)
    i+=1
        

