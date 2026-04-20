# st = input("Enter the String : ")

# rev = ""

# for ch in st :

#     rev = ch + rev

# print(rev)

# if rev == st :
#     print("Palindrome")

# else :
#     print("Not Palindrome")    


def checkRev(st) :
    rev = ""
    for ch in st : 

        rev = ch + rev

    if rev == st :
            print ("Palindrome")

    else : 
            print("Not Palindrome")    


    return rev    

rev = checkRev("trff")
print(rev)