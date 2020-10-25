count = 5
max = 0
min = 10
sum = 0
i = 0

while i<count:
    print("Judge ", i+1, " vote: ")
    vote = float(input())
    sum+=vote
    if vote > max:
        max = vote
    if vote<min:
        min = vote
    i+=1

print("sum:", sum, " max: ", max, " min: " ,min)

tot = (sum - max - min) * 2
print("total score:", tot)




