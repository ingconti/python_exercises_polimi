JUDGES = 5
max = 0
min = 10
sum = 0
i = 0

while i<JUDGES:
    vote = float(raw_input())
    sum+=vote
    if vote > max:
        max = vote
    if vote<min:
        min = vote
    i+=1

tot = (sum - max - min) * 2
print(tot)




