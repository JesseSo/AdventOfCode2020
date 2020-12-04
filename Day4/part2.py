import re

f = open("text.txt", "r")
fileLines = f.readlines()
dataLines = []
requiredColumnPassports = []
validByr = [1920, 2002]
validIyr = [2010, 2020]
validEyr = [2020, 2030]
validHgtCm = [150, 193]
validHgtIn = [59, 76]
validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
requiredValues = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
validPidLenght = 9;
cid = "cid:"

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
    if count == len(requiredValues) :
        requiredColumnPassports.append(line)
        count = 0
    else :
        count = 0

count = 0

for line in requiredColumnPassports :
    splitLine = line.split()
    splitLine.sort()
    for line in splitLine :
        if cid in line :
            splitLine.pop(1)
    if int(splitLine[0].split(":")[1]) >= validByr[0] and int(splitLine[0].split(":")[1]) <= validByr[1] :
        count = count + 1
    if splitLine[1].split(":")[1] in validEcl :
        count = count + 1
    if int(splitLine[2].split(":")[1]) >= validEyr[0] and int(splitLine[2].split(":")[1]) <= validEyr[1] :
        count = count + 1
    if re.search("^#.*[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]$", splitLine[3].split(":")[1]) :
        count = count + 1
    if splitLine[4].split(":")[1].endswith("in") or splitLine[4].split(":")[1].endswith("cm") :
        if splitLine[4].split(":")[1].endswith("in") :
            if int(splitLine[4].split(":")[1][:-2]) >= validHgtIn[0] and int(splitLine[4].split(":")[1][:-2]) <= validHgtIn[1] :
                count = count +1
        if splitLine[4].split(":")[1].endswith("cm") :
            if int(splitLine[4].split(":")[1][:-2]) >= validHgtCm[0] and int(splitLine[4].split(":")[1][:-2]) <= validHgtCm[1] :
                count = count +1
    if int(splitLine[5].split(":")[1]) >= validIyr[0] and int(splitLine[5].split(":")[1]) <= validIyr[1] :
        count = count + 1
    if len(splitLine[6].split(":")[1]) == validPidLenght :
        count = count + 1
    if count == 7 :
        validPassports = validPassports + 1
    count = 0 

print(validPassports+1)