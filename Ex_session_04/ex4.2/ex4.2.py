MAX_BEDS = 10
MONTHS = ["January", "February", "March","April",
		  "May", "June", "July", "August",
		  "September", "October", "November", "December"]
MONTHS_NUM = len(MONTHS)  # ma se inchiodi la lista, perche' fai la fatica di andarla a scandire per vedere quanto e' lunga?

FILE_PREFIX = "bed_"
FILE_SUFFIX = ".txt"

def buildName(bedNumber):
	bedNumberStr = str(bedNumber)
	if len(bedNumberStr) < 2:
		bedNumberStr = FILE_PREFIX + '0' + bedNumberStr
	fname = bedNumberStr + FILE_SUFFIX
	return fname


#if not found, return ""
def findDataFor(fieldName, inLines):
	result = ""
	l = len(inLines)
	i = 0
	found = False

	while i < l and not found:
		info = inLines[i].split(':')
		if info[0] == fieldName:
			found = True
		else:
			i += 1
	if found:
		result = info[1].strip()
	return  result


def convertDate(s):
	result = "invalid month"
	#get month as index:
	yearStr = s[0:4]
	monthStr = s[5:7]
	dayStr = s[8:10]
	if monthStr.isdigit():
		index = int(monthStr)  - 1
		if index < MONTHS_NUM:
			monthName = MONTHS[index]

	result = yearStr + '-' + monthName + '-' + dayStr
	return result

def printPatientSurgeryData(lines):
	#use  array of field names to parse rows.
	keys = ['surname',  'name', 'surgery_date']
	patientRecord = ""
	for k in keys:
		s = findDataFor(k, lines)
		if len(s)>0: # test if we cannto find a valid field.
			if k != "surgery_date" :
				patientRecord = patientRecord + s + " "
			else:
				patientRecord = patientRecord + convertDate(s) + " "

	print(patientRecord)


def process(fileName):
	# print('processing ', fileName)
	try:
		f = open(fileName)		
	except:
		return False
	else:
		print('file name: ', fileName)
		lines = f.read().splitlines()
		printPatientSurgeryData(lines)
		f.close()
		
for bedNumber in range(1,MAX_BEDS):
	fileName = buildName(bedNumber)
	result = process(fileName)

