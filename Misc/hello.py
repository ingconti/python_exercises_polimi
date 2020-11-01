s = "AABBCCDDEE"
upperCaseVowels = "AIOUE"
vowelsCount = 0
        
for i in range(0, len(s)):
    if s[i] in upperCaseVowels:
        vowelsCount+=1
    i -= 1

print(str(vowelsCount))
