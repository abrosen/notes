

def insertion_sort(array):
    target_index = 1
    while target_index < len(array):
        target = array[target_index]
        for i in range(0, target_index+1):
            if array[i] > target:
                array[i], target = target, array[i]
        array[target_index] = target
        target_index += 1
        print(array)
    return array

def o    