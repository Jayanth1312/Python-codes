def word_details(text: str) -> dict:
    details: dict = {'words': (words := text.split()),
                     'length': len(words),
                     'letters': len(''.join(words)),
                     'reversed': words[::-1]}
    return details

print(word_details(input("enter the word you like: ")))


inp = input("Enter Desired Word: ")

if (text := len(inp)) > 10:
    print("Too Long")
else:
    print("Correct size")

print((lambda x, y: x * y if x * y < 10 else 0)(1, 2))
print(x + y if (x := int(input('Enter Number 1: '))) + (y := int(input('Enter Number 2: '))) < 10 else 0)