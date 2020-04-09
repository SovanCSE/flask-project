"""
Best case time complexity O(1)
Worst & average case time complexity O(n)
"""

def linear_search(list_items, target_item):
    found = False
    for index, item in enumerate(list_items):
        if item == target_item:
            print("Target item index: ", index)
            found = True
            break
    return found

print("Is target item found?", linear_search([2,8,5,9,12], 7))
print("Is target item found?", linear_search([2,8,5,9,12], 5))