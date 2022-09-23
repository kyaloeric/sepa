# again declare empty lists to store the output

numbers_divisible_by_sum_of_its_digits = []

r = range(1, 101, 1)
for num in r:
    sum_of_num = 0

    string_number = str(num)
    for i in string_number:
        sum_of_num += int(i)

    if num % sum_of_num == 0:
        numbers_divisible_by_sum_of_its_digits.append(num)

print('numbers divisible by sum of its digits: => ' + str(numbers_divisible_by_sum_of_its_digits))