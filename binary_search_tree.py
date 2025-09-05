class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, value):
        if value == self.data:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def calculate_sum(self):
        sum = self.data
        if self.left:
            sum += self.left.calculate_sum()
        if self.right:
            sum += self.right.calculate_sum()
        
        return sum
    
    def in_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def pre_order_traversal(self):
        elememts = []
        elememts.append(self.data)
        
        if self.left:
            elememts += self.left.pre_order_traversal()
        
        if self.right:
            elememts +=  self.right.pre_order_traversal()
            
        return elememts
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)
        return elements
    
        
def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root

if __name__ == "__main__":
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print(numbers_tree.search(20))
    print(numbers_tree.search(100))
    print("Min:", numbers_tree.find_min())
    print("Max:", numbers_tree.find_max())
    sum = numbers_tree.calculate_sum()
    print("Sum:", sum)
    print("In-order Traversal:", numbers_tree.in_order_traversal())
    print("Pre-order Traversal:", numbers_tree.pre_order_traversal())
    print("Post-order Traversal:", numbers_tree.post_order_traversal())
    