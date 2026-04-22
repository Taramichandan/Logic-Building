def repNev(arr) :
    replace = []
    for num in arr :

        if num < 0 :

            num = 0
            
        replace.append(num)

    return replace    

rep = repNev([4,-2,9,-5,6])
print(rep)