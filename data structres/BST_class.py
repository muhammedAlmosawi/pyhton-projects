class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class BST(Node):
    def __init__(self, data):
        super().__init__(data)
        self.root = None
        self.count = 1

    def push_recursively(self, node, value):
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

    def push(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.push_recursively(self.root, value)
        self.count += 1

    def update(self, old_value, new_value):
        self.pop_recursively(self.root, old_value)
        self.push_recursively(self.root, new_value)

    def pop(self, value):
        self.pop_recursively(self.root, value)
        self.count -= 1
    
    def print_data(self, root, last=False, header=""):
        elbow = "|_"
        line = "| "
        t_shape = "|--"
        blank = "\t"

        print(header, (elbow if last else t_shape) + str(root.data))
        if last:
            return ""
        value = root.left_child
        self.print_data(value, last = False if root.left_child else True, header=header + (blank if last else line))
        value = root.right_child
        self.print_data(value, last=False if root.right_child else True, header=header+(blank if last else line))


        '''if self.root is None:
            return

        depth = self.get_depth(self.root)
        max_width = 2 ** depth - 1  

        current_level = [self.root]
        level = 0

        
        while current_level != None:
            next_level = []
            current_level = next_level
            level += 1


            line = ""
            connection_line = ""

            space_between_nodes = max_width // (2 ** level) if level > 0 else max_width

            for i, node in enumerate(current_level):
                if node is not None:
                    line += f"{node.data}".center(space_between_nodes)
                    next_level.append(node.left_child)
                    next_level.append(node.right_child)
                else:
                    line += " " * space_between_nodes
                    next_level.append(None)
                    next_level.append(None)

                if i < len(current_level) - 1:
                    connection_line += " " * (space_between_nodes // 2)
                    connection_line += "|" + " " * (space_between_nodes // 2)

            print(line.rstrip())
            if any(child is not None for child in next_level):
                print(connection_line.rstrip())'''
        
        