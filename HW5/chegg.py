def _init_(self, data):
    self.key = data
    self.count = 1
    self.left = None
    self.right = None


# traversal of BST

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.key,"(", root.count,")",end = " ")
        inorder(root.right)

# A utility function to insert a new node

# with given key in BST


def insert(node, key):
    # If the tree is empty, return a new node
    if node == None:
        k = newNode(key)
        return k
    # If key already exists in BST, increment

    # count and return
    if key == node.key:
        (node.count) += 1
        return node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    
    # return the (unchanged) node pointer
    return node

# Given a non-empty binary search tree, return
# the node with minimum key value found in that
# tree. Note that the entire tree does not need
# to be searched.

def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current

# Given a binary search tree and a key,
# this function deletes a given key and
# returns root of modified tree

def deleteNode(root, key):
    if root == None:
        return root
    # If the key to be deleted is smaller than the
    # root's key, then it lies in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
    # If the key to be deleted is greater than
    # the root's key, then it lies in right subtree
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    # if key is same as root's key
    else:
        # If key is present more than once,
        # simply decrement count and return
        if root.count > 1:
            root.count -= 1
            return root
        # ElSE, delete the node node with
        # only one child or no child
        if root.left == None:
            temp = root.right
            return temp
        elif root.right == None:
            temp = root.left
            return temp
    # node with two children: Get the inorder
    # successor (smallest in the right subtree)
    temp = minValueNode(root.right)
    # Copy the inorder successor's content
    # to this node
    root.key = temp.key
    root.count = temp.count
    # Delete the inorder successor
    root.right = deleteNode(root.right, temp.key)
    return root

# Driver Code



if _name_ == '_main_':
    root = None
    root = insert(root, 12)
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 9)
    root = insert(root, 11)
    root = insert(root, 10)
    root = insert(root, 12)
    root = insert(root, 12)
    print("Inorder traversal of the given tree")
    inorder(root)
    print()

# Let us create following BST

# 12(3)

# / \

# 10(2) 20(1)

# / \

# 9(1) 11(1)



  

print("Delete 20")

root = deleteNode(root, 20)

print("Inorder traversal of the modified tree")

inorder(root)

print()

print("Delete 12")

root = deleteNode(root, 12)

print("Inorder traversal of the modified tree")

inorder(root)

print()

print("Delete 9")

root = deleteNode(root, 9)

print("Inorder traversal of the modified tree")

inorder(root)

