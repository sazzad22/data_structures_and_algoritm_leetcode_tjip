# TC : O(N)
# SC : O(1)


class ListNode:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val}, {self.next}"

class MyLinkedList:

    def __init__(self):
        self.n : int = 0
        self.d_head = ListNode(0)

    def get(self, index: int) -> int:
        # start from the node after dummy head i.e d_head
        if self.n <= index or index < 0:
            return -1
        curr = self.d_head.next
        # jump to the index
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        # self.addAtIndex(0,val)
        curr = ListNode(val,self.d_head.next)
        self.d_head.next = curr
        self.n += 1
        # print("add at head",self.d_head)
        print('length',self.n)

    def addAtTail(self, val: int) -> None:
        # self.addAtIndex(self.n,val)
        curr = self.d_head
        while curr.next != None:
            curr  = curr.next
        curr.next = ListNode(val,None)
        self.n += 1
        # print("add at tail",self.d_head)
        print('length',self.n)
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index < 0 or index > self.n:
            return 
        # start
        curr = self.d_head
        # jumping ,stoping jump if I reach the index before the given index
        for _ in range(index):
            curr =curr.next
        # create new node
        new_node = ListNode(val,curr.next)
        
        curr.next = new_node
        
        self.n+= 1
        # print("add at index",self.d_head)
        print('length',self.n,'given index',index)


    def deleteAtIndex(self, index: int) -> None:
        if self.n <= index or index < 0: 
            return
        curr = self.d_head
        # print("before delete",self.d_head)
        # print('length',self.n,'given index',index)
        for _ in range(index):
            curr = curr.next
           
        curr.next = curr.next.next
        self.n -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)