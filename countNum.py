def count(arr):
    even = 0
    odd = 0

    for n in arr : 

        if n % 2 == 0 :

            even += 1

        elif n % 2 == 1 :
            
            odd += 1

    return even , odd

print(count([5,7,6,3,4,8]))