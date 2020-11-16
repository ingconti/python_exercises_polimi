FNAME = "patients.csv"
SELECTED_WARDS = {"Cardiology", "Neurology"}

def patientDictFrom(line):
    cleanedLline = line.rstrip('\r\n') # strip out all tailing whitespace
    cleanedLline = cleanedLline.replace('"', '').replace(', ', ',')
    elems = cleanedLline.split(',')
    dict = {
        "name" : elems[0], "surname": elems[1], "Hgmm" : int(elems[2]),  "ward" : elems[3]
    }
    return dict

#go line by line to save memory
f = open(FNAME)
next(f) #skip first
for line in f:
    if len(line)>0:
        patient = patientDictFrom(line)
        Hgmm = patient["Hgmm"]
        ward = patient["ward"]
        if Hgmm>680 and ward in SELECTED_WARDS:
            print(patient["name"], patient["surname"])
