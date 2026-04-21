def countFeq(arr) :
    freq = {} 

    for num in arr :

        if num in freq :

            freq[num] += 1

        else :
            freq[num] = 1

    return freq            


print(countFeq([4,5,6,7,3,3,4,4,5]))