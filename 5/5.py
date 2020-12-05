filename = 'input.txt'


class BoardingPass:
    def __init__(self, r, c):
        self.row = r
        self.column = c

    def seat_id(self):
        return (self.row * 8) + self.column

    def __str__(self):
        return f"Row: {self.row}, Column: {self.column}, SeatID: {self.seat_id()}"


with open(filename) as file:
    max_seat_id = 0
    min_row = 127
    max_row = 0
    boarding_passes = []

    for line in file:
        boarding_pass_encoded = line.rstrip('\n')
        # the first 7 characters of the boarding pass code encode the row
        row_encoded = boarding_pass_encoded[0:7]
        # the 3 characters after the encoded row encode the column
        seat_encoded = boarding_pass_encoded[7:11]
        row, column = 0, 0
        # to get the number of the row and column, we just have to leftshift zeroes for Fs or Ls and ones for Bs or Rs
        for index, char in enumerate(row_encoded):
            row |= ((1 if char == 'B' else 0) << 6 - index)
        for index, char in enumerate(seat_encoded):
            column |= ((1 if char == 'R' else 0) << 2 - index)

        boarding_pass = BoardingPass(row, column)
        boarding_passes.append(boarding_pass)

        # get the max. seat id
        if boarding_pass.seat_id() > max_seat_id:
            max_seat_id = boarding_pass.seat_id()

    # create a list of all seat ids
    seat_ids = []
    for bp in boarding_passes:
        seat_ids.append(bp.seat_id())

    # get the smallest and highest seat ids
    # our seat is not in the front or back, so the missing seat id has to be in between the smallest and highest seat id
    seat_ids.sort()
    smallest_seat_id = seat_ids[0]
    highest_seat_id = seat_ids[len(seat_ids) - 1]
    missing_seat_id = 0
    # find out, which seat id is missing
    for x in range(smallest_seat_id, highest_seat_id):
        if x not in seat_ids:
            missing_seat_id = x

    print(f'max seat id: {max_seat_id}')
    print(f'your seat id: {missing_seat_id}')
