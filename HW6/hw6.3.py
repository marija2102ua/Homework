def calcul():
    """
 This function calculate the number
    of characters included in a given
    string
"""


string = input("Enter the string wich you want to count: ")
res = {i: string.count(i) for i in set(string)}
print("The count of all characters in stting is :" + str(res))
calcul()
