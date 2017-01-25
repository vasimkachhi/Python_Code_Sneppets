"""
    This program return if given number is in power of two or not
"""
a = input("Enter a no\n")

if a & a-1 == 0:
    print "Is power of two"
else:
    print "Not power of two"
