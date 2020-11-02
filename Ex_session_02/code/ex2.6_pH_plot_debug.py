
### Write a program that asks the user 10 floats representing pH,
### saves them in a list, computing and outputting
### a plot of values using a '.'.


N_OF_SAMPLES = 10
pHSamples = [0] * N_OF_SAMPLES

#for i in range(0, N_OF_SAMPLES):
#    pHSamples[i] = float(raw_input())

pHSamples = [5.1, 6.0, 7.0, 8, 8.3, 7.6, 6.9, 9, 7.9, 5]

# find max and min to have a range:
maxPH_asInt = int(max(pHSamples))
minPH_asInt = int(min(pHSamples))

print (maxPH_asInt, minPH_asInt)

# start from highest
for s in range(maxPH_asInt, minPH_asInt-1, -1):
    line = '{:0>2}'.format(s) + ": "
    for i in range(0, N_OF_SAMPLES):
        sampleAsInt = int(pHSamples[i])
        if sampleAsInt == s:
            line += "."
        else:
            line += " "

    print(line)
