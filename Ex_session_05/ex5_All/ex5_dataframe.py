import pandas as pd
import matplotlib.pyplot as plt


YOUNG_15_19_FNAME = "SA_0000001760.csv"
ADULT_FNAME       = "SA_0000001400.csv"
ISO_FNAME         = "countries.csv"


# 15 / 19:

def filterYoungDataOnYearAndSex(df, year):
	filtered = df[ (df['YEAR'] == year) & (df['SEX'] == 'BTSX') ]
	# now we can delete 'SEX' column, and year, too:
	wantedColumns = ['COUNTRY', 'Numeric']
	filtered = filtered[wantedColumns]
	return filtered


def readAndReduceYoungData(year):
	try:
		dataFrame = pd.read_csv(YOUNG_15_19_FNAME)
		# filter columns  needed:
		wantedColumns = ['YEAR', 'COUNTRY', 'SEX','Numeric']
		dataFrame = dataFrame[wantedColumns]
		dataFrame = filterYoungDataOnYearAndSex(dataFrame, year)
		dataFrame.to_csv("young.csv", index=False)
	except:
		# return empty dataframe:
		dataFrame = pd.DataFrame()

	return dataFrame

#adult:

def filterAdultDataOnYearAndAlcohol(df, year):
	filtered = df[ (df['YEAR'] == year) & (df['ALCOHOLTYPE'] == 'SA_TOTAL') ]
	# now we can delete 'ALCOHOLTYPE' column,, and year, too:
	wantedColumns = ['COUNTRY', 'Numeric']
	filtered = filtered[wantedColumns]

	return filtered



def readAndReduceAdultData(forYear):
	try:
		dataFrame = pd.read_csv(ADULT_FNAME)
		# filter columns  needed:
		wantedColumns = ['YEAR','COUNTRY','ALCOHOLTYPE','Numeric']
		dataFrame = dataFrame[wantedColumns]
		dataFrame = filterAdultDataOnYearAndAlcohol(dataFrame, forYear)
		dataFrame.to_csv("adult.csv",index=False)
	except:
		# return empty dataframe:
		dataFrame = pd.DataFrame()

	return dataFrame


def mergeAndAddDelta(young_15_19_df, adult_df):
	# as both dataframe have the same "Numeric" value, we change thewm on fly
	# (not needed but more readable: if we don not rename, we will get:
	# COUNTRY,Numeric_x,Numeric_y as columns name

	merged = pd.merge(young_15_19_df, adult_df, on='COUNTRY')
	merged.columns = ['COUNTRY','Numeric_Young','Numeric_Adult'];
	merged = merged[merged['Numeric_Adult'] > 1.3 * merged['Numeric_Young'] ]
	#add columns:
	merged['delta'] = merged['Numeric_Adult'] - merged['Numeric_Young']
	merged.to_csv("cartesian.csv", index=False)
	return merged


def showDiagram(dataframe):
	dataframe.plot(kind = 'bar', x='name', y= 'delta')
	plt.xticks(fontsize=7)
	plt.show()


def askYear():
	ok = False
	while ok == False:
		year = input("type an year ")
		ok = year.isdigit()
		if ok == False:
			print("wrong input")

	return year


def replaceISOCode(df):
	try:
		ISO_dataFrame = pd.read_csv(ISO_FNAME)
		ISO_dataFrame['alpha3'] = ISO_dataFrame['alpha3'].str.upper()

		dataFrame = pd.merge(df, ISO_dataFrame, left_on='COUNTRY', right_on='alpha3')

		# strip un neede columns:
		wantedColumns = ['name', 'delta']
		dataFrame = dataFrame[wantedColumns]
	except:
		# return empty dataframe:
		dataFrame = pd.DataFrame()

	return dataFrame



#main code:
# year = askYear()
year = 2010
young_15_19_df = readAndReduceYoungData(year)
if young_15_19_df.empty:
	print("no data")
else:
	adult_df = readAndReduceAdultData(year)
	if adult_df.empty:
		print("no data")
	else:
		merged = mergeAndAddDelta(young_15_19_df, adult_df)
		with_ISO = replaceISOCode(merged)
		showDiagram(with_ISO)
		print("done")
