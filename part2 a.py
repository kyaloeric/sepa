# this program will print the names that start with an A form the file
def searchName():
    Names_starting_with_A = []
    infile = open("names.txt", "r")
    for line in infile:
        if line.startswith("A"):
            words = line.split()
            Names_starting_with_A.append(words)

    print("Names_starting_with_A: => " + str(Names_starting_with_A))


searchName()
