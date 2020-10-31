# Distance between lower and upper case of the same char is 32.
# Write a program that receives in input a string and outputs the corresponding uppercase string.

TO_UPPERCASE = True
LOWERCASE_TO_UPPERCASE_DELTA = 32
s = str(raw_input())
i = 0
result = ""
while i<len(s):
    asciiCode = ord(s[i])
    if TO_UPPERCASE and asciiCode >= ord('a') and asciiCode <= ord('z'):
        result += chr(asciiCode - LOWERCASE_TO_UPPERCASE_DELTA)
    elif not TO_UPPERCASE and asciiCode >= ord('A') and asciiCode <= ord('Z'):
        result += chr(asciiCode + LOWERCASE_TO_UPPERCASE_DELTA)
    else:
        result += chr(asciiCode)
    i += 1

print(result)
