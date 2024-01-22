def combinations(digits):
    if not digits and '1' in digits:
        return []
    nums = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        
        for letter in nums[int(digits[index])]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations

input_digits = input("Enter digits (2-9): ")
print(result := combinations(input_digits))