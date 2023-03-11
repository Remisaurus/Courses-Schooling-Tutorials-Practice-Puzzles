fibonacci = [1, 2]
while fibonacci[-1] <= 4000000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
even_numbers = 0
for each in fibonacci:
    if (each % 2) == 0:
        even_numbers += each
print(even_numbers)