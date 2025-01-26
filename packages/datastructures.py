class Linked_list:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None
 
    def __str__(self):
        return str(self.data)


# class Hash:
#     def __init__(self, length):
    #    self.__list = [] 


# class adjacent_list:
#     def __init__(self, length):
#         self.__list = []
#         for i in range(length):
#             self.__list.append(i)

#     def add(self, node):
#         pass


class Edge:
    def __init__(self, target, weight:int):
        self.target = target  
        self.weight = weight  
        self.next = None  

class Node:
    def __init__(self, code, type):
        self.code = code  # شناسه گره
        self.type = type  # نوع گره (خانه، بیمارستان، عادی)
        self.edges = None  # لیست یال‌های خروجی (به صورت linked list)
        if self.type == "hospital":
            self.ambulances = None

        


class Graph:
    def __init__(self):
        self.head = None

    def _get_node(self, code):
        current = self.head
        while current:
            if current.code == code:
                return current
            current = current.next
        return None
        
    def add_node(self, code, type):
        if self._get_node(code):
            print(f"Node {code} already exists!")
            return
        new_node = Node(code, type)
        new_node.next = self.head
        self.head = new_node

    def add_edge(self, from_code, to_code, weight:int):
        from_node = self._get_node(from_code)
        to_node = self._get_node(to_code)

        if not from_node or not to_node:
            print(f"\n(!) Error: Invalid node code(s): {from_code}, {to_code}\n")
            return
        dup_res = self.check_duplicate_edge( from_node, to_node)
        if dup_res:
            print(f"\n(!) Error: Attempt to create DUPLICATE edge: {from_code}, {to_code}\n")
            return
        else:
            new_edge = Edge(to_code, weight)
            if not from_node.edges:
                from_node.edges = new_edge
            else:
                current = from_node.edges
                while current.next:
                    current = current.next
                current.next = new_edge
            print("\n(*) Edge created Successfully*\n")

    def display_graph(self):
        current = self.head
        while current:
            print(f"code: {current.code} | type: {current.type}")
            edges = current.edges
            if not edges:
                print(f"\t*No edges*")
            while edges:
                print(f"\t==> {edges.target} (Weight = {edges.weight})")
                edges = edges.next
            print()
            current = current.next

    def check_duplicate_edge(self, from_node:Node, to_node:Node):
        to_node_code = to_node.code
        edges = from_node.edges
        while edges:
            if edges.target == to_node_code:
                return True
            edges = edges.next
        return False


class Ambulance:
    def __init__(self, location, hospital, code):
        self.hospital = hospital
        self.location = location
        self.code = code
        self.next = None



