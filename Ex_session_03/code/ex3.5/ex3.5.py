import csv

FNAME = "patients.csv"
#FNAME = "sample.csv"

SELECTED_WARDS = {"Cardiology", "Neurology"}

# protect against file is missing using "try":
try:
    f = open(FNAME)
    csv_reader = csv.DictReader(f, skipinitialspace = True)

    list_of_patients = list(csv_reader) # we got a list of dict

    for patient in list_of_patients:
        Hgmm = int(patient["Hgmm"])
        ward = patient["ward"]
        if Hgmm>680 and ward in SELECTED_WARDS:
            print(patient["name"], patient["surname"])
except:
    print(False)
