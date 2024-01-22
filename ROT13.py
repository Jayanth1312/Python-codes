# manual version of EBG13 (decrypt the EBG13 to get ROT13)

import codecs


def main() -> None:
    user_input: str = input("Enter the Message: ")

    encrypted_message: str = codecs.encode(user_input, 'rot13')
    print(encrypted_message)


if __name__ == "__main__":
    main()
