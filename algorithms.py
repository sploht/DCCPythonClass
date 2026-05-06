def bubble_sort(contact_list):
    swaps = 0
    for i in range(len(contact_list)-1):
        for j in range(len(contact_list)-i-1):
            if contact_list[j+1] < contact_list[j]:
                contact_list[j+1], contact_list[j] = contact_list[j], contact_list[j+1]
                swaps += 1
        if swaps == 0:
            break

def binary_search(contact_list, lower_index, upper_index, target_contact):
    if lower_index <= upper_index:
        midpoint = (lower_index+upper_index) // 2
        if contact_list[midpoint] == target_contact:
            return midpoint
        elif (contact_list[midpoint] > target_contact):
            return binary_search(contact_list, lower_index, midpoint-1, target_contact)
        else:
            return binary_search(contact_list, midpoint+1, upper_index, target_contact)
    return -1