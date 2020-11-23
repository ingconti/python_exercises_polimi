FILE_PREFIX = "samples_"
FILE_SUFFIX = ".csv"


def buildName(patientCode):
	fname = FILE_PREFIX + patientCode + FILE_SUFFIX
	return fname


def avgFrom(line):
	values = line.split(',')
	valuesCount = len(values)
	if valuesCount > 0:
		sum = int(values[0])
		for i in range(1, valuesCount):
			value = int(values[i])
			sum += value
		return float(sum / valuesCount)
	else:
		return 0.0

def process(fileName):
	try:
		f = open(fileName)
		lines = f.read().splitlines()
		lineCount = len(lines)
		if lineCount > 0:
			line = lines[0]  # take first only
			avg = avgFrom(line)
			print(avg)
			return True
		else:
			return False
	except:
		return False


patientCode = input('Enter patient''s code: ')
fileName = buildName(patientCode)
result = process(fileName)
if process(fileName) == False:
	print(False)

