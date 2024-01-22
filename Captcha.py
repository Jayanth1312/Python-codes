from captcha.image import ImageCaptcha


def main() -> None:
    text: str = input('Enter the captcha: ')

    captcha: ImageCaptcha = ImageCaptcha(width=300,
                                         height=200,
                                         fonts=['C:/Windows/Fonts/Arial.ttf', 'C:/Windows/Fonts/Agencyr.ttf'],
                                         font_sizes=(40, 70, 100))

    captcha.write(text, 'captcha.png')


if __name__ == "__main__":
    main()
