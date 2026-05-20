def bubble_sort(A):
    n = len(A)
    for i in range(0,n):
        
        for j in range(n-1):
            if(A[j]>A[j+1]):
                A[j+1],A[j] = A[j],A[j+1]
                
                
                
    return A
    

def Merge(left,right):
    B = []
    i = 0
    j = 0
    while i in range(0,len(left)) and j in range(0,len(right)):
        if(left[i]<right[j]):
            B.append(left[i])
            i+=1                                                            #Merge sort of 2 sorted list
        else:
            B.append(right[j])
            j+=1
    B.extend(left[i:])
    B.extend(right[j:])
    return B

def Merge_sort(arr):
    if len(arr)==1:
        return arr
    else:
        left = Merge_sort(arr[:(len(arr)//2)])
        right = Merge_sort(arr[(len(arr)//2):])                             #Merge sort of the single list
    
    return Merge(left,right)

print(bubble_sort([99,5,2,3,4,6,88]))




    



