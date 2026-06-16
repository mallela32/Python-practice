def is_valid(isbn):
    str = isbn.replace('-','')
    if(len(str) != 10):
        return False
    sum = 0
    length = 10
    for index,char in enumerate(str):
        if index != 9 and char.isalpha():
            return False
        elif index == 9 and char.isalpha() and  char == 'X':
            sum += 10
        elif index == 9 and char.isalpha() and char != 'X':
            return False
        else:
            sum += int(char) * (length - index)
    return sum % 11 == 0
