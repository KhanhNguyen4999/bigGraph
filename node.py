class INode:
    def __init__(self, idx):
        self.value = idx 
        self.next = None


class GNode:
    def __init__(self, idx):
        self.lsOutDeg = None
        self.idx = idx
    
    def addEdge(self, idxDstNode):
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

    def removeEdge(self, idxDstNode):
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
    
    def isEdgeExist(self, idxNode):
        head = self.lsOutDeg
        if head == None:
            return False
        
        while head != None:
            if head.value == idxNode:
                return True 
            head = head.next

        return False

    def __eq__(self, idxNode):
        return self.idx == idxNode
