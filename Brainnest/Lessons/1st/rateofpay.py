try:
    hours = int(input("hours: "))
except ValueError:
    print("integer input required.")
    quit()
    
try:
    rate = int(input("rate: "))
except ValueError:
    print("integer input required.")
    quit()
    
extra_hours = 0
if hours > 40:
    extra_hours = hours - 40
    hours = 40
    
pay = hours * rate + extra_hours * 1.5 * rate

print(f'with {hours + extra_hours} at a rate {rate} for the first 40 hours and 50% extra after. the pay will be: {pay}')