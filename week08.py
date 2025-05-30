class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def pre_order(node):
    if node is None:
        return
    print(f"{node.data}", end="->")
    post_order(node.left)
    post_order(node.right)

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(f"{node.data}", end="->")
    in_order(node.right)

def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(f"{node.data}", end="->")


node1 = TreeNode()
node1.data = 'hs'

node2 = TreeNode()
node2.data = 'sl'
node1.left = node2

node3 = TreeNode()
node3.data = 'mb'
node1.right = node3

node4 = TreeNode()
node4.data = 'hw'
node2.left = node4

node5 = TreeNode()
node5.data = 'zz'
node2.right = node5

node6 = TreeNode()
node6.data = 'sm'
node3.left = node6

print(node6.data)
print(node1.right.left.data)
pre_order(node1)
print()
in_order(node1)
print()
post_order(node1)
