from packages.functions import floyd_warshall

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
    
    def to_adjacency_matrix(self):
        """
        Converts the graph into an adjacency matrix representation using linked lists.
        Returns:
            tuple: (matrix_head, nodes_head) where matrix_head is a linked list of linked lists,
                   and nodes_head is a linked list of node codes.
        """
        # Gather all nodes into a linked list
        nodes_head = None
        current = self.head
        while current:
            new_node = Linked_list(current.code)
            new_node.next = nodes_head
            nodes_head = new_node
            current = current.next

        # Count the nodes
        current = nodes_head
        num_nodes = 0
        while current:
            num_nodes += 1
            current = current.next

        # Create a linked list of linked lists for the matrix
        matrix_head = None
        for _ in range(num_nodes):
            row_head = None
            for _ in range(num_nodes):
                new_cell = Linked_list(float('inf'))
                new_cell.next = row_head
                row_head = new_cell
            new_row = Linked_list(row_head)
            new_row.next = matrix_head
            matrix_head = new_row

        # Set diagonal to 0 (distance to itself is 0)
        row = matrix_head
        row_index = 0
        while row:
            col = row.data
            col_index = 0
            while col:
                if row_index == col_index:
                    col.data = 0
                col = col.next
                col_index += 1
            row = row.next
            row_index += 1

        # Fill the adjacency matrix with edge weights
        node_map = {}
        current = nodes_head
        index = 0
        while current:
            node_map[current.data] = index
            current = current.next
            index += 1

        current = self.head
        while current:
            edge = current.edges
            while edge:
                from_index = node_map[current.code]
                to_index = node_map[edge.target]

                row = matrix_head
                for _ in range(from_index):
                    row = row.next

                col = row.data
                for _ in range(to_index):
                    col = col.next

                col.data = edge.weight
                edge = edge.next
            current = current.next

        return matrix_head, nodes_head


    def house_request_ambulance(self, house_code, ambulances):
        """
        Handles a house's request for an ambulance by finding the closest one.

        Args:
            house_code (str): The code of the house requesting an ambulance.
            ambulances (LinkedListNode): Linked list of ambulances, where each
                                        data is the code of the ambulance's location.

        Returns:
            str: The code of the closest ambulance's location or None if no ambulances are available.
        """
        # Compute shortest paths
        shortest_paths = floyd_warshall(self)

        # Find the index of the house_code
        nodes_head = self.to_adjacency_matrix()[1]
        node_map = {}
        current = nodes_head
        index = 0
        while current:
            node_map[current.data] = index
            current = current.next
            index += 1

        if house_code not in node_map:
            print(f"Error: House code {house_code} not found in the graph.")
            return None

        house_index = node_map[house_code]

        # Get the distances from the house
        row = shortest_paths
        for _ in range(house_index):
            row = row.next
        distances = row.data

        # Iterate through ambulances to find the closest one
        closest_ambulance = None
        min_distance = float('inf')
        current_ambulance = ambulances

        while current_ambulance:
            ambulance_code = current_ambulance.code
            if ambulance_code not in node_map:
                print(f"Warning: Ambulance location {ambulance_code} not found in the graph.")
                current_ambulance = current_ambulance.next
                continue

            ambulance_index = node_map[ambulance_code]

            # Retrieve the distance from the adjacency matrix
            distance = distances
            for _ in range(ambulance_index):
                distance = distance.next

            if distance.data < min_distance:
                min_distance = distance.data
                closest_ambulance = ambulance_code

            current_ambulance = current_ambulance.next

        if closest_ambulance:
            print(f"The closest ambulance to house {house_code} is at {closest_ambulance} with a distance of {min_distance}.")
        else:
            print(f"No available ambulances for house {house_code}.")

        return closest_ambulance


class Ambulance:
    def __init__(self, location, hospital, code):
        self.hospital = hospital
        self.location = location
        self.code = code
        self.next = None



