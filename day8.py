with open('day8_input.txt') as f:
    content = f.read()


def create_nodes(input_list, child_node=0):
    nodes = input_list[0]
    metadata = input_list[1]
    input_list = input_list[2:]
    for n in range(nodes):
        input_list, child_node = create_nodes(input_list, child_node)
    for i in range(metadata):
        child_node += input_list[i]
    return input_list[metadata:], child_node


split = list(map(int, content.split()))
_, sum_of_metadata = create_nodes(split)
print(sum_of_metadata)


def calulate_root_node(input_list):
    nodes = input_list[0]
    metadata = input_list[1]
    input_list = input_list[2:]

    if nodes == 0:
        return input_list[metadata:], sum(input_list[:metadata])

    temp_list = []
    result = 0
    for n in range(nodes):
        input_list, sum_so_far = calulate_root_node(input_list)
        temp_list.append(sum_so_far)
    for i in range(metadata):
        if input_list[i] <= nodes:
            result += temp_list[input_list[i] - 1]
    return input_list[metadata:], result


split = list(map(int, content.split()))
_, result = calulate_root_node(split)
print(result)
