def countNum(arr):

    pos = 0
    nev = 0

    for n in arr :

        if n > 0 :

            pos += 1

        else :

            nev += 1

    return pos , nev            

print(countNum([-3,6,7,-4,1,9]))