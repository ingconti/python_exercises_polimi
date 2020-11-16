FNAME = "patients.csv"
SELECTED_WARDS = {"Cardiology", "Neurology"}
P_THRESH = 680

def patientDictFom(line):
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
        patient = patientDictFom(line)
        Hgmm = patient["Hgmm"]
        ward = patient["ward"]
        if Hgmm>P_THRESH and ward in SELECTED_WARDS:
            print(patient["name"], patient["surname"])
