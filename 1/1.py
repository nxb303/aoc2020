list_of_numbers = []

with open('input.txt') as f:
    for line in f:
        list_of_numbers.append(int(line.rstrip('\n')))

for number in list_of_numbers:
    for secondNumber in list_of_numbers:
        sum_of_numbers = number + secondNumber
        if sum_of_numbers == 2020:
            print(f'Solution Part One: {str(number*secondNumber)}')

for number in list_of_numbers:
    for secondNumber in list_of_numbers:
        for thirdNumber in list_of_numbers:
            sum_of_numbers = number + secondNumber + thirdNumber
            if sum_of_numbers == 2020:
                print(f'Solution Part Two: {str(number*secondNumber*thirdNumber)}')
