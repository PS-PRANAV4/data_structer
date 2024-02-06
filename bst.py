class Node:
    def __init__(self,value) -> None:
        self.rref = None
        self.lref = None
        self.value = value
    def __str__(self) -> str:
        return f"{self.lref} {self.rref}  {self.value}"


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
    def inorder_traversel(self):
        self.inorder_traverse(self.root)

    def inorder_traverse(self,current_node):
        
        if current_node.lref != None:
            self.inorder_traverse(current_node.lref)
        print(current_node.value)
        if current_node.rref != None:
            self.inorder_traverse(current_node.rref)
    
    def pre_order_traversel(self):
        self.pre_order_traverse(self.root)

    def pre_order_traverse(self,current_node):
        print(current_node.value)
        if current_node.lref != None:
            self.pre_order_traverse(current_node.lref)
        
        if current_node.rref != None:
            self.pre_order_traverse(current_node.rref)
        
    def post_order(self):
        self.post_order_traverse(self.root)

    def post_order_traverse(self,current_node):
        
        if current_node.lref != None:
            self.post_order_traverse(current_node.lref)
        
        if current_node.rref != None:
            self.post_order_traverse(current_node.rref)
        print(current_node.value)

    def delete_a_node(self,data):
        self.process_delete_node(data,self.root)
    def process_delete_node(self,data,current_node):
        if not current_node:
            
            return current_node
        if current_node.value > data:
            current_node.lref = self.process_delete_node(data,current_node.lref)
        elif current_node.value < data:
            current_node.rref = self.process_delete_node(data,current_node.rref)
        else:
            if current_node.rref == None:
                return current_node.lref
            if current_node.lref == None:
                return current_node.rref
            curr = current_node.rref
            prev = current_node
            while curr.lref:
                prev = curr
                curr = curr.lref
            current_node.value = curr.value
            if prev == current_node:
                current_node.rref = None
            else:
                prev.lref = None

            # print(self.pre_order_traversel())
            # print(curr)
            # print(prev)
            # prev.lref = None
            # print(self.pre_order_traversel())
        return current_node
# bst_first = Bst(5)  
# bst_first.root.lref = Node(3)  
# bst_first.root.rref = Node(6) 
# bst_first.root.lref.lref = Node(2)  
# bst_first.root.lref.rref = Node(4) 
# bst_first.root.rref.rref = Node(7)  

bst_first = Bst(100)
# bst_first.adding_data_to_bst(8)
bst_first.adding_data_to_bst(20)
bst_first.adding_data_to_bst(200)
bst_first.adding_data_to_bst(10)
bst_first.adding_data_to_bst(30)
bst_first.adding_data_to_bst(150)
bst_first.adding_data_to_bst(300)
bst_first.adding_data_to_bst(12)
bst_first.adding_data_to_bst(4)
bst_first.inorder_traversel()
print()
# bst_first.pre_order_traversel()
# bst_first.inorder_traversel()
print()
# bst_first.post_order()
# print(preOrder(root))
result = bst_first.delete_a_node(300)
bst_first.inorder_traversel()
print("After deleting specified node:")
# bst_first.pre_order_traversel()
# print(preOrder(result))
# print(bst_first.root.value)
# print(bst_first.root.lref.value)
# print(bst_first.root.rref.value)
# print(bst_first.root.lref.lref.value)
# print(bst_first.root.rref.rref.value)
# print(bst_first.root.lref.lref.lref.value)
# print(bst_first.root.rref.rref.rref.value)
# print(bst_first.root.lref.lref.lref.lref.value)
# print(bst_first.root.rref.rref.rref.rref.value)
# print(bst_first.root.lref.lref.lref.lref.lref.value)
# print(bst_first.root.rref.rref.rref.rref.rref.value)