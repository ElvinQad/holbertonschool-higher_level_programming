#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete the item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Create a new list without the element at idx
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
    
    # Clear the original list and add the new elements
    my_list.clear()
    for item in new_list:
        my_list.append(item)
    
    return my_list 