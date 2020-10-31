#Write a program that receives in input a string value and outputs the number of uppercase vowels it contains:

s = str(raw_input())
i = len(s)-1
upperCaseVowels = "AIOUE"
vowelsCount = 0
while i >= 0:    
    if s[i] in upperCaseVowels:
        vowelsCount+=1
    i -= 1

print(str(vowelsCount))
