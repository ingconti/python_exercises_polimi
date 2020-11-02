# Write a program that asks the user the number of patients of his ward.
# For every patient the program asks the surname, 10 integer measures of blood pressure (mmHg), saves them in a lists, computing and outputting
# The name of every patient with at least a measure of pressure 10% above the average of all measures.

N_OF_MEASURES = 10
patientNum = int(input())
nameAndmmHg = []

for i in range(0, patientNum):
    print("name of patient " + '{: >2}'.format(i) + ": ", end=" ")
    name = str(input())
    mmHG = [0] * N_OF_MEASURES

    for m in range(0, N_OF_MEASURES):
        print("measure " + '{: >2}'.format(m) + ": ", end=" ")
        mmHG[m] = int(input())

    nameAndmmHg.append([name, mmHG])

# dump to see:
for pd in nameAndmmHg:
    print (pd)

if patientNum > 0:
    sum = 0
    for patientAndData in nameAndmmHg:
        # print (patientAndData)
        for m in patientAndData[1]:
            sum += m

    # now we have sum:
    avg = sum / patientNum / N_OF_MEASURES
    print ("avg: " + str(avg))

    threeshold = avg * 1.1
    for patientAndData in nameAndmmHg:
        found = False
        i = 0
        while i < N_OF_MEASURES and not found:
            m = patientAndData[1][i]
            if m > threeshold:
                print (patientAndData[0])
                found = True
            else:
                i += 1
else:
    print(False)


