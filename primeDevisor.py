numList = []
for i in range(10):
    inp = int(input())
    numList.append(inp)
num_devisor = dict()
for num in numList:
    counter = 0
    devide_list = []
    for devideCandidate in range(1, num+1):
        if num%devideCandidate == 0:
            devide_list.append(devideCandidate)
    for eachNum in devide_list:
        prime_counter = 0
        for i in range(1, eachNum+1):
            if eachNum%i == 0:
                prime_counter += 1
        if prime_counter == 2:
            counter += 1
    num_devisor[num] = counter
sortedResult = sorted(num_devisor.items(), key = lambda item: (-item[1], -item[0]))
print(f'{sortedResult[0][0]} {sortedResult[0][1]}')                  