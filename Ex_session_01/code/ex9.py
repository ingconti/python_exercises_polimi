#ex 9 growing sequence

oldValue = 0
maxGrowingSequenceLen = 0
currGrowingSequenceLen = 0
n = 1

while n!=0:
    n = float(raw_input())
    if n>oldValue:
        currGrowingSequenceLen+=1
        oldValue = n
    else:
        oldValue = 0
        currGrowingSequenceLen = 0
        
    if currGrowingSequenceLen>maxGrowingSequenceLen:
        maxGrowingSequenceLen = currGrowingSequenceLen
    
print(maxGrowingSequenceLen)

