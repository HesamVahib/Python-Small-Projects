indx = int(input())

dic = dict()
for i in range(indx):
    translate = input().split()
    dic[translate[1]] = dic[translate[2]] = dic[translate[3]] = translate[0]

sentence = input().split()
tarjome = []
for word in sentence:
    if word in dic:
        word = dic[word]
    tarjome.append(word)

print (" ".join(tarjome))
