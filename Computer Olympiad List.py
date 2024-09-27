indx = int(input())
recordList = []
for i in range(indx):
    recordList.append(input())
recordList.sort(key= lambda word:(word[0], word.lower().split('.')[1][0]))
for each in recordList:
    eachWords = each.split('.')
    eachWords[1] = eachWords[1][0].upper()+eachWords[1][1:].lower()
    print(eachWords[0], eachWords[1], eachWords[2])