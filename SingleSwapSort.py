"""
    This program checks if list can be sorted in single swap or not
"""

# Method one
listdata = [1, 2, 3, 5, 4, 6, 5]
lst = list(listdata)

rev = sorted(listdata)
count = 0
for i in range(0, len(listdata)):
    if listdata[i] != rev[i]:
        count +=1
if count > 2:
    print "Can not be sorted in single swap"
else:
    print "Can be sorted in single swap"


# Method two
count =  0
for index1 in range(0, len(listdata)):
    for index2 in range(index1, len(listdata)):
        if listdata[index1] > listdata[index2]:
            listdata[index1], listdata[index2] = listdata[index2], listdata[index1]
            count += 1
            if count > 1:
                print "Can not be sorted in single Swap"
if count < 2:
    print "Can be sorted in single swap"

# Method Three
# Fastest method
count = 0
for k in range(0, len(lst)-1):
    if lst[k] > lst[k+1]:
        count += 1
if count > 1:
    print "Can not be sorted in single swap"
else:
    print "Can be sorted in single swap"
