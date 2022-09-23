r = range(1, 101, 1)
for number in r:
    sum_of_digits = 0
    n = number
    while n > 0:
        digit = n % 10
        sum_of_digits = sum_of_digits + digit
        n = n // 10
    sq_of_sum = sum_of_digits ** 2

    if number == sq_of_sum:
        print(number)
