def check(index, line, a):
    line = str(line)
    if index > 0:
        try:
            indbef = str(a[index - 1]).index("C")
        except:
            indbef = str(a[index - 1]).index("_")

    if line.__contains__("C"):
        if index == 0:
            line = line.replace("C", "|")
        else:
            indnow = line.index("C")
            line = line.replace("C", "\\" if indnow > indbef else "/")
    elif line.__contains__("_"):
        if index == 0:
            line = line.replace("_", "|")
        else:
            indnow = line.index("_")
            line = line.replace("_", "\\" if indnow > indbef else "/")
    return line


a = open("input.txt").readlines()
for index, line in enumerate(a):
    print check(index, line, a)



