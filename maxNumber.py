def maxNumber(arr) :
    maxNum = arr[0]

    for num in arr : 

        if num > maxNum :

            maxNum = num 

    return maxNum        

max = maxNumber([9,5,34,56,5])

print(max)