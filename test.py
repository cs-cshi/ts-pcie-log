# import itertools
#
# list1 = [[1, 2], [3, 4], [5, 6]]
# list2 = [[11, 22], [33, 44]]
#
# for sub_list1, sub_list2 in itertools.zip_longest(list1, list2, fillvalue=""):
#     for item1, item2 in itertools.zip_longest(sub_list1, sub_list2, fillvalue=""):
#         print(item1, item2)

lane_values = {
    'lane0': ['0x0', '0x0'],
    'lane1': ['0x0', '0x0'],
    'lane2': ['0x0', '0x0']
}

# 获取字典 lane_values 中所有值的列表
all_values = list(lane_values.values())

print("所有值的列表:")
print(all_values)