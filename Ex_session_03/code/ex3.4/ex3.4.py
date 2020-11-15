FNAME = "visits.txt"  # TAB delimited

surnames = ()   # empty tuple (dont write:  = {} ...
firstVisits = []   # will be array of tuples

# protect against file is missing using "try":
try:
    #go line by line to save memory
    f = open(FNAME)
    next(f) #skip first
    for line in f:
        cleanedLline = line.rstrip('\r\n') # strip out all tailing whitespace
        elems = cleanedLline.split('\t')
        #print(elems)
        surname = elems[0]
        date = elems[1]
        if surname not in surnames:
            surnames = surnames + (surname, ) # tuples are immutable, create new ONE.
            # note sintax-pyton 3
            #surnames = (*surnames, surname)
            t = (surname, date)
            firstVisits.append(tuple(t))


    for v in sorted(firstVisits):
        print(v)
except:
    print(False)
