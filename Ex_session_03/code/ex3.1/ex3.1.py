
FNAME = "samples.csv"

f=open(FNAME)

lines = f.read().splitlines() #prevent if user has typed return.
lineCount = len(lines)
if lineCount > 0:
	line = lines[0]		#take first only
	elementsList = line.split(',')
	elementsCount = len(elementsList)
	sum = 0
	if elementsCount>0:
		max = int(elementsList[0])
		min = int(elementsList[0])
		for i in range(1, elementsCount):
			value = int(elementsList[i])
			sum += value
			if value >max:
				max = value
			elif value < min:
				min = value
		print(sum, max, min)
	else:
		print(False)

else:
	print(False)
