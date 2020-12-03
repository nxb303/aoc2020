list_of_passwords = []
number_of_correct_passwords = 0
number_of_correct_passwords_part_two = 0
with open('input.txt') as f:
    for line in f:
        split_line = line.split(sep=' ')
        bounds = split_line[0].split(sep='-')
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])
        character = split_line[1].rstrip(':')
        password = split_line[2].rstrip('\n')

        occurence = password.count(character)
        if bool(password[lower_bound - 1] == character) != bool(password[upper_bound - 1] == character):
            number_of_correct_passwords_part_two += 1
        if lower_bound <= occurence <= upper_bound:
            number_of_correct_passwords += 1

print(number_of_correct_passwords)

print(number_of_correct_passwords_part_two)
# for number in list_of_numbers:
#     for secondNumber in list_of_numbers:
#         for thirdNumber in list_of_numbers:
#             sum = number + secondNumber + thirdNumber
#             if sum == 2020:
#                 print(str(number*secondNumber*thirdNumber))
