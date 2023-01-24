class INode:
    def __init__(self, idx):
        self.value = idx 
        self.next = None


class GNode:
    def __init__(self, idx):
        self.edges = None
        self.idx = idx
    
    def addEdge(self, idxDstNode):
        pI = INode(idxDstNode)
        head = self.edges
        if head == None:
            self.edges = pI
        elif head.next == None:
            if head.value < pI.value:
                pI.next = head
                head = pI
            elif head.value > pI.value:
                head.next = pI
        else:
            p_prev = head
            p_curr = head.next
            while p_curr:
                if p_curr.value > pI.value:
                    pI.next = p_curr
                    p_prev.next = pI 
                    break 
                p_prev = p_curr
                p_curr = p_curr.next

    def removeEdge(self, idxDstNode):
        head = self.edges
        if head == None:
            return 
        
        if head.value == idxDstNode:
            head = head.next
        else:
            p_prev = head 
            p_curr = head.next
            while p_curr:
                if p_curr.value == idxDstNode:
                    p_prev.next = p_curr.next
                    break
                p_prev = p_curr
                p_curr = p_curr.next
    
    def isEdgeExist(self, idxNode):
        head = self.edges
        if head == None:
            return False
        
        while head != None:
            if head.idx == idxNode:
                return True 
            head = head.next

        return False
