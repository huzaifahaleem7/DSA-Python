class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linklist:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            raise Exception("Linklist is empty")
            return
        itr = self.head
        lltr = ""
        while itr:
            lltr += str(itr.data) + " --> " if itr.next else str(itr.data)
            itr = itr.next
        print(lltr)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)

        itr = self.head
        while itr:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count = count + 1
            
    def insert_after_value(self, data_after, data_to_insert):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
    
    def remove_by_value(self, data):
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            
            
        
if __name__ == "__main__":
    ll = Linklist()
    ll.insert_at_begining(2)
    ll.insert_at_begining(4)
    ll.print()
    ll.insert_at(1, 6)
    ll.print()
    ll.insert_at(2, 29)
    ll.print()
    ll.insert_at(4, 40)
    ll.print()
    ll.remove_at(2)
    ll.print()
    ll.insert_after_value(2, 20)
    ll.insert_after_value(20, 30)
    ll.print()
    ll.remove_by_value(30)
    ll.print()
    ll.remove_by_value(4)
    ll.print()