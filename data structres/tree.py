class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def addNode(self, child):
        self.children.append(child)

def pre_order_traversal(node):
    if node == None:
        return None
    print(node.data)
    for child in node.children:
        pre_order_traversal(child)

def depth_first_search(node, target):
    if node == None:
        return False
    elif node.data == target:
        return True
    for child in node.children:
        if depth_first_search(child, target):
            return True
    return False

def insert(root, value):
    if root == None:
        root = value
    else:
        root.addNode(value)

def delete(root, target):
    if root == None:
        return None
    root.children = [child for child in root.children if child.data != target]
    for child in root.children:
        delete(child, target)

def tree_height(node):
    if node == None:
        return 0
    elif not node.children:
        return 1
    return 1 + max(tree_height(child) for child in node.children)

def print_data(node):
    print(node.data)
    if node.children:
        for child in node.children:
            print_data(child)


class AVL_tree(TreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.height = 1

    def balance_factor(self):
        left_height = self.children[0].height if self.children and len(self.children) > 0 else 0
        right_height = self.children[1].height if self.children and len(self.children) > 1 else 0
        return left_height - right_height
    
    def update_height(self):
        left_height = self.children[0].height if self.children and len(self.children) > 0 else 0
        right_height = self.children[1].height if self.children and len(self.children) > 1 else 0
        self.height = 1 + max(left_height, right_height)

    def rotate_left(self):
        new_root = self.children[1]
        self.children[1] = new_root.children[0]
        new_root.children[0] = self
        self.update_height()
        new_root.update_height()
        return new_root
    
    def rotate_right(self):
        new_root = self.children[0]
        self.children[0] = new_root.children[1]
        new_root.children[1] = self
        self.update_height()
        new_root.update_height()
        return new_root
    

root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
child3 = TreeNode("D")

root.addNode(child1)
root.addNode(child2)
root.addNode(child3)

# Traversal example (pre-order)
print("Pre-order traversal:")
pre_order_traversal(root)

# Searching example
target_value = "D"
print(f"Is {target_value} present in the tree? {depth_first_search(root, target_value)}")

# Insertion example
new_node = TreeNode("E")
insert(child1, new_node)
print("After insertion:")
pre_order_traversal(root)

# Deletion example
delete(root, "C")
print("After deletion:")
pre_order_traversal(root)

# Height calculation example
print("Height of the tree:", tree_height(root))

# AVL tree example (basic concept)
avl_root = AVL_tree("M")
avl_child1 = AVL_tree("L")
avl_child2 = AVL_tree("R")

avl_root.addNode(avl_child1)
avl_root.addNode(avl_child2)

avl_child1.addNode(AVL_tree("A"))
avl_child1.addNode(AVL_tree("B"))

avl_child2.addNode(AVL_tree("X"))

avl_root = avl_root.rotate_left()
print("After rotation (left):")
pre_order_traversal(avl_root)

avl_root = avl_root.rotate_right()
print("After rotation (right):")
pre_order_traversal(avl_root)