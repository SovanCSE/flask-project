"""
Best case time complexity O(1)
Worst & average case time complexity O(log n)
"""

def binary_search(list_items, target_item):
    first = 0
    last = len(list_items)-1
    found = False
    while(first <= last and not found):
        mid_point = (last + first)//2
        print("Mid:",mid_point)
        if list_items[mid_point] == target_item:
            print("Target item index position:", mid_point)
            found = True
        else:
            if list_items[mid_point] > target_item:
                last = mid_point - 1
                print("Last:",last)
            else:
                first = mid_point + 1
                print("First:", first)
    return found

print("Is target item found?", binary_search([2,3,4,5,9], 7))
print("Is target item found?", binary_search([2,3,4,5,6], 5))