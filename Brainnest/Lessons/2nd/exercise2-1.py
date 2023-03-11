def rate_of_pay(hours, rate):
    try:
        tryhours = int(hours)
    except ValueError:
        print("integer input at hours required.")
        quit()
        
    try:
        tryrate = int(rate)
    except ValueError:
        print("integer input at pay required.")
        quit()
        
    extra_hours = 0
    if tryhours > 40:
        extra_hours = tryhours - 40
        tryhours = 40
        
    pay = tryhours * tryrate + extra_hours * 1.5 * tryrate

    print(f'with {tryhours + extra_hours} at a rate {tryrate} for the first 40 hours and 50% extra after. the pay will be: {pay}')
    
rate_of_pay(45, 10)