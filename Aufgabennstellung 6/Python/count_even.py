def count_even(numbers):
    counter = 0
    for number in numbers:
        if (number % 2) == 0:
            counter += 1

    return counter


numberList = [1,2,4,8,9,10,14,6,3,5,7,9,13,14,15,16,17,18,200,101,211,122]

print(f"Anzahl gerader Zahlen: {count_even(numberList)}")
