numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number%5==0:
        print(numbers)
    elif number > 150:
        continue
    else:
        break 
    print(numbers)