# tRNA sequences are in a form like this:

#"GGGCCCGUAGCUCAGCCAGGUAGAGCGCCCGGCUCAUAACCGGGUGGUCGGGGGUUCAAAUCCCCCCGGGCCCACCA".
# Write a program that receives in input a string representing a triplet, a string containing a sequence and outputs
# the number of occurrences of the given triplet.
# don't use built-in "find" function.

# example:
# "GUA"
# "GGGCCCGUAGCUCAGCCAGUAG"
# output: 2

triplet = str(raw_input())
seq = str(raw_input())

seqLen = len(seq)
tripletLen = len(triplet)

if tripletLen % 3 == 0:
    numtrip = 0
    for i in range(0, seqLen, 3):
        if seq[i:i+3] == triplet:
            numtrip = numtrip + 1
    print(numtrip)

else:
    print(False)


