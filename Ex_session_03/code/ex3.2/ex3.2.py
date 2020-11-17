
FNAME = "patient_samples.csv"

def pressuresFrom(stringValues):
	result = []
	for s in stringValues[1:]:
		result.append(int(s))
	return result

def averagePressureFor(line):
	elements = line.split(',')
	elementsCount = len(elements)
	if elementsCount > 0:
		pressures = pressuresFrom(elements)
		# print(pressures)
		rowAvg = float( sum(pressures) / (elementsCount - 1) )
	else:
		rowAvg = 0
	return rowAvg

f = open(FNAME)
lines = f.read().splitlines()
numOfPatients = len(lines)
if numOfPatients > 0:
	maxAveragePressure = averagePressureFor(lines[0])
	indexOfPatient = 0
	for i in range(1,numOfPatients):
		line = lines[i]
		rowAvg = averagePressureFor(line)
		if rowAvg>maxAveragePressure:
			maxAveragePressure = rowAvg
			indexOfPatient = i

	surname = lines[indexOfPatient].split(',')[0]
	print(surname)
else:
	print(False)