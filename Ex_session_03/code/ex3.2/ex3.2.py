
FNAME = "patient_samples.csv"
f=open(FNAME)
lines = f.read().splitlines()

def pressureFrom(stringValues):
	result = []
	for s in stringValues[1:]:
		result.append(int(s))
	return result

numOfPatients = len(lines)
if numOfPatients > 0:
	maxAveragePressure = 0 #no
	indexOfPatient = 0
	for i in range(len(lines)):
		line = lines[i]
		elements = line.split(',')
		elementsCount = len(elements)
		if elementsCount > 0:
			pressures = pressureFrom(elements)
			#print(pressures)
			rowAvg = float(sum(pressures)) / (elementsCount-1)
			if rowAvg>maxAveragePressure:
				maxAveragePressure = rowAvg
				indexOfPatient = i

	surname = lines[indexOfPatient].split(',')[0]
	print(surname)
else:
	print(False)
