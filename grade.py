score = input("Enter Score: ")
try:
    fscore = float(score)
except:
    print("Error! Use a number in digits")
    quit()

if fscore >= 0:
    if fscore < 0.6:
        print("F")
    elif fscore < 0.7:
        print("D")
    elif fscore < 0.8:
        print("C")
    elif fscore < 0.9:
        print("B")
    elif fscore <= 1.0:
        print("A")
    else:
        print("Error! Score must be between 0.0 and 1.0")
else:
    print("Error! Score must be between 0.0 and 1.0")
