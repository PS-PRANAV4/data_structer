

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.ref = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_first(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    def traverse_linked_list(self):
        node = self.head
        while True:
            print(node.value)
            if node.ref == None:
                break
            node = node.ref
    def insert_at_end(self,value):
            node = Node(value)
            if self.head == None:
                self.head = node
            else:
                current_node = self.head
                while True:
                    if current_node.ref == None:
                        break
                    current_node = current_node.ref
                current_node.ref = node
    def insert_at_index(self,value,index):
        node = Node(value=value)
        position = 0
        if index == 0:
            self.insert_at_first(value=value)
        else:
            current_node = self.head
            while True:
                position += 1
                
                if position == index:
                    break
                current_node = current_node.ref
            node.ref = current_node.ref
            current_node.ref = node
    def update_node(self,value,index):
        position = 0
        node = self.head
        if index == 0:
            node.value = value
        else:
            while True:
                position += 1
                node = node.ref
                
                if position == index:
                    node.value = value
                    break
    def size_of_node(self):
        node = self.head
        size = 1
        while True:
            size += 1
            node = node.ref
            if node.ref == None:
                return size
    def remove_first_node(self):
        del_node = self.head
        self.head = self.head.ref
        del del_node
    def remove_last_node(self):
        node = self.head
        if self.head == None:
            print("no node in th linked list")
            return None
        else:
            last_node = node
            if last_node.ref == None:
                    self.head = None
                    del last_node
            curremt_node = node.ref
            size = 0
            
            while True:
                curremt_node = curremt_node.ref

                if curremt_node.ref == None:
                    
                    last_node.ref.ref = None
                    
                    del curremt_node
                    break
                
                last_node = last_node.ref
node = LinkedList()

node.insert_at_first(2)
node.insert_at_first(5)
node.insert_at_first(8)
node.insert_at_first(9)
node.insert_at_end(1)
node.insert_at_index(111,3)
node.update_node(100,2)
# node.remove_first_node()
node.remove_last_node()
node.traverse_linked_list()

print(node.size_of_node())

