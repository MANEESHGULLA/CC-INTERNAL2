def lemonadeChange(bills):
    fives = 0
    tens = 0

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives == 0:
                return False
            fives -= 1
            tens += 1
        else:  # bill == 20
            if fives > 0 and tens > 0:
                fives -= 1
                tens -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True


print(lemonadeChange([5,5,5,10,20]))     # True
print(lemonadeChange([5,5,10]))          # True
print(lemonadeChange([10,10]))           # False
print(lemonadeChange([5,5,10,10,20]))    # False
