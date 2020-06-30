# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between
# 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.


def getNumbers():
    number_list = []
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5 != 0:
            number_list.append(str(num))
    return ', '.join(number_list)


# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated
# sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320


def getFactorial(number):
    try:
        resulting_number = 1
        for num in range(1, number + 1):
            resulting_number *= num
    except TypeError as err:
        return err

    return int(resulting_number)


# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an
# integral number between 1 and n (both included). and then the program should print the dictionary.


def generateDictionary(number):
    try:
        return {int(num): num * num for num in range(1, number + 1)}
    except TypeError as err:
        return err
