value = input("Введыть чотирицифрове натуральне число ")
multiply = int(value[0])*int(value[1])*int(value[2])*int(value[3])
reverse = value[::-1]
sort = ''.join(sorted(value))

print(f"multiply: {multiply}")
print(f"reversed: {reverse}")
print(f"sort: {sort}")

