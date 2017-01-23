"""
    This Program is to Count occurrence on characters in String .
    And Returns character with Max  occurrence
"""


word = raw_input("Enter String \n")
dicti = {}
for char in word:
    try:
        dicti.update({char: dicti[char] + 1})
    except:
        dicti.update({char: 1})
maxchar = {pair[0]: pair[1] for pair in dicti.items() if pair[1] == max(dicti.values())}
print maxchar


from collections import Counter
import operator
a = Counter(word)
print (max(a.iteritems(), key=operator.itemgetter(1)))   # returns only first character with macx occurrence
maxchar = {pair[0]: pair[1] for pair in a.items() if pair[1] == max(a.values())}
print maxchar


data = {}
for i in word:
    data.update({i: data.get(i, 0) + 1})
maxchar = {pair[0]: pair[1] for pair in data.items() if pair[1] == max(data.values())}
print maxchar


z = {}
map(lambda x: z.update({x: z.get(x, 0) + 1}), word)
maxchar = {pair[0]: pair[1] for pair in z.items() if pair[1] == max(z.values())}
print maxchar

