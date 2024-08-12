class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.count = 1

    def addNode(self, child):
        self.children.append(child)
        self.count += 1

    def pre_order_traversal(self, node):
        if node.data == None:
            return None
        print(node.data)
        for child in node.children:
            self.pre_order_traversal(child)

    def depth_first_search(self, node, target):
        if node == None:
            return False
        elif node.data == target:
            return True
        for child in node.children:
            if self.depth_first_search(child, target):
                return True
        return False

    def insert(target_node, value):
        if target_node == None:
            target_node = value
        else:
            target_node.addNode(value)

    def delete(self, target_node, target):
        if target_node == None:
            return None
        target_node.children = [child for child in target_node.children if child.data != target]
        self.count -= 1
        for child in target_node.children:
            self.delete(child, target)

    def tree_height(self, node):
        if node == None:
            return 0
        elif not node.children:
            return 1
        return 1 + max(self.tree_height(child) for child in node.children)

    def print_data(self):
        print(self.data)
        if self.children:
            for child in self.children:
                self.print_data(child)



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

print("Pre-order traversal:")
root.pre_order_traversal(node=root)

target_value = "D"
print(f"Is {target_value} present in the tree? {root.depth_first_search(root, target_value)}")

new_node = TreeNode("E")
TreeNode.insert(child1, new_node)
print("After insertion:")
root.pre_order_traversal(root)

root.delete(root, "C")
print("After deletion:")
root.pre_order_traversal(root)

print("Height of the tree:", root.tree_height(root))

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
root.pre_order_traversal(avl_root)

avl_root = avl_root.rotate_right()
print("After rotation (right):")
root.pre_order_traversal(avl_root)