import re

def validateByr(byr):
    if int(byr) >= validByr[0] and int(byr) <= validByr[1] :
        return True
    else:
        return False

def validateEcl(ecl):
    if ecl in validEcl :
        return True
    else:
        return False

def validateEyr(eyr):
    if int(eyr) >= validEyr[0] and int(eyr) <= validEyr[1] :
        return True
    else: 
        return False

def validateHcl(hcl):
    if re.search("^#.*[a-f0-9]{6}$", hcl) :
        return True
    else:
        return False

def validateHgt(hgt):
    if hgt.endswith("in") :
        if int(hgt[:-2]) >= validHgtIn[0] and int(hgt[:-2]) <= validHgtIn[1] :
                return True
    if hgt.endswith("cm") :
        if int(hgt[:-2]) >= validHgtCm[0] and int(hgt[:-2]) <= validHgtCm[1] :
                return True
    return False

def validateIyr(iyr):
    if int(iyr) >= validIyr[0] and int(iyr) <= validIyr[1] :
        return True
    else:
        return False

def validatePid(pid):
    if len(pid) == validPidLenght :
        return True
    else:
        return False

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
    byr = splitLine[0].split(":")[1]
    ecl = splitLine[1].split(":")[1]
    eyr = splitLine[2].split(":")[1]
    hcl = splitLine[3].split(":")[1]
    hgt = splitLine[4].split(":")[1]
    iyr = splitLine[5].split(":")[1]
    pid = splitLine[6].split(":")[1]

    if validateByr(byr) and validateEcl(ecl) and validateEyr(eyr) and validateHcl(hcl) and validateHgt(hgt) and validateIyr(iyr) and validatePid(pid):
        validPassports = validPassports + 1

print(validPassports+1)