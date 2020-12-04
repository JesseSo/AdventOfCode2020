f = open("text.txt", "r")
fileLines = f.readlines()
dataLines = []
requiredValues = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
optionalValue = "cid:"
oneLine = ""
count = 0
validPassports = 0

for line in fileLines :
    if line == "\n" :
        dataLines.append(oneLine.replace('\n', ' '))
        oneLine=""
    else :
        oneLine+=line
for line in dataLines :
    for value in requiredValues :
        if value in line :
            count += 1
    if count == len(requiredValues):
        validPassports += 1
        count = 0
    else :
        count = 0
print(validPassports+1)