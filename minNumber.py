def min_Num(arr) :

    minNum = arr[0]

    for num in arr :

        if num < minNum :

            minNum = num

    return minNum    


        

print(min_Num([3,5,7,9,4]))