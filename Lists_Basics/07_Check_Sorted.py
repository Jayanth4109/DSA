def isSorted(self, arr, n):
        is_ascending = True
        is_descending = True
        
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                is_descending = False  
            elif arr[i] > arr[i + 1]:
                is_ascending = False  
        
        if is_ascending or is_descending:
            return 1
        else:
            return 0