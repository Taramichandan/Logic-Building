# def missNum(arr) :

#     # n = len(arr) + 1

#     number = 0
#     total = 0

#     missing = 0


#     for num in range(5, 12) :

#         number += num

#     for numb in arr : 

#         total += numb


#     missing = number - total

#     return missing 

        
# print(missNum([5,6,7,8,9,11]))

def rmArr(arr) :
    unique = []

    check = {}

    for num in arr :

        if num not in unique:
            check[num] = True

            unique.append(num)

    return unique        


print(rmArr([2,3,5,4,5,4,2]))