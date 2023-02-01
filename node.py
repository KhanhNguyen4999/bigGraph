class INode:
    def __init__(self, idx):
        self.value = idx 
        self.next = None


class GNode:
    """
    Class structure store information of internal node in the graph include:
    - Node index
    - List of edge start from that node
    
    (Graph will become network if it comes with data)
    """
    def __init__(self, idx):
        self.lsOutDeg = None
        self.idx = idx
    
    def insert_edge(self, idxDstNode):
        """
        Inserting new edge actually save dstNode as new neighbor
        params:
            - idxDstNode: destination node
        """
        pI = INode(idxDstNode)
        if self.lsOutDeg == None:
            self.lsOutDeg = pI
        elif self.lsOutDeg.next == None:
            if self.lsOutDeg.value > pI.value:
                pI.next = self.lsOutDeg
                self.lsOutDeg = pI
            elif self.lsOutDeg.value < pI.value:
                self.lsOutDeg.next = pI
        else:
            p_prev = self.lsOutDeg
            p_curr = p_prev.next
            while p_curr:
                if p_curr.value > pI.value:
                    pI.next = p_curr
                    p_prev.next = pI 
                    break 
                p_prev = p_curr
                p_curr = p_curr.next

    def remove_edge(self, idxDstNode):
        """
        Removing edge actually delete destination node's idx from list neighbor
        params:
            - idxDstNode: destination node
        """
        if self.lsOutDeg == None:
            return 
        
        if self.lsOutDeg.value == idxDstNode:
            self.lsOutDeg = self.lsOutDeg.next
        else:
            p_prev = self.lsOutDeg 
            p_curr = p_prev.next
            while p_curr:
                if p_curr.value == idxDstNode:
                    p_prev.next = p_curr.next
                    break
                p_prev = p_curr
                p_curr = p_curr.next
    
    def is_edge_exist(self, idxNode):
        """
        Check whether idxNode is the neighbor or not
        """
        head = self.lsOutDeg
        if head == None:
            return False
        
        while head != None:
            if head.value == idxNode:
                return True 
            head = head.next

        return False

    def __eq__(self, other):
        return self.idx == other.idx
