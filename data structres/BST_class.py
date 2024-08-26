class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

    
        
        
        
        '''if node == None:
            node = self.root
        
        elbow = "|_"
        line = "|"
        t_shape = "|--"
        blank = "   "


        print(header, (elbow if last else t_shape) + str(node.data))

        if node.left_child:
            value = node.left_child
            self.print_data(value, last=False if node.left_child else True, header=header + (blank if last else line))
        if node.right_child:
            value = node.right_child
            self.print_data(value, last=False if node.right_child else True, header=header+(blank if last else line))
'''
class BST(Node):
    def __init__(self, data):
        self.data = super().__init__(data)
        self.root = None
        self.count = 1

    def get_min(self, node):
        current = node
        while current.left_child is not None:
            current = current.left_child
        return current

    def get_depth(self, node):
        if node is None:
            return 0
        else:
            return max(self.get_depth(node.left_child), self.get_depth(node.right_child)) + 1
        
    def get_count(self):
        return self.count
    
    def push_recursively(self, node, value):
        if isinstance(value, Node):
            value = value.data

        if value < node.data:
            if node.left_child is None:
                node.left_child = Node(value)
            else:
                self.push_recursively(node.left_child, value)
        else:
            if node.right_child is None:
                node.right_child = Node(value)
            else:
                self.push_recursively(node.right_child, value)

    def push(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.push_recursively(node=self.root, value=value)
        self.count += 1

    def update(self, old_value, new_value):
        self.pop_recursively(self.root, old_value)
        self.push_recursively(self.root, new_value)

    def pop_recursively(self, node, value):
        if node is None:
            return node

        if value < node.data:
            node.left_child = self.pop_recursively(node.left_child, value)
        elif value > node.data:
            node.right_child = self.pop_recursively(node.right_child, value)
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child

            min_larger_node = self.get_min(node.right_child)
            node.data = min_larger_node.data
            node.right_child = self.pop_recursively(node.right_child, min_larger_node.data)
        
        return node

    def pop(self, value):
        self.pop_recursively(self.root, value)
        self.count -= 1


    def _depth(self, node):
        if node is None:
            return 0
        return 1 + max(self._depth(node.left_child), self._depth(node.right_child))

    def _print_level(self, nodes, level, max_level):
        if not nodes:
            return

        # Calculate spacing
        if level == max_level - 1:
            width = 3  # Minimal width for the last level
        else:
            width = (2 ** (max_level - level))
        width = max(width, 1)  # Ensure at least 1 space

        # Prepare the line to be printed
        line = ''
        next_nodes = []

        for node in nodes:
            if node:
                line += f'{node.data:^{width}}'
                next_nodes.extend([node.left_child, node.right_child])
            else:
                line += ' ' * (width)
                next_nodes.extend([None, None])

        print(line)
        # Continue if there are more nodes in the next level
        if any(next_nodes):
            self._print_level(next_nodes, level + 1, max_level)

    def print_tree(self):
        depth = self._depth(self.root)
        self._print_level([self.root], 0, depth)