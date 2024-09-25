# import itertools
#
# list1 = [[1, 2], [3, 4], [5, 6]]
# list2 = [[11, 22], [33, 44]]
#
# for sub_list1, sub_list2 in itertools.zip_longest(list1, list2, fillvalue=""):
#     for item1, item2 in itertools.zip_longest(sub_list1, sub_list2, fillvalue=""):
#         print(item1, item2)

def test_dic():
    lane_values = {
        'lane0': ['0x0', '0x0'],
        'lane1': ['0x0', '0x0'],
        'lane2': ['0x0', '0x0']
    }

    # 获取字典 lane_values 中所有值的列表
    all_values = list(lane_values.values())

    print("所有值的列表:")
    print(all_values)


def test_split_string():
    input_string = "lane0 0x10198:0xd5f00 c-1:0x3 c0:0x15 c+1:0x0 margin&swing:0x0"

    # 分割字符串，首先按空格分割，提取 lane0
    parts = input_string.split()
    result = {parts[0]: {}}

    # 对剩余部分按冒号分割，构建字典
    for part in parts[1:]:
        key, value = part.split(":")
        result[parts[0]][key] = value

    print(result)


test_split_string()
