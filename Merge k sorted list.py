class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import Queue
        p = Queue.PriorityQueue()
        out = root = ListNode(0)
        for i in range(len(lists)):
            if lists[i]: p.put((lists[i].val,lists[i]))  
        while(p.qsize()>0):
            ad = p.get()[1] 
            out.next = ListNode(ad.val) 
            out = out.next
            if ad.next: p.put((ad.next.val,ad.next))  
        return root.next
