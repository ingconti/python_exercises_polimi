# Write a program that asks the user 12 integer weather temperatures for the current year, saves them in a list, computing and outputting
# an histogram plot of values using a '*'.
# the histogram spans from min to max degrees.
# write the scale on left.

N_OF_MONTHS = 12
temperatures = [0] * N_OF_MONTHS

#for i in range(0, N_OF_MONTHS):
#    temperatures[i] = int(raw_input())

temperatures = [5,6,7,12,16,25,26,22,18,10,5,4]

# find max and min to have a range:
maxT = max(temperatures)
minT = min(temperatures)

tempRange = maxT - minT
# start from highest

for t in range(maxT, minT, -1):
    line = '{:0>2}'.format(t) + ": "
    for i in range(0, N_OF_MONTHS):
        if temperatures[i] >= t:
            line += "*"
        else:
            line += " "

    print(line)
