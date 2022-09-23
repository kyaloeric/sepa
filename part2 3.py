# print ages that age is only 5
def searchAge():
    infile = open("names.txt", "r")
    lines_that_age_is_equal_to_5 = []
    age_number = 5
    for line in infile:
        if str(age_number) in line:
            age = line.split()
            lines_that_age_is_equal_to_5.append(age)

    print("In these lines age is only equal to 5: => " + str(lines_that_age_is_equal_to_5))


searchAge()
