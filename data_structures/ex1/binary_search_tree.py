class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass
  def breadth_first_for_each(self, cb):
    queue = [self]
    new_vals = []
    while queue:
      current_node = queue.pop()
      new_vals.append(cb(current_node.value))
      if current_node.left is not None:
        queue.append(current_node.left)
      if current_node.right is not None:
        queue.append(current_node.right)
    return new_vals


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

double = lambda x: x * 2

b1 = BinarySearchTree(5)
b1.insert(2)
b1.insert(7)
print(b1.value)
print(b1.left.value)
print(b1.right.value)
print(b1.breadth_first_for_each(double))  
