# Distance between lower and upper case of the same char constant: OFFSET = ord(a') - ord(A')
# Write a program that receives in input a string and outputs the corresponding uppercase string.
# Use a const so you can easily switch to lowercase

TO_UPPERCASE = True
LOWERCASE_TO_UPPERCASE_DELTA = OFFSET = ord('a') - ord('A')
s = str(raw_input())
i = 0
l = len(s)

result = ""
for i in range(0, l):
    asciiCode = ord(s[i])
    if TO_UPPERCASE and asciiCode >= ord('a') and asciiCode <= ord('z'):
        result += chr(asciiCode - LOWERCASE_TO_UPPERCASE_DELTA)
    elif not TO_UPPERCASE and asciiCode >= ord('A') and asciiCode <= ord('Z'):
        result += chr(asciiCode + LOWERCASE_TO_UPPERCASE_DELTA)
    else:
        result += chr(asciiCode)
    #i += 1

print(result)
