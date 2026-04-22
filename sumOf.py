def sumOf(num) :

    sum = 0

    for i in range(1 , num + 1 ) :

        sum += i

    return sum

num = int(input("enter the number : "))

total = sumOf(num)

print(total) 