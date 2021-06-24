dnaCode = []
rnaCode = ""
strDna = input("Please enter DNA code: ")
dnaCode[:0] = strDna


for i in range(len(dnaCode)):
    if(dnaCode[i] == "A"):
        dnaCode[i] = "T"
    elif(dnaCode[i] == "C"):
        dnaCode[i] = "G"
    elif(dnaCode[i] == "G"):
        dnaCode[i] = "C"
    elif(dnaCode[i] == "T"):
        dnaCode[i] = "A"

# DNA -> RNA
for i in range(len(dnaCode)):
    if(dnaCode[i] == "T"):
        dnaCode[i] = "U"

for i in dnaCode:
    rnaCode += i

geneticCodeTable = {
    "UUU": "F", "UUC": "F", "UUA": 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L','CUA': 'L','CUG': 'L',
    'AUU': 'I','AUC': 'I','AUA': 'I','AUG': 'M',
    'GUU':'V','GUC': 'V','GUA': 'V','GUG': 'V',
    'UCU': 'S','UCC': 'S','UCA': 'S','UCG': 'S',
    'CCU': 'P','CCC': 'P','CCA': 'P','CCG': 'P',
    'ACU': 'T','ACC': 'T','ACA': 'T','ACG': 'T',
    'GCU': 'A','GCC': 'A','GCA': 'A','GCG': 'A',
    'UAU': 'Y','UAC': 'Y','UAA': '.','UAG': '.',
    'CAU': 'H','CAC': 'H','CAA': 'Q','CAG': 'Q',
    'AAU': 'N','AAC': 'N','AAA': 'K','AAG': 'K',
    'GAU': 'D','GAC': 'D','GAA': 'E', 'GAG': 'E',
    'UGU': 'C','UGC':'C','UGA': '.', 'UGG': 'W',
    'CGU': 'R','CGC': 'R','CGA': 'R','CGG': 'R',
    'AGU': 'S','AGC': 'S','AGA': 'R','AGG': 'R',
    'GGU': 'G','GGC': 'G', 'GGA': 'G','GGG': 'G'
}

proteinString = ""

for i in range(0, len(rnaCode), 3):
    #if(geneticCodeTable[rnaCode[i:i+3]] == "."):
        #break
    proteinString += geneticCodeTable[rnaCode[i:i+3]]

print("RNA code: ",rnaCode)
print("Protein String: ",proteinString) 
