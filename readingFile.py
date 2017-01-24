count = 0
flag = True
for index, line in enumerate(open("E:\\vasimk\\BACKUP\\BACKUP\\PythonPract\\test1.txt").readlines()):
    d = str(line)
    count += d.count("manila")
    if count >= 8 and flag:
        print index + 1
        flag = False


import json
a = json.loads(open("E:\\vasimk\\BACKUP\\BACKUP\\PythonPract\\test2.json").read()).keys()
b = str(open("E:\\vasimk\\BACKUP\\BACKUP\\PythonPract\\test1.txt").read()).strip().split(",")
print a
print b
print list(set(a).intersection(set(b)))

print open("E:\\vasimk\\BACKUP\\BACKUP\\PythonPract\\test1.txt").readline(60)


x =  json.loads(open("E:\\vasimk\\BACKUP\\BACKUP\\PythonPract\\test2.json").read())
y = json.dumps(x)
print x
print y

