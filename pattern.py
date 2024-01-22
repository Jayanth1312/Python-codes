import re

pattern = input("Enter a pattern: ")
text = input("Enter a text: ")

matches = re.finditer(pattern, text)

count = sum(1 for _ in matches)

if count > 0:
    print(f"Pattern found {count} times.")
else:
    print("Pattern not found.")