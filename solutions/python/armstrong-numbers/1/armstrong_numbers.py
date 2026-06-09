def is_armstrong_number(number):
    sum = 0;
    for num in str(number):
      sum += int(num) ** len(str(number))
    return sum == number
    
