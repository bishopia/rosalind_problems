def readFile(filePath):
    """Reading a file and return a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def gc_content(seq):
    """ GC content of DNA/RNA sequence"""
    return round(
        ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


### --- read data from file (FASTA) ---

#store fasta file contents in a list
FASTAFile = readFile("../test_data/gc_content.txt")


### --- clean/prepare data ---

#Dictionary for data and header
FASTADict = {}

FASTALabel = ""

# print(FASTAFile)

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

# print(FASTADict)


### --- format data and ...---
### --- run operation (pass data to gc_content function) ---

RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

# print(RESULTDict)


### --- collect results ---

#look for head
maxGCKey = max(RESULTDict, key=RESULTDict.get)

# print(f'{maxGCKey}\n{RESULTDict[maxGCKey]}')

#remove header from report above
print(f'{maxGCKey[1:]}\n{RESULTDict[maxGCKey]}')

