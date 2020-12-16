number = int(input("Enter number: "))
i = 1
factorial = 1
while i <= number:
    factorial *= i
    i += 1
print("Factorial {}! = ".format(number), factorial)

#
# number = int(input("Enter number:  "))
# factorial = 1
# for i in range(1,number + 1):
#     factorial *= i
# print("Factorial {}! = ".format(number), factorial)