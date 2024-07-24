
num = input("Введите ваше число")
system = int(input("Введите систему счисления этого числа"))


def from_any_to_ten(num, system):
    if system == 16:
        return int(num, base=16)
    total = 0
    for i in range(len(num) - 1, -1, -1):
        total += int(num[len(num) - i - 1]) * system ** i
    return total

def from_any_to_ten_easy(num, system):
    return int(num, base=system)

def from_ten_to_any(num, system):
    total = ""
    num = int(num)
    if system > 9:
        while num >= system:
            if num % system <= 9:
                total += str(num % system)
            elif num % system == 10:
                total += "A"
            elif num % system == 11:
                total += "B"
            elif num % system == 12:
                total += "C"
            elif num % system == 13:
                total += "D"
            elif num % system == 14:
                total += "E"
            elif num % system == 15:
                total += "F"
            num = num // system
        else:
            total += str(num)
    elif system <= 9:
        while num >= system:
            total += str(num % system)
            num = num // system
        else:
            total += str(num)
    return total[::-1]

print(from_ten_to_any(num, system))


# i = 3
# total += 1 * 16^3 = 3
# i = 2
# total += 10 * 16^2 = 12
# i = 1
# total += 15 * 16^1 = 16
# i = 0
# total += 2 * 16^0 = 16