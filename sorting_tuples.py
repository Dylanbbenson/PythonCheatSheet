filename = input('Enter File: ')
if len(filename) < 1 : filename = 'text.txt' #default file
hand = open(filename)

dict = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dict[word] = dict.get(word,0) + 1   #count words

print(filename, " words with their counts: \n",dict, "\n")
x = sorted(dict.items())    #sort items based on place in file
print(filename, " words with their counts, sorted into tuples: \n",x,"\n")


tmp = list()
for k,v in dict.items():
    new_tup = (v,k)     #flip value and key
    tmp.append(new_tup)
print('Flipped: ', tmp)

tmp = sorted(tmp)       #reverse sort
print('Sorted: ', tmp)  #sorted alphabetically

tmp = sorted(tmp, reverse=True)     #reverse sorted alphabetically
print('Reverse Sorted: ', tmp)

print("5 most common words: ")
for v,k in tmp[:5]: #5 most common words
    print(k,v)