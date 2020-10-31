# tRNA sequences are in a form like this:

#"GGGCCCGUAGCUCAGCCAGGUAGAGCGCCCGGCUCAUAACCGGGUGGUCGGGGGUUCAAAUCCCCCCGGGCCCACCA".
# Write a program that receives in input a string containing a sequence and outputs
# the number of occurrences of the triplet "GUA"
# don't use built-in "find" function.

#example: "GGGCCCGUAGCUCAGCCAGGUAG"
#output: 2

#only for test:
#seq = "GCGUACAGGUAG"
#triplet = "GUA"

seq = str(raw_input())
triplet = str(raw_input())

tripletLen = len(triplet)
len=len(seq)
i = 0
result = 0
stop = False

while i<len:
    j = 0
    matchesTilNow = 0
    while j<tripletLen and i+j < len and not stop:
        ch = seq[i+j]
        chInTriplet = triplet[j]
        if ch == chInTriplet:
            matchesTilNow += 1
            if matchesTilNow == tripletLen:
                result += 1
                i = i + j
        else:
            stop = True
        j += 1

    i += 1
    stop = False

print(result)

