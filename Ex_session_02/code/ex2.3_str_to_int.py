# Write a program that asks the user a string containing only numeric chars, computing and outputting the corresponding integer value,
# or False if input contains non-numeric characters.

seq = raw_input()
if seq.isdigit():
    val = int(seq)
    isValid = True
else:
    isValid = False

if isValid:  #prima il caso che vorremmo avere
    print(str(val))
else:
    print(isValid)

