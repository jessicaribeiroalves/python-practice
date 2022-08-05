def pairs_sum_to_target(list1, list2, target):
    pairs_list = []
    for x, element1 in enumerate(list1):
        for y, element2 in enumerate(list2):
            if (element1 + element2 == target):
                pairs_list.append([x, y])

    return pairs_list


list1 = [1, -2, 4, 5, 9]
list2 = [4, 2, -4, -4, 0]
target = 5
print(pairs_sum_to_target(list1, list2, target))


# Assumptions:
# Both lists will always have the same number of elements
# Pairs list can be returned in any order
