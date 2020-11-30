import pandas as pd

YOUNG_15_19_FNAME = "SA_0000001760.csv"
ADULT_FNAME       = "SA_0000001400.csv"


def readAndReduceYoungData():
	try:
		dataFrame = pd.read_csv(YOUNG_15_19_FNAME)
		# filter columns  needed:
		wantedColumns = ['YEAR', 'SEX','Numeric']
		dataFrame = dataFrame[wantedColumns]

	except:
		# return empty dataframe:
		dataFrame = pd.DataFrame()

	return dataFrame


def readAndReduceAdultData():
	try:
		dataFrame = pd.read_csv(ADULT_FNAME)
		# filter columns  needed:
		wantedColumns = ['YEAR', 'SEX','Numeric']
		dataFrame = dataFrame[wantedColumns]

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


def filterDataOnYear(df, forYear):
	filtered = df[df['YEAR'] == forYear]
	return filtered

#main code:
# year = askYear()
year = 2010
young_15_19_df = readAndReduceYoungData()
if young_15_19_df.count == 0:
	print("no data")
else:
	young_15_19_filtered_df = filterDataOnYear(young_15_19_df, year)
	if young_15_19_filtered_df.count == 0:
		print("no data")
	else:
		adult_df = readAndReduceAdultData()
		print("done")
