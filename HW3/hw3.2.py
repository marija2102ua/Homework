value = int(input("Введыть чотирицифрове натуральне число "))
fourth = value % 10
third = value // 10 % 10
second = value // 100 % 10
first = value // 1000
multiply = first*second*third*fourt
print(first*second*third*fourth)



# value = input("Введыть чотирицифрове натуральне число ")
# multiply = int(value[0])*int(value[1])*int(value[2])*int(value[3])
# reverse = value[::-1]
# sort = ''.join(sorted(value))
#
# print(multiply)
# print(reverse)
# print(sort)
