# https://classroom.udacity.com/courses/ud513/lessons/7122604912/concepts/79198839630923

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current_node = self.root
        while True:
            if current_node.value > new_val:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(new_val)
                    break
            elif current_node.value < new_val:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(new_val)
                    break

    def search(self, find_val):
        current_node = self.root
        if current_node.value == find_val:
            return True
        while current_node.left or current_node.right:
            if current_node.value == find_val:
                return True
            elif current_node.value > find_val:
                current_node = current_node.left
            elif current_node.value < find_val:
                current_node = current_node.right
        return False

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print tree.root.left.value
print tree.root.left.left.value

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)