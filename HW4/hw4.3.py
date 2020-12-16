number = int(input("Enter number  "))
fibonacci_numbers =[0,1]
for i in range(2,number):
    fibonacci_numbers.append(fibonacci_numbers[i -1]+fibonacci_numbers[i-2])
    if fibonacci_numbers[i]==number:
        break
print("Fibonacci = {}  ".format(fibonacci_numbers))
