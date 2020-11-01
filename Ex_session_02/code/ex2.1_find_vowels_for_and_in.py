#Write a program that receives in input a string value and outputs the number of uppercase vowels it contains:

s = str(raw_input())
len = len(s)
upperCaseVowels = "AIOUE"
vowelsCount = 0

for i in range(0, len):
    if s[i] in upperCaseVowels:
        vowelsCount+=1
    i -= 1

print(str(vowelsCount))
