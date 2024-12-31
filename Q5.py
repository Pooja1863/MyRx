def sort_hashmap_by_value(input_map):
    sorted_map = dict(sorted(input_map.items(), key=lambda item: item[1]))
    return sorted_map

input_map = {101: "John Doe", 102: "Jane Smith", 103: "Peter Johnson"}
sorted_map = sort_hashmap_by_value(input_map)
print(sorted_map)