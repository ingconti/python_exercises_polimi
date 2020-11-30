import pandas as pd

YOUNG_15_19_FNAME = "SA_0000001760.csv"
ADULT_FNAME       = "SA_0000001400.csv"


# 15 / 19:

def filterYoungDataOnYearAndSex(df, year):
	filtered = df[ (df['YEAR'] == year) & (df['SEX'] == 'BTSX') ]
	return filtered


def readAndReduceYoungData(year):
	try:
		dataFrame = pd.read_csv(YOUNG_15_19_FNAME)
		# filter columns  needed:
		wantedColumns = ['YEAR', 'COUNTRY', 'SEX','Numeric']
		dataFrame = dataFrame[wantedColumns]
		dataFrame = filterYoungDataOnYearAndSex(dataFrame, year)

	except:
		# return empty dataframe:
		dataFrame = pd.DataFrame()

	return dataFrame

#adult:

def filterAdultDataOnYearAndAlcohol(df, year):
	filtered = df[ (df['YEAR'] == year) & (df['ALCOHOLTYPE'] == 'SA_TOTAL') ]
	return filtered



def readAndReduceAdultData(forYear):
	try:
		dataFrame = pd.read_csv(ADULT_FNAME)
		# filter columns  needed:
		wantedColumns = ['YEAR','COUNTRY','ALCOHOLTYPE','Numeric']
		dataFrame = dataFrame[wantedColumns]
		dataFrame = filterAdultDataOnYearAndAlcohol(dataFrame, forYear)
	except:
		# return empty dataframe:
		dataFrame = pd.DataFrame()

	return dataFrame




def askYear():
	ok = False
	while ok == False:
		year = input("type an year ")
		ok = year.isdigit()
		if ok == False:
			print("wrong input")

	return year



#main code:
# year = askYear()
year = 2010
young_15_19_df = readAndReduceYoungData(year)
if young_15_19_df.count == 0:
	print("no data")
else:
	adult_df = readAndReduceAdultData(year)
	if adult_df.count == 0:
		print("no data")
	else:

		print("done")
