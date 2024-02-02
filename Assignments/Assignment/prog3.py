def digitCount(number):
    count = 0
    for i in str(number):
        count += 1
    return count

def evenDigitCount(number):
    count = 0
    for i in str(number):
        if int(i) % 2 == 0:
            count += 1
    return count

def oddDigitCount(number):
    count = 0
    for i in str(number):
        if int(i) % 2 != 0:
            count += 1
    return count

def main():
    number = 1234567890
    result = [digitCount(number), evenDigitCount(number), oddDigitCount(number)]
    print(result)

if __name__ == "__main__":
    main()