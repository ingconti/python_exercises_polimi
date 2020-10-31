Write a program that receives in input a string value and outputs the number of uppercase vowels it contains:

s = str(raw_input())
i = len(s)-1
vowelsCount = 0
while i >= 0:    
    if s[i] == 'A' or s[i] == 'I' or s[i] == 'U' or s[i] == 'O' or s[i] == 'E':
        vowelsCount+=1

    i -= 1


print(str(vowelsCount))
