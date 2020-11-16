iso1 = str(input('1st ISO code '))
iso2 = str(input('2nd ISO code '))
isoValues = [iso1, iso2]

FNAME = "TB_burden_age_sex_2020-11-05.csv"
#FNAME = "TB_burden_reduced.csv"
f=open(FNAME)
lines = f.read().splitlines()
nOfLines = len(lines)
if nOfLines > 0:
	sum = 0
	titleRow = lines[0].replace('"', '')
	columnsTitles = titleRow.split(',')
	columnOfBest =  columnsTitles.index('best')
	columnOfISOCode = columnsTitles.index('iso2')
	columnOfSex = columnsTitles.index('sex')
	for i in range(1, nOfLines):
		line = lines[i].replace('"', '')
		columnsValues = line.split(',')
		a = columnsValues[columnOfISOCode]
		b = columnsValues[columnOfSex]
		if columnsValues[columnOfISOCode] in isoValues and columnsValues[columnOfSex] == 'f':
			sum = sum + int(columnsValues[columnOfBest])
	print(sum)
else:
	print(False)
