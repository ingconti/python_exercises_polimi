FNAME = "visits.txt"  # TAB delimited

surnames =  []
firstVisits = []

def elementsFom(line):
    cleanedLline = line.rstrip('\r\n') # strip out all trailing whitespace
    elems = cleanedLline.split('\t')
    return elems

def dictFrom(surname, date):
    return {
        "surname": surname,
        "date" : date,
    }


#go line by line to save memory
f = open(FNAME)
next(f) #skip first
for line in f:
    elems = elementsFom(line)
    (surname,date) = elems
    if surname not in surnames:
        surnames.append(surname)
        d = dictFrom(surname, date)
        firstVisits.append(d)

for v in firstVisits:
    print(v["surname"], v["date"])
