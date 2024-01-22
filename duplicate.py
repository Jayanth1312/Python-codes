def remove_duplicates_and_sort(input_string: str) -> str:
    # Create an empty list to store unique characters
    unique_chars = []

    # Iterate through each character in the input string
    for char in input_string:
        # If the character is not already in the unique_chars list, add it
        if char not in unique_chars:
            unique_chars.append(char)

    return ''.join(sorted(unique_chars))


if __name__ == '__main__':
    input_string = input()
    print(remove_duplicates_and_sort(input_string))

