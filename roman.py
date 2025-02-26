def int_to_roman(num: int) -> str:
    if num < 1 or num > 3999:
        raise ValueError("poe um valor menor ai porra")
    
    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""
    for value, symbol in roman_numerals:
        count = num // value
        result += symbol * count
        num %= value
    return result

try:
    numero = int(input('fala um numero ai pai: '))
    print(f'o numero {numero} em algarismos romanos e: {int_to_roman(numero)}')
except ValueError as e:
    print(f"erro: {e}")
