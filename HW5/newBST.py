class newNode:  
    def __init__(self, data):  
        self.key = data
        self.count = 1
        self.left = None
        self.right = None
        self.type = None
 

def walk(root): 
    if root != None: 
        walk(root.left) 
        print(root.key,"(", root.count,")",  end = "\n")  
        walk(root.right) 



def insert(node, key):   
    if node == None: 
        k = newNode(key) 
        return k 
  
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

 
def minValueNode(node): 
    current = node  
  
    # loop down to find the leftmost leaf  
    while current.left != None:  
        current = current.left  
  
    return current

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

if __name__ == '__main__': 
    

    root = None
    root=insert(root,'NIPS')
    root=insert(root,'NIPS')
    root=insert(root,'NIPS')
    root=insert(root,'EMNLP')
    root=insert(root,'NAACL')
    root=insert(root,'ICML')
    root=insert(root,'KDD')
    root=insert(root,'KDD')
    root=insert(root,'AAAI')
    root=insert(root,'ACL')
    root=insert(root,'ACL')
    root=insert(root,'ACL')
    root=insert(root,'ACL')
    root=insert(root,'CVPR')
    root=insert(root,'ICCV')
    root=insert(root,'SIGIR')
    root=insert(root,'SIGIR')
    root=insert(root,'ICWSM')
    root=insert(root,'WWW')
    root=insert(root,'ICDE')
    root=insert(root,'CIKM')
    root=insert(root,'IJCAI') 
    
  
    print("Inorder traversal of the given tree")  
    walk(root)  
    print() 
    deleteNode(root, 'NIPS')
    print("Inorder traversal of the given tree") 
    walk(root) 
    deleteNode(root, 'NIPS')
    print("Inorder traversal of the given tree") 
    walk(root) 
    deleteNode(root, 'NIPS')
    print("Inorder traversal of the given tree") 
    walk(root) 
    deleteNode(root, 'WWW')
    print("Inorder traversal of the given tree") 
    walk(root) 
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