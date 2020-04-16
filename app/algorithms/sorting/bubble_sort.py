"""
Best case time complexity O(n)
Worst & average case time complexity O(n^2)
"""
def bubble_sort(item_list):
    n = len(item_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if item_list[j] > item_list[j+1]:
                item_list[j], item_list[j + 1] = item_list[j+1], item_list[j]
    return item_list

item_list = [12, 10, 22, 11, 25, 15]
print("Sorted list::", bubble_sort(item_list))
