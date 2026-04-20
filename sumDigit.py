num = int(input("Enter the number : "))

rev = 0
sum = 0

while num > 0 :

    dig = num % 10
    rev = rev * 10 + dig 
    num = num // 10

    sum += dig

print(sum)    