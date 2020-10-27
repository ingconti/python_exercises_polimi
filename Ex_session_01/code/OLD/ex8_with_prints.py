#ex 8 temperatures

INVALID_COORD = -1.0
SQUARE_BIG_DISTANCE = 10000000

print("your coordinates")
userX = float(raw_input())
userY = float(raw_input())

print("number of places:")
numberOfPlaces = int(raw_input())
maxTemperature = -273.0  # every temperature will be heigher.
minSquareDistance = SQUARE_BIG_DISTANCE
nearerX = INVALID_COORD
nearerY = INVALID_COORD
nearerTemperature = INVALID_COORD
indexOfNearest = 0
indexOfHottest = 0
n=0
while n<numberOfPlaces:
    print("coordinates at place " + str(n) )
    x = float(raw_input())
    y = float(raw_input())
    print("temperature at place " + str(n) )
    temperature = float(raw_input())
    deltaX = (userX - x)
    deltaY = (userY - y)
    squareOfDistance = deltaX * deltaX + deltaY * deltaY

    if squareOfDistance<minSquareDistance:
        nearerX = x
        nearerY = y
        nearerTemperature = temperature
        indexOfNearest = n
        minSquareDistance = squareOfDistance
    if temperature>maxTemperature:
        maxTemperature = temperature
        indexOfHottest = n
    n+=1

print(nearerX, nearerY, nearerTemperature)
if indexOfNearest == indexOfHottest:
    print("hottest too")
