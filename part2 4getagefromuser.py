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


searchAge()
