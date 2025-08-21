def count_even(list_of_numbers):
    counter = 0
    for number in list_of_numbers:
        if (number % 2) == 0:
            counter += 1

    return counter


number_list = [1,2,4,8,9,10,14,6,3,5,7,9,13,14,15,16,17,18,200,101,211,122]

print(f"Liste: {number_list}")
print(f"Anzahl gerader Zahlen: {count_even(number_list)}")
