from input import raw_licence, part_1_answer, part_2_answer


license = [int(data) for data in raw_licence.split(' ')]
metadata_sum = 0


def process_node(offset):
    """
    Process a node in the tree which starts at the specified offset of the license. This method calls itself recursively
        to process the entire tree represented in the tree datastructure in the license.
    We will sum the metadata values in metadata_sum as a side effect.

    Args:
        offset(int): The index of the node in the licence list.

    Returns:
        int: The index of the last position of the node.
    """
    global metadata_sum
    # if values[]

    num_children = license[offset]
    num_metadata = license[offset + 1]

    # If we have children, process those children and fetch the end offset of the last child.
    # First, we have to add two to the offset that account for the header data
    children_offset_end = offset + 2
    values = {}
    if num_children:
        for i in range(0, num_children):
            children_offset_end, child_value = process_node(children_offset_end)
            values[i+1] = child_value


    # Sum each piece of the metadata. The metadata starts after the offset of the children.
    metadata_values = []
    for i in range(children_offset_end, children_offset_end + num_metadata):
        metadata_values.append(license[i])
    node_metadata_sum = sum(metadata_values)
    metadata_sum += node_metadata_sum

    # If a node has children, then its value is the sum of its children node's values at the index of this nodes metadata values
    value = 0
    if num_children:
        for metadata in metadata_values:
            value += values.get(metadata, 0)
    else:
    # If there are no children, then the value of the node is the sum of its metadata.
        value = node_metadata_sum

    return children_offset_end + num_metadata, value


_, value = process_node(0)

print('Part 1 - {} -  Metadata sum: {}, Answer: {}'.format('Success!' if metadata_sum == part_1_answer else 'Failure!', metadata_sum, part_1_answer))
print('Part 2 - {} -  Root value: {}, Answer: {}'.format('Success!' if value == part_2_answer else 'Failure!', value, part_2_answer))
