def find_common_elements(list1, list2):
    common_elements = list(set(list1) & set(list2))
    return common_elements


list1 = [int(x) for x in input("list 1: ").split()]
list2 = [int(x) for x in input("list 2: ").split()]

result = find_common_elements(list1, list2)
print("Common elements:", result)
