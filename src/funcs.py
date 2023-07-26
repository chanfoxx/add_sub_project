def add(num_1, num_2):
    """Складывает два числа."""
    try:
        result = int(num_1 + num_2)
    except TypeError:
        return "Operand type's must be a number."
    else:
        return result


def sub(num_1, num_2):
    """Вычитает одно число из другого."""
    try:
        result = int(num_1 - num_2)
    except TypeError:
        return "Operand type's must be a number."
    else:
        return result
