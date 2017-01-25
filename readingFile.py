"""
	This code reads the keys from text file and checks if that keys exists in json file.\
	Also returns line no of 8th occurance of word manila from text file
"""
count = 0
flag = True
for index, line in enumerate(open("test.txt").readlines()):
    d = str(line)
    count += d.count("manila")
    if count >= 8 and flag:
        print index + 1
        flag = False


import json
a = json.loads(open("testjson.json").read()).keys()
b = str(open("test.txt").read()).strip().split(",")
print a
print b
print list(set(a).intersection(set(b)))

print open("test.txt").readline(60)


x =  json.loads(open("testjson.json").read())
y = json.dumps(x)
print x
print y
