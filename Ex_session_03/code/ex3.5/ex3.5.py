import csv

FNAME = "TB_burden_age_sex_2020-11-05.csv"
RISK_FNAME = "risks.txt"

with open(RISK_FNAME) as f_risk:
    lines = f_risk.read().splitlines()
    riskfactors = set(lines)  # build a set.

# protect against file is missing using "with":
with open(FNAME) as f:
    countries = set()
    csv_reader = csv.DictReader(f)
    list_of_rows = list(csv_reader)
    for row in list_of_rows:
        #print(row)
        lo = row["lo"]
        if lo.isdigit() and int(row["lo"])>100 :
            countries.add(row["country"])

    for c in sorted(countries):
       print(c)
