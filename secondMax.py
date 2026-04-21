def secMax(arr) :
    
    first = float('-inf')
    second = float('-inf')

    if len(arr) < 2 :
        return None
    
    for num in arr :

        if num > first : 
            second = first 
            first = num

        elif num > second and num != first :
            second = num

    return second        


secondMax = secMax([3,5,6,7,8])
print(secondMax)