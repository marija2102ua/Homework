divisible2 = [n for n in range(1,11)if n % 2 == 0]
print(f'Even numbers that are divisible by 2 {divisible2}.')
divisible3 = [n for n in range(1,11)if n % 3 == 0]
print(f'Odd numbers, which are divisible by 3 {divisible3}.')
not_div_2_3= [n for n in range(1,11)if n % 2 != 0 and n % 3 != 0]
print(f'Numbers that are not divisible by 2 and 3 {not_div_2_3}.')