# Write a program that asks the user the number of patients of his ward.
# for every patient the program asks the surname, 10 integer measures of blood pressure (mmHg), saves them in a lists, computing and outputting
# the name of every patient with at least a measure of pressure 10% above the average of all meausures.

N_OF_MEASURES = 10
patientNum = int(input())
nameAndmmHg = []

for i in range(0, patientNum):
    print("patient name " + '{: >2}'.format(i) + ": ", end = "")
    name = str(input())
    for m in range(0, N_OF_MEASURES):
        mmHG[m] = int(input())
    nameAndmmHg = [name, mmHG]

#debug:
nameAndmmHg.append(["Smith",  [80, 90, 90, 95, 100, 120, 130, 150, 120, 90]])
nameAndmmHg.append(["Cooper", [80, 90, 90, 95, 100, 100, 70, 105, 101, 90]])
patientNum = len(nameAndmmHg)

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


