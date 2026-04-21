def secMin(arr):
    min1 = float('inf')
    min2 = float('inf')

    if len(arr) < 2 :
        return None

    for num in arr :

        if num < min1 :

            min2 = min1
            min1 = num

        elif num < min2 and num != min1 : 
            min2 = num 

    return min2            

        

sec = secMin([5,7,9,3,6])

print(sec)