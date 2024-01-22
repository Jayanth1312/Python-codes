def intToRoman(num):
    roman = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''
    for key in roman:
        while num >= key:
            result += roman[key]
            num -= key
    return result


if __name__ == '__main__':
    num = int(input('enter the number: '))
    i = intToRoman(num)
    print(i)
