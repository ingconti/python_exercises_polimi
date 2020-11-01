# ex 2.4
###

#Write a program that receives in input a sentence and outputs the occurrences of every char
# contained, in alphabetical order
# example:
# given:
# the quick brown fox jumps over the lazy dog
# you should have:
# [' ', 8]
# ['a', 1]
# ['b', 1]
# ['c', 1]
# ['d', 1]
# ['e', 3]
# and so on...

#test:
#s = "the quick brown fox jumps over the lazy dog"
s = str(input())

chars = ""
occurrences = []

for ch in s:
    l = len(occurrences)
    if l == 0:
        #first time:
        occurrences.append([ch, 1])
    else:
        l = len(occurrences)
        i = 0
        found = False
        while i<l and not found:
            couple = occurrences[i]
            if couple[0] == ch:
                couple[1] += 1
                found = True
            i += 1
        if not found:
            occurrences.append([ch, 1])

occurrences.sort()
for couple in occurrences:
    print(couple)


