def day_converter(number):
    month = 0
    week = 0
    day = 0
    if number%30 == 0:
        month = number/30
    else:
        month = number//30
        week = (number%30)//7
        if week == 0:
            day = number/1
    day = ((number%30)%7)/1
    
    print(month,week, day)

day_converter(77)