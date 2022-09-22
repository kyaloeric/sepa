# declare empty lists for each part to store the output
divisible_by_7_and_3 = []
divisible_by_7and_not_3 = []
ODD_divisible_by_7_and_not_3 = []

r = range(1, 101, 1)
for i in r:
    # we are going to use the append() function to insert the i elements that fulfill the requirements
    # into the empty lists already declared above.

    # part A
    if (i % 7 == 0) and (i % 3 == 0):
        divisible_by_7_and_3.append(i)
    # part B
    if (i % 7 == 0) and (i % 3 != 0):
        divisible_by_7and_not_3.append(i)
    # part C
    if i % 2 != 0:
        if (i % 7 == 0) and (i % 3 != 0):
            ODD_divisible_by_7_and_not_3.append(i)

print("Divisible by both 7 and 3: => " + str(divisible_by_7_and_3))
print("Divisible by 7 but not 3: => " + str(divisible_by_7and_not_3))
print("ODD and Divisible by 7 and not 3: => " + str(ODD_divisible_by_7_and_not_3))
