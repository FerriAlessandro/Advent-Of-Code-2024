def part1():

    l1 = []
    l2 = []
    distance = 0
    f = open("input.txt", "r")
    for line in f: 
        tmp = line.split()
        l1.append(int(tmp[0]))
        l2.append(int(tmp[1]))
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        if(l1[i] >= l2[i]):
            distance+=l1[i]-l2[i]
        else:
            distance+=l2[i]-l1[i]

    return distance

def part2():
    dic = {}
    l2 = []
    res = 0
    f = open("day1_input.txt", "r")
    for line in f: 
        tmp = line.split()
        dic[int(tmp[0])] = 0
        l2.append(int(tmp[1]))
    for val in l2: 
        if val in dic:
            dic[val]+=1
    for val in dic.keys():
        res+=(val*dic[val])
    
    return res

print(part2())