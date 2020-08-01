class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # planning
        # start at root and loop until self is None
        # if value <= self
        #  if self.left is None
        # insert our value
        # else
        # go left (update self to be self.left)
        # elif value > self
        # if self.right is None
        # insert our value
        # else
        # go right (update self to be self.right)
        cur_node = self
        while cur_node is not None:
            if value < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = BSTNode(value)
                else:
                    cur_node.left.insert(value)
            elif value >= cur_node.value:
                if cur_node.right is None:
                    cur_node.right = BSTNode(value)
                else:
                    cur_node.right.insert(value)
            return value

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # compare target value to cur value
        # 1. == return True
        # 2. < we go left
        # 3. > we go right
        # 4. if cant go left or right (not found, return false)
        cur_node = self
        if cur_node is not None:
            is_found = self._find(target, cur_node)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, target, cur_node):
        if target > cur_node.value and cur_node.right:
            return self._find(target, cur_node.right)
        elif target < cur_node.value and cur_node.left:
            return self._find(target, cur_node.left)
        if target == cur_node.value:
            return True

        # Return the maximum value found in the tree

    def get_max(self):
        # right most node will always be the biggest
        cur_node = self
        if cur_node is None:
            return None
        while cur_node.right is not None:
            cur_node = cur_node.right
        return cur_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursion method
        cur_node = self
        fn(cur_node.value)
        if cur_node.left is not None:
            cur_node.left.for_each(fn)
        if cur_node.right is not None:
            cur_node.right.for_each(fn)
