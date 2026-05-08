numbers = [1,2,3,4,5,6,7,9,10,11,12,13]

def binary_search(numbers,element):

    if len(numbers) == 1:
        print(numbers[0])
        return 0
    
    elif numbers[len(numbers)//2] == element:
        print(numbers[len(numbers)//2])
        return 0
    
    elif element > numbers[len(numbers)//2]:
        divide = numbers[(len(numbers)//2)+1:]
        binary_search(divide,element)
        return 0
    
    else:
        divide = numbers[0:len(numbers)//2]
        binary_search(divide,element)
        return 0

binary_search(numbers,9)