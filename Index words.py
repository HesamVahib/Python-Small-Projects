sentence = input()
words = sentence.split()[1:]
lenWordsList = len(words)
deletedWord = []
c = 0
for dotWords in words:
   if c == lenWordsList - 1: break
   else:
    if '.' in dotWords:
        c += 1
        deletedWord.append(words[c])
    else:
        c += 1

capitalWords = dict()
counter  = 2
for each in words:
    if each in deletedWord:
         counter += 1
    elif each[0].isupper():
      each = each.strip(".")
      each = each.strip(",")
      capitalWords[counter] = each
      counter += 1
    else:
       counter += 1
wordsList = tuple(capitalWords.items())
if wordsList:
  for (indx, word) in wordsList:
    print(f"{indx}:{word}")
else:
   print('None')