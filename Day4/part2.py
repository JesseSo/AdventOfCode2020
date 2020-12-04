import re

def validateByr(byr):
    if int(byr) >= 1920 and int(byr) <= 2002 :
        return True
    else:
        return False

def validateEcl(ecl):
    if ecl in validEcl :
        return True
    else:
        return False

def validateEyr(eyr):
    if int(eyr) >= 2020 and int(eyr) <= 2030 :
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
        if int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76 :
                return True
    if hgt.endswith("cm") :
        if int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193 :
                return True
    return False

def validateIyr(iyr):
    if int(iyr) >= 2010 and int(iyr) <= 2020 :
        return True
    else:
        return False

def validatePid(pid):
    if len(pid) == validPidLenght :
        return True
    else:
        return False
    
def getDataInOneRow(lines):
    dataLines = []
    oneLine = ""
    for line in lines :
        if line == "\n" :
            dataLines.append(oneLine.replace('\n', ' '))
            oneLine=""
        else :
            oneLine+=line
    return dataLines

def getRowsWithRequiredValues(lines):
    count = 0
    requiredColumnPassports = []
    for line in getDataInOneRow(fileLines) :
        for value in requiredValues :
            if value in line :
                count += 1
        if count == len(requiredValues) :
            requiredColumnPassports.append(line)
        count = 0
    return requiredColumnPassports

f = open("text.txt", "r")
fileLines = f.readlines()
validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
requiredValues = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
validPidLenght = 9
validPassports = 0

for line in getRowsWithRequiredValues(getDataInOneRow(fileLines)) :
    splitLine = line.split()
    splitLine.sort()
    for line in splitLine :
        if "cid" in line :
            splitLine.pop(1)
    byr = splitLine[0].split(":")[1]
    ecl = splitLine[1].split(":")[1]
    eyr = splitLine[2].split(":")[1]
    hcl = splitLine[3].split(":")[1]
    hgt = splitLine[4].split(":")[1]
    iyr = splitLine[5].split(":")[1]
    pid = splitLine[6].split(":")[1]

    if validateByr(byr) and validateEcl(ecl) and validateEyr(eyr) and validateHcl(hcl) and validateHgt(hgt) and validateIyr(iyr) and validatePid(pid):
        validPassports += 1

print(validPassports+1)