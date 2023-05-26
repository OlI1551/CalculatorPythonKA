data = input()

a = data.count('+')
b = data.count('-')
c = data.count('*')
d = data.count('/')
operator_quantity = a + b + c + d

if operator_quantity != 1:
    print("throws exception")
else:
    for i in range(len(data)):
        if data[i] not in ['+', '-', '*', '/']:
            continue
        else:
            num1 = data[:i]
            operator = data[i]
            num2 = data[i + 1:]

    if len(num1) <= 0 or len(num2) <= 0:
        print("throws exception")
    else:
        num1 = num1.strip()
        num2 = num2.strip()

        if (num1 in "12345678910" and num1 != "") and (num2 in "12345678910" and num2 != ""):
            if operator == '+':
                print(int(num1) + int(num2))
            elif operator == '-':
                print(int(num1) - int(num2))
            elif operator == '*':
                print(int(num1) * int(num2))
            else:
                print(int(num1) // int(num2))

        elif (num1 in "IIIVIIIX" and num1 != "") and (num2 in "IIIVIIIX" and num2 != ""):
            num_roman = {
                'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
                'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10
            }

            if operator == '+':
                result = (num_roman[num1] + num_roman[num2])
            elif operator == '-':
                result = (num_roman[num1] - num_roman[num2])
            elif operator == '*':
                result = (num_roman[num1] * num_roman[num2])
            else:
                result = (num_roman[num1] // num_roman[num2])

            if result < 1:
                print("throws exception")
            else:
                num_arabic = {
                    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
                    20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX',
                    70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C'
                }

                tens = result // 10
                units = result % 10

                if result in num_arabic:
                    print(num_arabic[result])
                else:
                    print(num_arabic[tens*10] + num_arabic[units])

        else:
            print("throws exception")