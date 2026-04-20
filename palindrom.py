# num = int(input("Enter the digits : "))
# rev = 0

# while num > 0 :

#     dig = num % 10 
#     rev = rev * 10 + dig
#     num = num // 10

# print(rev)    

def revNum(num) :
    rev = 0

    while num > 0 :

        dig = num % 10 
        rev = rev * 10 + dig
        num = num // 10

    return rev    


rever = revNum(567)
print(rever)