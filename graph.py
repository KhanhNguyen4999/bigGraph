from node import *
import copy

class Graph:

    def __init__(self, nodes={}):
        """
        node to list of neighbors in the graph by hashtable (dict/dictionary)
        """
        self.nodes = nodes
    
    def insert_node(self, nodeIdx) -> None:
        '''
        Insert a node with node index into the graph    
        '''
        if self.is_node_exist(nodeIdx):
            return 
        else:
            self.nodes[nodeIdx] = GNode(nodeIdx)
    
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
            for idx in self.nodes:
                if idx != nodeIdx:
                    gnode = self.nodes[idx]
                    if gnode.is_edge_exist(nodeIdx):
                        gnode.remove_edge(nodeIdx)
            
            # Step 2
            del self.nodes[nodeIdx]

    def remove_edge(self, s_nodeIdx, e_nodeIdx) -> None:
        raise NotImplementedError

    def get_sub_graph_by_node(self, ls_nodeIdx):
        """
        Get a subgraph by list of nodeIdx
        """
        # Get all nodes in list node idx from graph to construct subgraph
        nodes = {}
        for idx in self.nodes:
            if idx in ls_nodeIdx:
                nodes[idx] = copy.deepcopy(self.nodes[idx])

        subgraph = self.__class__(nodes)

        # Remove all edge point to node not in list node idx
        edges = subgraph.get_edges()
        for s_nodeIdx, e_nodeIdx in edges:
            if e_nodeIdx not in ls_nodeIdx:
                subgraph.remove_edge(s_nodeIdx, e_nodeIdx)

        return subgraph


    # def get_sub_graph_by_edge(self, s_nodeIdx, e_nodeIdx) -> None:
    #     raise NotImplementedError

    # def load_graph(self) -> None:
    #     None

    # def save_graph(self) -> None:
    #     None

    def show_graph(self) -> None:
        raise NotImplementedError

    def is_node_exist(self, nodeIdx) -> bool:
        """
        Check whether node exist in the graph or not
        """
        return nodeIdx in self.nodes

    def get_nodes(self) -> None:
        """
        Get all nodes in the graph
        """
        return list(self.nodes.values())
    
    def get_edges(self) -> None:
        """
        Get all edges in the graph
        """
        edges = []
        for nodeIdx in self.nodes:
            head = self.nodes[nodeIdx].lsOutDeg
            while head:
                edges.append((nodeIdx, head.value))
                head = head.next
        return edges
    

# Directed Graph
class TNGraph(Graph):
    def __init__(self, nodes={}):
        super(TNGraph, self).__init__(nodes) 
    
    def insert_edge(self, s_nodeIdx, e_nodeIdx) -> None:
        """
        Insert a new edge into directed graph: 
        params:
            - s_nodeIdx: edge start from
            - e_nodeIdx: node that edge pointer to
        The s_node will store e_node as new neighbor node
        """
        if self.is_node_exist(s_nodeIdx) and self.is_node_exist(e_nodeIdx):
            self.nodes[s_nodeIdx].insert_edge(e_nodeIdx)
    
    def remove_edge(self, s_nodeIdx, e_nodeIdx) -> None:
        """
        Remove edge from directed graph:
        params:
            - s_nodeIdx: edge start from
            - e_nodeIdx: node that edge pointer to
        Remove e_node from s_node's neighbor list
        """
        if self.is_node_exist(s_nodeIdx):
            self.nodes[s_nodeIdx].remove_edge(e_nodeIdx)

    def show_graph(self) -> None:
        ls_edges = self.get_edges()
        ls_edges = list(sorted(ls_edges))

        print("### List edge from directed graph ###")
        for edge in ls_edges:
            print("{} -> {}".format(edge[0], edge[1]))
        print("#####################################\n")



# Undirected graph
class TUNGraph(Graph):
    def __init__(self, nodes={}):
        super(TUNGraph, self).__init__(nodes)

    def insert_edge(self, s_nodeIdx, e_nodeIdx) -> None:
        """
        Insert a new edge into Undirected graph: 
        params:
            - s_nodeIdx: edge start from
            - e_nodeIdx: node that edge pointer to
        The s_node will store e_node as new neighbor node and vice versa
        """
        if self.is_node_exist(s_nodeIdx) and self.is_node_exist(e_nodeIdx):
            self.nodes[s_nodeIdx].insert_edge(e_nodeIdx)
            self.nodes[e_nodeIdx].insert_edge(s_nodeIdx)
                
    def remove_edge(self, s_nodeIdx, e_nodeIdx) -> None:
        """
        Remove edge from Undirected graph:
        params:
            - s_nodeIdx: edge start from
            - e_nodeIdx: node that edge pointer to
        Remove e_node from s_node's neighbor list and vice versa
        """
        if self.is_node_exist(s_nodeIdx):
            self.nodes[s_nodeIdx].remove_edge(e_nodeIdx)

        if self.is_node_exist(e_nodeIdx):
            self.nodes[e_nodeIdx].remove_edge(s_nodeIdx)

    def show_graph(self) -> None:
        ls_edges = self.get_edges()
        ls_edges = list(set(tuple(sorted(edge)) for edge in ls_edges))
        ls_edges = list(sorted(ls_edges))

        print("### List edge from undirected graph ###")
        for edge in ls_edges:
            print("{} - {}".format(edge[0], edge[1]))
        print("#######################################\n")

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
    tngraph.show_graph()

    subgraph = tngraph.get_sub_graph_by_node([0,1,2])
    subgraph.show_graph()

    # Create Undirected graph
    tungraph = TUNGraph()
    tungraph.insert_node('ppp')
    tungraph.insert_node('ade')
    tungraph.insert_node('xyz')
    tungraph.insert_node('ik')
    tungraph.insert_node('kiệt')
    tungraph.insert_node('no')

    tungraph.insert_edge('ppp','ade')
    tungraph.insert_edge('ade','xyz')
    tungraph.insert_edge('xyz','ik')
    tungraph.insert_edge('ik','kiệt')
    tungraph.insert_edge('kiệt','no')
    tungraph.insert_edge('no','ppp')

    tungraph.show_graph()

    tungraph = tungraph.get_sub_graph_by_node(['kiệt', 'no', 'ppp'])
    tungraph.show_graph()

