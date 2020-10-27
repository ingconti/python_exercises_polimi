JUDGES = 5

vote = float(raw_input())
max = vote
min = vote
sum=vote
i = 1
while i<JUDGES:
    vote = float(raw_input())
    sum+=vote
    if vote > max:
        max = vote
    elif vote<min:
        min = vote
    i+=1

tot = (sum - max - min) * 2
print(tot)
