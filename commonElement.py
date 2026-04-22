def commonEle (arr1 , arr2) :

    common = []
    for i in arr1 : 

        for j in arr2 :

            if i == j :

                if i not in common : 

                    common.append(i)

    return common



print(commonEle([2,3,4,5],[4,5,6,7]))