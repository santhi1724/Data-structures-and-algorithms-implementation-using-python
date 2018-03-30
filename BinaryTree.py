class Node(object):

    def __init__(self,data):
        self.data = data;
        self.leftChild = None;
        self.rightChild = None;

class binarySearchTree(object):

    def __init__(self):
        self.root = None;

    def insert(self,data):
        if not self.root:
            self.root = Node(data);
        else:
            self.insertNode(data,self.root);

    def insertNode(self,data,node):

        if data < node.data:
            if node.leftChild:
                self.insertNode(data,node.leftChild);
            else:
                node.leftChild = Node(data);
        else:
            if node.rightChild:
                self.insertNode(data,node.rightChild);
            else:
                node.rightChild = Node(data);
                
    
    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root);
            
    def removeNode(self,data, node):
        if not node:
            return node;
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild);
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild);
        else:
            if not node.leftChild and not node.rightChild:
                print("removing a leaf node...");
                del node;
                return None;
            if not node.leftChild:
                print("removing a node with single right child...");
                tempNode = node.rightChild;
                del node;
                return tempNode;
            elif not node.rightChild:
                print("removing a node with single left child..");
                tempNode = node.leftChild;
                del node;
                return tempNode;
            print("Removing node with two children..");
            tempNode = self.getPredeccor(node.leftChild);
            node.data = tempNode.data;
            node.leftChild = self.removeNode(tempNode.data, node.leftChild);                 
        return node;
    def getPredeccor(self,node):
        
        if node.rightChild:
            return self.getPredeccor(node.rightChild);
        
        return node;
    
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root);
        
    def getMin(self,node):
        if node.leftChild:
            return self.getMin(node.leftChild);
        return node.data;
    
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root);

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild);
        return node.data;

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root);

    def traverseInorder(self, node):
        if node.leftChild:
            self.traverseInorder(node.leftChild);
        print("%s" % node.data);

        if node.rightChild:
            self.traverseInorder(node.rightChild);
        
bst = binarySearchTree();
bst.insert(10);
bst.insert(13);
bst.insert(5);
bst.insert(15);
bst.remove(10);


bst.traverse();


        
            
            
