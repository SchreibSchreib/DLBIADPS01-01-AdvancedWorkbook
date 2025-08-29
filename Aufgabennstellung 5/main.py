def sum_natural_numbers(max_value):
    if not isinstance(max_value, int) or max_value < 1:
        raise ValueError("Zahl muss eine natürliche Zahl >= 1 sein.")
    return _recursive_sum(max_value)

def _recursive_sum(current_number):
    if current_number == 1:
        return 1
    return current_number + _recursive_sum(current_number - 1)



print(sum_natural_numbers(1))
print(sum_natural_numbers(5))
print(sum_natural_numbers(50))
print(sum_natural_numbers(500))
