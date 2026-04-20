# num = int(input("Enter the number : "))

# for i in range(1 , 11) :

#     mul = num * i 

#     print(f"{num} * {i} : {mul}")    

 
def mul(num) :

    for i in range(1, 11) :
        
        mul = num * i

        print(f"{num} * {i} : {mul}")

        
num = int(input("Enter the number : "))
(mul(num))