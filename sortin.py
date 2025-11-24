def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        for j in range(0, n-i-1):
        
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



#Using .sort()

my_list = [3, 1, 4, 1, 5]
my_list.sort()
# Result: [1, 1, 3, 4, 5]                



#Using sorted()

my_list = [3, 1, 4, 1, 5]
new_list = sorted(my_list)
# Result: [1, 1, 3, 4, 5]