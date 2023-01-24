from node import *

class Graph:

    def __init__(self):
        self.edges = []
        self.nodes = []
    
    def addNode(self, nodeIdx) -> None:
        raise NotImplementedError
    
    def addEgde(self, s_nodeIdx, e_nodeIdx) -> None:
        raise NotImplementedError

    def removeNode(self, nodeIdx) -> None:
        raise NotImplementedError

    def removeEdge(self, s_nodeIdx, e_nodeIdx) -> None:
        raise NotImplementedError

    # def getSubGraphByNode(self, nodeIdx) -> None:
    #     raise NotImplementedError

    # def getSubGraphByEdge(self, s_nodeIdx, e_nodeIdx) -> None:
    #     raise NotImplementedError

    # def loadGraph(self) -> None:
    #     None

    # def saveGraph(self) -> None:
    #     None
    

# Directed Graph
class TNGraph(Graph):
    def __init__(self):
        super(TNGraph, self).__init__()
    
    def isNodeExist(self, nodeIdx) -> bool:
        for gnode in self.nodes:
            if gnode.idx == nodeIdx:
                return True
        return False

    def addNode(self, nodeIdx) -> None:
        if self.isNodeExist(nodeIdx):
            return 
        else:
            self.nodes.append(GNode(nodeIdx))
    
    def removeNode(self, nodeIdx) -> None:
        # Remove all edge direction to nodeId
        if self.isNodeExist(nodeIdx):
            for gnode in self.nodes:
                if gnode.idx != nodeIdx:
                    if gnode.isEdgeExist(nodeIdx):
                        gnode.removeEdge(nodeIdx)
            
            # Remove all edge dicrection start from nodeId
            for i, gnode in enumerate(self.nodes):
                if gnode.idx == nodeIdx:
                    self.nodes.remove(i)
                    break 
    
    def addEdge(self, s_nodeIdx, e_nodeIdx) -> None:
        for gnode in self.nodes:
            if gnode.idx == s_nodeIdx:
                gnode.addEdge(e_nodeIdx)
                break 
    
    def removeEdge(self, s_nodeIdx, e_nodeIdx) -> None:
        for gnode in self.nodes:
            if gnode.idx == s_nodeIdx:
                gnode.removeEdge(e_nodeIdx)
                break 

    def printListNode(self) -> None:
        print("Number of node: ", len(self.nodes))
        for gnode in self.nodes:
            print("Node: ", gnode.idx)
    
    def printListEdge(self) -> None:
        print("Edge in directed graph: ")
        for gnode in self.nodes:
            head = gnode.edges
            while head:
                print("Edge: {} -> {}".format(gnode.idx, head.value))
                head = head.next



        


# Undirected graph
# class TUNGraph(Graph):
#     def __init__(self):
#         super.__init__(TUNGraph, self)

if __name__ == "__main__":
    
    graph = TNGraph()
    graph.addNode(1)
    graph.addNode(2)
    graph.addNode(3)

    graph.addEdge(1,2)
    graph.addEdge(2,3)
    graph.addEdge(2,3)

    graph.printListNode()
    graph.printListEdge()



