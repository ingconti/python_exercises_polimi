MAX_ITERATIONS = 10

i = 0
max = 0
max_fractional_part = 0.0
happenHere = 0
while i<MAX_ITERATIONS:
    n = float(raw_input())
    fractional_part = n - int(n)
    if fractional_part>max_fractional_part:
        max_fractional_part = fractional_part
        max = n
        happenHere = i
    i+=1

print("max: ", max, " at iteration: ", happenHere+1)
