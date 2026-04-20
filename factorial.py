# num = int(input("Enter the number : "))

# fact = 1

# for n in range(1, num + 1) :
#     fact = fact * n

# print(fact)    


def checkFact(num):
    
    fact = 1

    for n in range(1 , num + 1) : 

        fact *= n

    return fact    



print(checkFact(6))
