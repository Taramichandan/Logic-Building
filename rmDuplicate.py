def remDup(arr) :
    unique = []
    check = {}

    for num in arr :

        if num not in check :

            check[num] = True
            unique.append(num)

    return unique        

remove = remDup([4,5,6,7,5,4,6])
print(remove)