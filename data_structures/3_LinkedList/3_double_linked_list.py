class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Double linked list is empty")
            return
        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data) +' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print("link list in forward: ", dllstr)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Double linke list is empty")
            return
        
        last_node = self.get_last_node()
        itr = last_node
        dllstr = ''
        while itr:
            # dllstr += ' <-- ' + str(itr.data) if itr.prev else str(itr.data)
            dllstr += str(itr.data) +' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print("link list in reverse: ", dllstr)
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    
    # def print(self):
    #     if self.head is None:
    #         print("Linked list is empty")
    #         return
    #     itr = self.head
    #     llstr = ''
    #     while itr:
    #         llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
    #         itr = itr.next
    #     print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)
        # itr.prev = Node(itr.data, itr, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(count+1, data_to_insert)
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        # Remove first node that contains data
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(count)
                break
            itr = itr.next
            count += 1
            
            
if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_forward()
    ll.print_backward()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_forward()
    ll.print_backward()
    ll.remove_by_value("figs")
    ll.print_forward()
    ll.print_backward()