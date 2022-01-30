def BubbleSort(array):

    lenght = len(array)-1

    for i in range(0,lenght):
        for j in range(0,lenght):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp

            
    return array


print(BubbleSort([3,5,2,1,8,9,6,4,7]))