"""
    This program checks if given number is a armstrong number
    Ex 407 = 4**3 + 0**3 +7**3
"""
a = input("Enter number\n")
l = len(str(a))
temp = a
sum = 0
while temp >0:
    digit = temp % 10
    sum += digit ** l # sum = sum + digit ** 10
    temp /= 10 # temp = temp /1 0
if sum == a:
    print "Is armstrong"
else:
    print "Is not armstrong"
