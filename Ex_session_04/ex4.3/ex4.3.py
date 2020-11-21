import pandas as pd

FILE_NAME = "heart.csv"
FEMALE = 0

try:
    dataFrame = pd.read_csv(FILE_NAME)
    columns = dataFrame.columns
    #print(columns)
    filtered = dataFrame[
        (dataFrame['cp']<2) &
        (dataFrame['sex'] == FEMALE) &
        (dataFrame['exang'] == 1)
        ]
    #print(filtered)
    average = filtered['age'].mean()
    print(average)

except:
       print(False)


