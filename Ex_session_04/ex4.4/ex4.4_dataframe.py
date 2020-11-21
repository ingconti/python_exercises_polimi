import pandas as pd

INFO_FILE_NAME = "info.txt"
N_OF_SAMPLES_KEY = "Number of samples"

FILE_PREFIX = "S_"
FILE_SUFFIX = ".gdm"


#new:
THRESHOLD = 0.19

#new
def readInfoFile():
	try:
		dataFrame = pd.read_csv(INFO_FILE_NAME", sep = '\t',  header = None)
		result = int(dataFrame.loc[5,1])
	except:
		result = 0
	return result

#the same
def process(nofFiles):
	for i in range(0,nOfFiles):
		fname = buildFileName(i)
		processFile(fname)

#the same
def buildFileName(index):
	s = FILE_PREFIX + '{:0>5}'.format(index)+FILE_SUFFIX
	return s


#new
def processFile(fname):
	print(fname)
	dataFrame = pd.read_csv(fname, sep = '\t',  header = None)
	dataFrame.columns = ['chr', 'start', 'end', 'strand', 'source', 'feature',
						 'score', 'frame', 'name', 'signal',
						'pvalue', 'qvalue', 'peak'
						 ]

	dataFrame['pvalue'] = pd.to_numeric(dataFrame['pvalue'])

	filtered = dataFrame[dataFrame['pvalue']/100 > THRESHOLD]

	width_df = filtered['end'] -  filtered['start']
	for v in width_df:
		print(v)
	#print(width_df.values)



#the same
nOfFiles = readInfoFile()
if nOfFiles>0:
	print(nOfFiles ," to be processed")
	process(nOfFiles)
else:
	print(INFO_FILE_NAME + " is missing")
