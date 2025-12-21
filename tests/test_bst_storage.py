class Node:
    def __init__(self, student_id, item):
        self.student_id = student_id
        self.item = item
        self.left = None
        self.right = None


class BSTStorage:
    def __init__(self):
        self.root = None

    def add(self, item):
        if self.root is None:
            self.root = Node(item.student_id, item)
            return

        current = self.root

        while True:
            if item.student_id < current.student_id:
                if current.left is None:
                    current.left = Node(item.student_id, item)
                    return
                else:
                    current = current.left

            elif item.student_id > current.student_id:
                if current.right is None:
                    current.right = Node(item.student_id, item)
                    return
                else:
                    current = current.right

            else:
                current.item = item
                return

    def search_by_id(self, student_id):
        current = self.root

        while current is not None:
            if student_id == current.student_id:
                return current.item
            elif student_id < current.student_id:
                current = current.left
            else:
                current = current.right

        return None

    def search_by_name(self, name):
        result = []
        self._walk(self.root, result, name, None)
        return result

    def search_by_group(self, group):
        result = []
        self._walk(self.root, result, None, group)
        return result

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

    def _walk(self, node, result, name, group):
        if node is None:
            return

        self._walk(node.left, result, name, group)

        if name is not None:
            if node.item.name == name:
                result.append(node.item)

        if group is not None:
            if node.item.group == group:
                result.append(node.item)

        self._walk(node.right, result, name, group)

