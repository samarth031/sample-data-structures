def selection_sort(arr):
    """
    This method follows O(n^2)
    For further notes, refer https://www.geeksforgeeks.org/selection-sort/
    """
    for i, data in enumerate(arr):
#         print(i, data)
        min_data = i
        for j in range(i+1, len(arr)):
            if arr[min_data] > arr[j]:
                min_data=j
        arr[i], arr[min_data] = arr[min_data], arr[i]
    
    print(arr)
    
if __name == '__main__':
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    selection_sort(a)
