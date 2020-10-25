print("part A - gimme a char:")
ch = input()
if ch>='A' and ch<='Z':
    ascii = ord(ch)
    print(ascii)
else:
    print("NOT capital letter")

print("part B - gimme a char:")
ch = input()

if ch>='a' and ch<='z':
    ascii = ord(ch)
    delta = ord('a') - ord('A')
    asciiUpperCase = ascii - delta
    print(chr(asciiUpperCase))
