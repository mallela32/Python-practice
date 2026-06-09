def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)

def total():
    total_grains = 0
    for num in range(1,65):
        total_grains += square(num)
    return total_grains
    
