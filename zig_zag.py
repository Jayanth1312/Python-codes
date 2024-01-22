def convert_to_zigzag(s, num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s

    rows = ['' for _ in range(num_rows)]   #array of empty strings

    # Initialize variables for direction and current row
    direction = -1  # moving up
    current_row = 0

    for char in s:     # Traverse the string and place characters in rows
        rows[current_row] += char
        if current_row == 0 or current_row == num_rows - 1:  # Changes the direction if at the top or bottom row
            direction *= -1
        current_row += direction

    result = ''.join(rows)  # Concatenation of rows
    return result

input_string = input()     #input string
num_rows = 3
zigzag_pattern = convert_to_zigzag(input_string, num_rows)
print(zigzag_pattern)