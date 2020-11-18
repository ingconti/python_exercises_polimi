FNAME = "TB_burden_age_sex_2020-11-05.csv"
#FNAME = "TB_burden_age_sex_2020-11-05_small.csv"
RISK_FNAME = "risks.txt"

def readRisks(name):
    f = open(name)
    lines = f.read().splitlines()
    return lines


def extractListFrom(str):
    wordList = []
    word = ""
    insideWord = False
    for c in str:
        if c == '"':
            insideWord = not insideWord

        if insideWord:
            if c != '"':
                word+=c
        else:
            if c == ',':
                wordList.append(word)
                word = ""
            else:
                if c != '"':
                    word+=c

    #if something remains
    wordList.append(word.rstrip('\r\n') )

    return wordList



def dictFrom(line):
    #print(line)
    elems = extractListFrom(line)
    dict = {}
    for i in range(0,len(elems)):
        dict[keys[i]] = elems[i]
    return dict

def addIfNotPresent(country, intoCountries):
    if country not in intoCountries:
        intoCountries.append(country)

riskfactors = readRisks(RISK_FNAME)
countries = []

#go line by line to save memory
f = open(FNAME)
line = f.readline()
keys = extractListFrom(line)
for line in f:
    if len(line)>0:
        d = dictFrom(line)
        lo = d["lo"]
        rf = d["risk_factor"]
        if rf in riskfactors and lo.isdigit() and int(lo)>10000:
            #some columns have NO data, so digit

            addIfNotPresent(country = d["country"], intoCountries = countries)

for c in sorted(countries):
    print(c)
