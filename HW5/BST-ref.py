# Python3 program to implement basic operations  
# (search, insert and delete) on a BST that handles  
# duplicates by storing count with every node  
  
# A utility function to create a new BST node  
class newNode:  

    # Constructor to create a new node  
    def __init__(self, data):  
        self.key = data 
        self.count = 1
        self.left = None
        self.right = None

# A utility function to do inorder  
# traversal of BST  
def walk(root): 
    if root != None: 
        walk(root.left) 
        print(root.key,"(", root.count,")",  end = "\n")  
        walk(root.right) 

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
  
    # Otherwise, recur down the tree  
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
  
    # loop down to find the leftmost leaf  
    while current.left != None:  
        current = current.left  
  
    return current
  
# Given a binary search tree and a key,  
# this function deletes a given key and  
# returns root of modified tree  
def deleteNode(root, key): 
    
    # base case  
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
  
        # Delete the inorder successor  
        root.right = deleteNode(root.right, temp.key) 
    return root 

def Print(root):
    if not root:
        return
    print('Binary Search Word Tree:')
    #print(self.root)
    PrintInorder(root, 0,'Root-',17)

def PrintInorder(node, height, preString, length):
    if node.key == None:
        return
    PrintInorder(node.right, height + 1, 'R-', length)
    string = preString + str(node.key) + '('+ str(node.count) +')'
    leftLen = (length - len(string)) // 2
    rightLen = length - len(string) - leftLen
    res = " "*leftLen + string + ""*rightLen
    print(" "*height*length+res)
    PrintInorder(node.left, height+1, 'L-', length)

if __name__ == '__main__': 
    
    wordList = ['NIPS', 'NIPS','NIPS', 'EMNLP','NAACL','ICML','KDD','KDD','AAAI','ACL','ACL','ACL','ACL','ICCV','CVPR','SIGIR','IJCAI','CIKM','ICDE','WWW']
    root = None

    for i in wordList:
        root = insert(root, i)
    
    
    print("Inorder traversal of the given tree")  
    walk(root) 

     
    # deleteNode(root, 'NIPS')
    # print("Inorder traversal of the given tree") 
    # walk(root) 
    # deleteNode(root, 'NIPS')
    # print("Inorder traversal of the given tree") 
    # walk(root) 
    # deleteNode(root, 'NIPS')
    # print("Inorder traversal of the given tree") 
    # walk(root) 
    # deleteNode(root, 'WWW')
    # print("Inorder traversal of the given tree") 
    walk(root) 
    # Print(root)
    # deleteNode(root, 'ACL')
    # print("Inorder traversal of the given tree")  
    # walk(root)  

    # deleteNode(root, 'zq')
    # deleteNode(root, 'zq')
    # deleteNode(root, 'zq')
    # deleteNode(root, 'zq')
    # print("Inorder traversal of the given tree")  
    # walk(root)
    # print("Delete 20")  
    # root = deleteNode(root, 20)  
    # print("Inorder traversal of the modified tree")  
    # inorder(root)  
    # print() 
  
    # print("Delete 12") 
    # root = deleteNode(root, 12)  
    # print("Inorder traversal of the modified tree")  
    # inorder(root)  
    # print() 
  
    # print("Delete 9") 
    # root = deleteNode(root, 9)  
    # print("Inorder traversal of the modified tree")  
    # inorder(root) 
  
# This code is contributed by PranchalK 