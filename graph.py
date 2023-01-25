from node import *

class Graph:

    def __init__(self):
        self.nodes = []
    
    def addNode(self, nodeIdx) -> None:
        if self.isNodeExist(nodeIdx):
            return 
        else:
            self.nodes.append(GNode(nodeIdx))
    
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

    def isNodeExist(self, nodeIdx) -> bool:
        for gnode in self.nodes:
            if gnode.idx == nodeIdx:
                return True
        return False

    def printListNode(self) -> None:
        print("Number of node: ", len(self.nodes))
        for gnode in self.nodes:
            print("Node: ", gnode.idx)
    
    def printListEdge(self) -> None:
        print("Edge in graph: ")
        for gnode in self.nodes:
            head = gnode.lsOutDeg
            while head:
                print("Edge: {} -> {}".format(gnode.idx, head.value))
                head = head.next
    

# Directed Graph
class TNGraph(Graph):
    def __init__(self):
        super(TNGraph, self).__init__()
    
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



# Undirected graph
class TUNGraph(Graph):
    def __init__(self):
        super(TUNGraph, self).__init__()

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

            if gnode.idx == e_nodeIdx:
                gnode.addEdge(s_nodeIdx)
                
    def removeEdge(self, s_nodeIdx, e_nodeIdx) -> None:
        for gnode in self.nodes:
            if gnode.idx == s_nodeIdx:
                gnode.removeEdge(e_nodeIdx)

            if gnode.idx == e_nodeIdx:
                gnode.removeEdge(s_nodeIdx)

if __name__ == "__main__":
    
    # Create Directed Graph
    tngraph = TNGraph()
    tngraph.addNode(0)
    tngraph.addNode(1)
    tngraph.addNode(2)
    tngraph.addNode(3)
    tngraph.addNode(4)
    tngraph.addNode(5)


    tngraph.addEdge(0,1)
    tngraph.addEdge(0,5)
    tngraph.addEdge(1,2)
    tngraph.addEdge(2,3)
    tngraph.addEdge(3,4)
    tngraph.addEdge(3,5)
    tngraph.addEdge(4,0)
    tngraph.addEdge(5,4)
    tngraph.addEdge(5,2)

    tngraph.removeNode(0)
    tngraph.printListEdge()

    # Create Undirected graph
    tungraph = TUNGraph()
    tungraph.addNode(0)
    tungraph.addNode(1)
    tungraph.addNode(2)
    tungraph.addNode(3)
    tungraph.addNode(4)
    tungraph.addNode(5)

    tungraph.addEdge(0,1)
    tungraph.addEdge(1,2)
    tungraph.addEdge(2,3)
    tungraph.addEdge(3,4)
    tungraph.addEdge(4,5)
    tungraph.addEdge(5,0)
    tungraph.printListEdge()

