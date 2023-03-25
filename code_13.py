
def get_merge_sorted_list(unsorted_list):

    if len(unsorted_list) == 1:
        return unsorted_list
    
    midland = int((len(unsorted_list))//2)

    east_side = unsorted_list[:midland]
    west_side = unsorted_list[midland:]

    half_east = get_merge_sorted_list(east_side)
    half_west = get_merge_sorted_list(west_side)

    return half_west + half_east

if __name__ == "__main__":

    unsorted_list = [28,45,96,22,88,56,90,10,63,79]

    print (get_merge_sorted_list(unsorted_list))    