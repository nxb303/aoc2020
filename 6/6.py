filename = 'input.txt'

with open(filename) as file:
    groups = []
    new_group = True
    group_index = 0

    for line in file:
        if line == '\n':
            new_group = True
            group_index += 1
            continue
        if new_group:
            groups.append([line.rstrip('\n')])
            new_group = False
        else:
            groups[group_index].append(line.rstrip('\n'))

    sum_of_counts = 0

    for group in groups:
        sum_of_counts += len(set(''.join(group)))

    print(f'Solution Part 1: {sum_of_counts}')

    sum_of_counts_part_two = 0
    for group in groups:
        list_of_sets_of_answers = []
        for person in group:
            list_of_sets_of_answers.append(set(person))

        sum_of_counts_part_two += len(set.intersection(*list_of_sets_of_answers))

    print(f'Solution Part 2: {sum_of_counts_part_two}')
