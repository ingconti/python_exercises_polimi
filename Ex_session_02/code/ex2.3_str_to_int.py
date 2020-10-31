# Write a program that asks the user a string containing only numeric chars, computing and outputting the corresponding integer value,
# or False if input contains non-numeric characters.

#Write it without using "int()" buit-in cast.

BASE = 10
wrongCharFound = False
s = str(raw_input())
i = 0
powerOfTen=1
result = 0
while i<len(s) and not wrongCharFound:
    digit = s[i]
    if digit<'0' or digit>'9':
        wrongCharFound = True
    else:
        intValue = ord(digit)-48
        result = result * BASE + intValue
        i += 1

if wrongCharFound:
    print(False)
else:
    print(result)
