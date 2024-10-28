##################################################
# Name: Matteo
# Collaborators:
# Estimate of time spent (hr): 
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    
    sumlist = []
    rowlist = [sum(i) for i in array]
    sumlist += rowlist
    collist = [0] * len(array)
    diag1=0
   
    for i in array:
        if len(i) != len(array):
            return False
        for j in range(len(i)):
            collist[j] += i[j]
            if j == array.index(i):
                diag1 += i[j]
    
    diag2 = [array[len(array)-1-i][i] for i in range(len(array)-1,-1,-1)]          
    sumlist += collist
    sumlist.append(diag1)
    sumlist.append(sum(diag2))

    for k in sumlist:
        if k != sumlist[0]:
            return False
    
    return True
    

        
            

small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))

