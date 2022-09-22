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


# searchName()

# get search age from the user
def searchAge():
    infile = open("names.txt", "r")
    names_resulting_from_user_age_input = []
    age_number = input("Enter an age of your choice: ")
    for line in infile:
        if str(age_number) in line:
            age = line.split()
            names_resulting_from_user_age_input.append(age)

    print("The following names age = " + str(age_number) + ": => " + str(names_resulting_from_user_age_input))


# searchAge()


def main():
    print(" KINDLY PICK A CHOICE BELOW")
    print(" 1. Search with name")
    print(" 2. Search with age")

    userChoice = int(input("Enter the choice here men: "))

    if userChoice == 1:
        searchName()
    elif userChoice == 2:
        searchAge()
    else:
        print('oops!!! Invalid Choice!')


main()
