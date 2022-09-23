# print out the names after user has entered a certain input
def searchName():
    Names_starting_with_user_input = []
    user_input = str(input("Enter a  letter: ").upper())
    infile = open("names.txt", "r")
    for line in infile:
        if line[0:len(user_input)].startswith(user_input):
            correct_names = line.split()
            Names_starting_with_user_input.append(correct_names)
            print(correct_names)


searchName()
