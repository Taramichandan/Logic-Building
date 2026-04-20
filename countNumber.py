
# num = int(input("Enter the number : "))

# rev = 0
# count = 0

# while num > 0 :

#     dig = num % 10
#     rev = rev * 10 + dig
#     num = num // 10

#     count += 1

# print(count)    


def count(num) :
    rev = 0
    count = 0

    while num > 0 :

        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10

        count += 1

    return count

num = int(input("Enter the Number : "))    

dig = count(num)

print(dig)
