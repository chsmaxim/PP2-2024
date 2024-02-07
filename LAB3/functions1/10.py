def unique_elements(list):
    newlist = []
    
    for element in list:
        if element not in newlist:
            newlist.append(element)
    
    return newlist

input_list = input("list: ")
list = input_list.split()
result = unique_elements(list)

print(result)


