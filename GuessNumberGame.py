"""
    This program is for guess game where you will have guess which number in selected in ranint method
"""
import random
count = 0
no = random.randint(1, 100)
while True:
    count += 1
    if count <= 6:
        a = input("Enter your guess\n")
        if no < a:
            print "Wrong Guess, Try with smaller number"
        elif no > a:
            print "Wrong Guess, Try with larger number"
        elif no == a:
            print "Congratulations You WIN in %s Chances" % count
    else:
        print "You Lose . You have made maximum tries "
        print "Correct answer was %s" % no
        break
