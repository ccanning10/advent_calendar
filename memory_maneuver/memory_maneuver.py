from input import raw_licence, answer


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

    num_children = license[offset]
    num_metadata = license[offset + 1]

    # If we have children, process those children and fetch the end offset of the last child.
    # First, we have to add two to the offset that account for the header data
    children_offset_end = offset + 2
    if num_children:
        for i in xrange(0, num_children):
            children_offset_end = process_node(children_offset_end)

    # Sum each piece of the metadata. The metadata starts after the offset of the children.
    for i in range(children_offset_end, children_offset_end + num_metadata):
        metadata_sum += license[i]

    return children_offset_end + num_metadata

process_node(0)
print('{} - Metadata sum: {}, Answer: {}'.format('Success!' if metadata_sum == answer else 'Failure!', metadata_sum, answer))
