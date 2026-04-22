def countNum (arr) :

    even = 0
    evenDict = {}

    odd = 0
    oddDict = {}

    for num in arr :

        if num % 2 == 0 :

            if num not in evenDict : 
                evenDict[num] = True 

                even += 1

                evenDict.append(even)


             

        else :

            odd += 1

    return even , evenDict , odd            

check  = countNum([3,4,6,5,1,7,9])

print(check)