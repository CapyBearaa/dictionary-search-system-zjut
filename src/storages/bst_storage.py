# src/storages/bst_storage.py

class BSTNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class BSTStorage:
    """
    Binary Search Tree storage.
    Ordered by student_id.
    Average complexity:
    - add: O(log N)
    - search_by_id: O(log N)
    Worst case: O(N)
    """

    def __init__(self):
        self.root = None

    def add(self, item):
        if self.root is None:
            self.root = BSTNode(item)
            return True

        return self._add_recursive(self.root, item)

    def _add_recursive(self, node, item):
        if item.student_id == node.item.student_id:
            raise ValueError(f"Item with id={item.student_id} already exists")

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

    def search_by_id(self, student_id):
        return self._search_recursive(self.root, student_id)

    def _search_recursive(self, node, student_id):
        if node is None:
            return None

        if student_id == node.item.student_id:
            return node.item

        if student_id < node.item.student_id:
            return self._search_recursive(node.left, student_id)
        else:
            return self._search_recursive(node.right, student_id)

    def search_by_name(self, name):
        result = []
        self._inorder_search_name(self.root, name, result)
        return result

    def _inorder_search_name(self, node, name, result):
        if node is None:
            return
        self._inorder_search_name(node.left, name, result)
        if node.item.name == name:
            result.append(node.item)
        self._inorder_search_name(node.right, name, result)

    def search_by_group(self, group):
        result = []
        self._inorder_search_group(self.root, group, result)
        return result

    def _inorder_search_group(self, node, group, result):
        if node is None:
            return
        self._inorder_search_group(node.left, group, result)
        if node.item.group == group:
            result.append(node.item)
        self._inorder_search_group(node.right, group, result)

    def get_all(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.item)
        self._inorder(node.right, result)

