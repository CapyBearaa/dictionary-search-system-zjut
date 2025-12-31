class BSTNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BSTStorage:
    def __init__(self):
        self.root = None

    def add(self, item):
        if self.root is None:
            self.root = BSTNode(item)
            return True
        return self._add_recursive(self.root, item)

    def _add_recursive(self, node, item):
        if item.student_id == node.item.student_id:
            raise ValueError(f"ID {item.student_id} exists")
        if item.student_id < node.item.student_id:
            if node.left is None:
                node.left = BSTNode(item)
                return True
            return self._add_recursive(node.left, item)
        else:
            if node.right is None:
                node.right = BSTNode(item)
                return True
            return self._add_recursive(node.right, item)

    # --- NEW: BST DELETION ALGORITHM ---
    def delete(self, student_id):
        self.root = self._delete_recursive(self.root, student_id)

    def _delete_recursive(self, node, student_id):
        if not node: return None
        if student_id < node.item.student_id:
            node.left = self._delete_recursive(node.left, student_id)
        elif student_id > node.item.student_id:
            node.right = self._delete_recursive(node.right, student_id)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            temp = self._min_value_node(node.right)
            node.item = temp.item
            node.right = self._delete_recursive(node.right, temp.item.student_id)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left: current = current.left
        return current

    def search_by_id(self, student_id):
        return self._search_recursive(self.root, student_id)

    def _search_recursive(self, node, student_id):
        if not node or node.item.student_id == student_id:
            return node.item if node else None
        if student_id < node.item.student_id:
            return self._search_recursive(node.left, student_id)
        return self._search_recursive(node.right, student_id)

    def get_all(self):
        res = []
        self._inorder(self.root, res)
        return res

    def _inorder(self, node, res):
        if node:
            self._inorder(node.left, res)
            res.append(node.item)
            self._inorder(node.right, res)
            
    # Include search_by_name and search_by_group using _inorder traversal...

