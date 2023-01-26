from node import *

class Graph:

    def __init__(self):
        """
        node to list of neighbors in the graph by hashtable (dict/dictionary)
        """
        self.nodes = []
    
    def insert_node(self, nodeIdx) -> None:
        '''
        Insert a node with node index into the graph    
        '''
        if self.is_node_exist(nodeIdx):
            return 
        else:
            self.nodes.append(GNode(nodeIdx))
    
    def insert_egde(self, s_nodeIdx, e_nodeIdx) -> None:
        raise NotImplementedError

    def remove_node(self, nodeIdx) -> None:
        """
        Remove node in big graph includes 2 steps:
        - Remove all edges pointer to that Node
        - Remove all edges start from that Node
        """
        if self.is_node_exist(nodeIdx):
            # Step 1
            for gnode in self.nodes:
                if gnode.idx != nodeIdx:
                    if gnode.is_edge_exist(nodeIdx):
                        gnode.remove_edge(nodeIdx)
            
            # Step 2
            for i, gnode in enumerate(self.nodes):
                if gnode.idx == nodeIdx:
                    self.nodes.remove(i)
                    break 

    def remove_edge(self, s_nodeIdx, e_nodeIdx) -> None:
        raise NotImplementedError

    # def getSubGraphByNode(self, nodeIdx) -> None:
    #     raise NotImplementedError

    # def getSubGraphByEdge(self, s_nodeIdx, e_nodeIdx) -> None:
    #     raise NotImplementedError

    # def loadGraph(self) -> None:
    #     None

    # def saveGraph(self) -> None:
    #     None

    def is_node_exist(self, nodeIdx) -> bool:
        """
        Check whether node exist in the graph or not
        """
        for gnode in self.nodes:
            if gnode.idx == nodeIdx:
                return True
        return False

    def nodes(self) -> None:
        """
        Get all nodes in the graph
        """
        nodes = []
        for gnode in self.nodes:
            nodes.append(gnode.idx)
        return nodes
    
    def edges(self) -> None:
        """
        Get all edges in the graph
        """
        edges = []
        for gnode in self.nodes:
            head = gnode.lsOutDeg
            while head:
                edges.append((gnode.idx, head.value))
                head = head.next
        return edges
    

# Directed Graph
class TNGraph(Graph):
    def __init__(self):
        super(TNGraph, self).__init__()
    
    def insert_edge(self, s_nodeIdx, e_nodeIdx) -> None:
        """
        Insert a new edge into directed graph: 
        params:
            - s_nodeIdx: edge start from
            - e_nodeIdx: node that edge pointer to
        The s_node will store e_node as new neighbor node
        """
        for gnode in self.nodes:
            if gnode.idx == s_nodeIdx:
                gnode.insert_edge(e_nodeIdx)
                break 
    
    def remove_edge(self, s_nodeIdx, e_nodeIdx) -> None:
        """
        Remove edge from directed graph:
        params:
            - s_nodeIdx: edge start from
            - e_nodeIdx: node that edge pointer to
        Remove e_node from s_node's neighbor list
        """
        for gnode in self.nodes:
            if gnode.idx == s_nodeIdx:
                gnode.remove_edge(e_nodeIdx)
                break 


# Undirected graph
class TUNGraph(Graph):
    def __init__(self):
        super(TUNGraph, self).__init__()

    def insert_edge(self, s_nodeIdx, e_nodeIdx) -> None:
        """
        Insert a new edge into Undirected graph: 
        params:
            - s_nodeIdx: edge start from
            - e_nodeIdx: node that edge pointer to
        The s_node will store e_node as new neighbor node and vice versa
        """
        for gnode in self.nodes:
            if gnode.idx == s_nodeIdx:
                gnode.insert_edge(e_nodeIdx)

            if gnode.idx == e_nodeIdx:
                gnode.insert_edge(s_nodeIdx)
                
    def remove_edge(self, s_nodeIdx, e_nodeIdx) -> None:
        """
        Remove edge from Undirected graph:
        params:
            - s_nodeIdx: edge start from
            - e_nodeIdx: node that edge pointer to
        Remove e_node from s_node's neighbor list and vice versa
        """
        for gnode in self.nodes:
            if gnode.idx == s_nodeIdx:
                gnode.remove_edge(e_nodeIdx)

            if gnode.idx == e_nodeIdx:
                gnode.remove_edge(s_nodeIdx)

if __name__ == "__main__":
    
    # Create Directed Graph
    tngraph = TNGraph()
    tngraph.insert_node(0)
    tngraph.insert_node(1)
    tngraph.insert_node(2)
    tngraph.insert_node(3)
    tngraph.insert_node(4)
    tngraph.insert_node(5)


    tngraph.insert_edge(0,1)
    tngraph.insert_edge(0,5)
    tngraph.insert_edge(1,2)
    tngraph.insert_edge(2,3)
    tngraph.insert_edge(3,4)
    tngraph.insert_edge(3,5)
    tngraph.insert_edge(4,0)
    tngraph.insert_edge(5,4)
    tngraph.insert_edge(5,2)

    tngraph.remove_node(0)
    ls_edges = tngraph.edges()
    print("List edge from directed graph")
    for edge in ls_edges:
        print("{} -> {}".format(edge[0], edge[1]))

    # Create Undirected graph
    tungraph = TUNGraph()
    tungraph.insert_node(0)
    tungraph.insert_node(1)
    tungraph.insert_node(2)
    tungraph.insert_node(3)
    tungraph.insert_node(4)
    tungraph.insert_node(5)

    tungraph.insert_edge(0,1)
    tungraph.insert_edge(1,2)
    tungraph.insert_edge(2,3)
    tungraph.insert_edge(3,4)
    tungraph.insert_edge(4,5)
    tungraph.insert_edge(5,0)
    ls_edges = tungraph.edges()
    print("List edge from undirected graph")
    for edge in ls_edges:
        print("{} -> {}".format(edge[0], edge[1]))
