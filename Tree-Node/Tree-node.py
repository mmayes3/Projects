class TreeNode(object):
    def __init__(self, value):

        self.value = value
        self.left = None
        self.middle = None
        self.right = None

    def insert_node(self, new_value):

        if new_value < self.value:
            if self.left == None:
                self.left = TreeNode(new_value)
            else:
                self.left.insert_node(new_value)
        elif new_value == self.value:
            if self.middle == None:
                self.middle = TreeNode(new_value)
            else:
                self.middle.insert_node(new_value)
        else:  # case when new_value > self.value:
            if self.right == None:
                self.right = TreeNode(new_value)
            else:
                self.right.insert_node(new_value)

    def traverse_LMRW(self):
        if self.left != None:
            self.left.traverse_LMRW()
        if self.middle != None:
            self.middle.traverse_LMRW()
        if self.right != None:
            self.right.traverse_LMRW()
        print(self.value)


def ternary_tree(L):
    T = TreeNode(L[0])
    for value in L[1:]:
        T.insert_node(value)
    return T


def main():
    T = ternary_tree([4, 1, 2, 2, 3, 1, 0, 4, 6, 5, 6, 4])
    print("ternary tree")
    T.traverse_LMRW()


main()
