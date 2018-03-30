class Node(object):

    def __init__(self,data):
        self.data = data;
        self.adjacencyList = [];
        self.visited = False;
        self.Predecessor = None;

class depthFirstSearch(object):

    def dfs(self, node):
        node.visited = True;
        print("%s" %node.data);

        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n);


dfs = depthFirstSearch()
node1 = Node("A");
node2 = Node("B");
node3 = Node("C");
node4 = Node("D");
node5 = Node("E");
node6 = Node("F");

node1.adjacencyList.append(node2);
node1.adjacencyList.append(node3);
node2.adjacencyList.append(node4);
node3.adjacencyList.append(node5);
node5.adjacencyList.append(node6);

dfs.dfs(node1)
        
