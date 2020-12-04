import re
filename = 'input.txt'

with open(filename) as file:
    passports = []
    passport_list_index = 0
    total_number_of_passports = 0
    number_of_valid_passports_part_1 = 0
    number_of_valid_passports_part_2 = 0

    # create a list of passport-features for each passport
    new_passport = True
    for line in file:
        if line == '\n':
            new_passport = True
            continue
        arguments = line.split(' ')
        if new_passport:
            passports.append(arguments)
            new_passport = False
            passport_list_index = len(passports) - 1
        else:
            passports[passport_list_index] += arguments

    # check if passports contain all necessary features
    for passport in passports:
        byr, iyr, eyr, hgt, hcl, ecl, pid, cid = False, False, False, False, False, False, False, False
        for feature in passport:
            key, value = feature.split(':')
            value = value.rstrip('\n')
            if 'byr' in feature:
                byr = True
            if 'iyr' in feature:
                iyr = True
            if 'eyr' in feature:
                eyr = True
            if 'hgt' in feature:
                hgt = True
            if 'hcl' in feature:
                hcl = True
            if 'ecl' in feature:
                ecl = True
            if 'pid' in feature:
                pid = True
            if 'cid' in feature:
                cid = True

        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            number_of_valid_passports_part_1 += 1

    # check if passports contain all necessary features and check for validity
    for passport in passports:
        byr, iyr, eyr, hgt, hcl, ecl, pid, cid = False, False, False, False, False, False, False, False
        for feature in passport:
            key, value = feature.split(':')
            value = value.rstrip('\n')
            if 'byr' in feature:
                if len(value) == 4 and 1920 <= int(value) <= 2002:
                    byr = True
            if 'iyr' in feature:
                if len(value) == 4 and (2010 <= int(value) <= 2020):
                    iyr = True
            if 'eyr' in feature:
                if len(value) == 4 and (2020 <= int(value) <= 2030):
                    eyr = True
            if 'hgt' in feature:
                if 'cm' in value:
                    height = int(value.rstrip('cm'))
                elif 'in' in value:
                    height = int(value.rstrip('in'))
                if ('cm' in value and (150 <= height <= 193))\
                        or ('in' in value and (59 <= height <= 76)):
                    hgt = True
            if 'hcl' in feature:
                if re.match('#[a-f0-9]{6}', value):
                    hcl = True
            if 'ecl' in feature:
                if value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth':
                    ecl = True
            if 'pid' in feature:
                if len(value) == 9:
                    pid = True
            if 'cid' in feature:
                cid = True

        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            number_of_valid_passports_part_2 += 1

    print(f'Solution Part 1: {number_of_valid_passports_part_1}')
    print(f'Solution Part 2: {number_of_valid_passports_part_2}')
