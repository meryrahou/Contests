number = input()
sorted_number = input()

digits = [digit for digit in number if digit != '0']
zero_count = number.count('0')

digits.sort()

if not digits:
    if '0' == sorted_number:
        print("OK")
    else:
        print("WRONG_ANSWER")
elif str(digits[0]) + '0'* zero_count + ''.join(digits[1:]) == sorted_number:
    print("OK")
else:
    print("WRONG_ANSWER")

