# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    # Greatest will be the current root which we start at
    node_greatest = root.value

    # Traverse the binary tree. If left child is present, go there.
    if root.left_child is not None:
        # Create a helper variable that calls greatest_node recursively, but using the left child.
        left_node = greatest_node(root.left_child)
        # Check if node_greatest(value) is > than child value
        if left_node > node_greatest:
            # If true, then change the root to the left child's value.
            node_greatest = left_node
    # If right child is present, go there.
    if root.right_child is not None:
        right_node = greatest_node(root.right_child)
        if right_node > node_greatest:
            node_greatest = right_node 

    return node_greatest

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(13)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))