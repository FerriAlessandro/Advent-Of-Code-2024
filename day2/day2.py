def checkSequence_1(report):
    growth = 0 #-1 increasing, +1 decreasing
    i = 0
    okay=1
    while i < len(report)-1 and okay:
    
        if growth == 0:
            if report[0]>=report[1]:
                growth = 1
            else:
                growth = -1
        
        diff = report[i]-report[i+1]
        if diff == 0 or abs(diff) > 3 or diff//(abs(diff)) != growth:
            okay = 0
            break
        i+=1
    return okay


def checkSequence_2(report):
    growth = 0 #-1 increasing, +1 decreasing
    i = 0
    okay=1
    while i < len(report)-1 and okay:
    
        if growth == 0:
            if report[0]>=report[1]:
                growth = 1
            else:
                growth = -1
        
        diff = report[i]-report[i+1]
        if diff == 0 or abs(diff) > 3 or diff//(abs(diff)) != growth:
            if checkSequence_1(report[:i-1]+report[i:]) == 0 and checkSequence_1(report[:i]+report[i+1:]) == 0 and checkSequence_1(report[:i+1]+report[i+2:]) == 0:
                okay = 0
            break
        i+=1
    return okay



def part1():
    f = open("input.txt", "r")
    safe = 0
    for line in f: 
        input = line.split()
        report = [int(val) for val in input]

        safe+=checkSequence_1(report)
    return safe

def part2():

    f = open("input.txt", "r")
    safe = 0
    for line in f: 
        input = line.split()
        report = [int(val) for val in input]
        safe+=checkSequence_2(report)
    return safe

print(part2())