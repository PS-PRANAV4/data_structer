class Node:
    def __init__(self,value) -> None:
        self.rref = None
        self.lref = None
        self.value = value


class Bst:
    def __init__(self,value) -> None:
        self.root = Node(value=value)
    

    def adding_data_to_bst(self,data):
        current_node = self.root
        self.adding_data(data=data,current_node=current_node)
    def adding_data(self,data,current_node):
        if current_node.value > data:
            if current_node.lref == None:
                current_node.lref = Node(value=data)
                return True
            else:
                current_node = current_node.lref
                self.adding_data(current_node=current_node,data=data)

        elif current_node.value < data:
            if current_node.rref == None:
                current_node.rref = Node(value=data)
                return True
            else:
                current_node = current_node.rref
                self.adding_data(data=data,current_node=current_node)    


bst_first = Bst(8)
# bst_first.adding_data_to_bst(8)
bst_first.adding_data_to_bst(9)
bst_first.adding_data_to_bst(7)
bst_first.adding_data_to_bst(10)
bst_first.adding_data_to_bst(6)
bst_first.adding_data_to_bst(11)
bst_first.adding_data_to_bst(5)
bst_first.adding_data_to_bst(12)
bst_first.adding_data_to_bst(4)
print(bst_first.root.value)
print(bst_first.root.lref.value)
print(bst_first.root.rref.value)
print(bst_first.root.lref.lref.value)
print(bst_first.root.rref.rref.value)
print(bst_first.root.lref.lref.lref.value)
print(bst_first.root.rref.rref.rref.value)
print(bst_first.root.lref.lref.lref.lref.value)
print(bst_first.root.rref.rref.rref.rref.value)
# print(bst_first.root.lref.lref.lref.lref.lref.value)
# print(bst_first.root.rref.rref.rref.rref.rref.value)