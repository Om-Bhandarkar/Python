def search_count(my_list, search_element):
    count = 0
    for i in my_list:
        if i == search_element:
            count += 1
    return count

my_list = [1, 2, 3, 2, 5, 2, 7, 8, 9]
search_element = 2
print("Count of the search element is:", search_count(my_list, search_element))