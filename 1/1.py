list_of_numbers = []

with open('input.txt') as f:
    for line in f:
        list_of_numbers.append(int(line.rstrip('\n')))

for number in list_of_numbers:
    for secondNumber in list_of_numbers:
        for thirdNumber in list_of_numbers:
            sum = number + secondNumber + thirdNumber
            if sum == 2020:
                print(str(number*secondNumber*thirdNumber))
