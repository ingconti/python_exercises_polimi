ADENINE = 'A'
CYTOSINE = 'C'
GUANINE = 'G'
THYMINE = 'T'
DNAELEM = ADENINE + CYTOSINE + GUANINE + THYMINE

FNAME = "refseqgene.5.genomic.fna"
#FNAME = "refseqgene.5.genomic_small.fna"

blocks = []
DNACount = 0
blockName = ""

f = open(FNAME)
# go line by line to save memory
for line in f:
    cleanedLline = line.rstrip('\r\n')  # strip out all tailing whitespace
    #print(cleanedLline)
    if cleanedLline.startswith('>NG_'):
        #close previous block if present:
        if len(blockName)>0:
            block = {'name': blockName, 'DNACount': DNACount}
            blocks.append(block)
            #and clear: (we saved)
            DNACount = 0
        #now the new block name:
        blockName = cleanedLline[13:]
    else: # line with DNA
        inRow = + cleanedLline.count(DNAELEM)
        #print(inRow)
        DNACount += inRow

#if here with name and count, add:
if len(blockName)>0:
   block = {'name': blockName, 'DNACount': DNACount}
   blocks.append(block)

for b in  sorted(blocks, key=lambda k: k['name']) :
    print( '{:0>4}'.format( b["DNACount"] ), b["name"])



