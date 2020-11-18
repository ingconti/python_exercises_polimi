
FNAME = "patient_samples.csv"
f=open(FNAME)
lines = f.read().splitlines()

numOfPatients = len(lines)
if numOfPatients > 0:
	maxAveragePressure = 0
	indexOfPatient = 0
	for i in range(len(lines)):
		line = lines[i]
		elements = line.split(',')
		elementsCount = len(elements)
		if elementsCount > 0:
			pressures =  list(map(int, elements[1:]))  #take from 2nd AND convert ('map') from string to int
			#print(pressures)
			rowAvg = sum(pressures) / (elementsCount-1)
			if rowAvg>maxAveragePressure:
				maxAveragePressure = rowAvg
				indexOfPatient = i


	surname = lines[indexOfPatient].split(',')[0]
	print(surname)
else:
	print(False)