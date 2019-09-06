def merge_logic(s1, s2, full_arr):
        i = j = 0
        while i + j < len(full_arr):
            if (j == len(s2)) or (i < len(s1) and s1[i] < s2[j]):
                full_arr[i+j] = s1[i]
                i += 1
            else:
                full_arr[i+j] = s2[j]
                j += 1
                
                
def merge_sort(full_arr):
    if len(full_arr) < 2:
        return
    
    mid = len(full_arr)//2
    s1 = full_arr[:mid]
    s2 = full_arr[mid:]
    print(s1, s2)
    merge_sort(s1)
    merge_sort(s2)
    merge_logic(s1, s2, full_arr)
    print(full_arr)
