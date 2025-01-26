from packages.datastructures import *

def dijkstra(graph, start_code, end_code):
    # Custom structure to store distances and visited status
    class DistanceNode:
        def __init__(self, code, distance, visited):
            self.code = code
            self.distance = distance
            self.visited = visited
            self.next = None

    # Initialize distance list as a linked list
    distance_head = None
    current = graph.head
    while current:
        new_distance_node = DistanceNode(current.code, float('inf'), False)
        new_distance_node.next = distance_head
        distance_head = new_distance_node
        current = current.next

    # Set the starting node distance to 0
    current = distance_head
    while current:
        if current.code == start_code:
            current.distance = 0
            break
        current = current.next

    def get_distance_node(code):
        current = distance_head
        while current:
            if current.code == code:
                return current
            current = current.next
        return None

    while True:
        # Find the unvisited node with the smallest distance
        current_distance_node = None
        min_distance = float('inf')
        current = distance_head
        while current:
            if not current.visited and current.distance < min_distance:
                min_distance = current.distance
                current_distance_node = current
            current = current.next

        if not current_distance_node or current_distance_node.code == end_code:
            break

        current_distance_node.visited = True
        current_node = graph._get_node(current_distance_node.code)

        # Update distances for neighbors
        edge = current_node.edges
        while edge:
            neighbor_distance_node = get_distance_node(edge.target)
            if neighbor_distance_node and not neighbor_distance_node.visited:
                new_distance = current_distance_node.distance + edge.weight
                if new_distance < neighbor_distance_node.distance:
                    neighbor_distance_node.distance = new_distance
            edge = edge.next

    # Get the final distance to the end node
    end_distance_node = get_distance_node(end_code)
    return end_distance_node.distance if end_distance_node else float('inf')


def Two_way_graph(graph: Graph) -> Graph:
    if graph.head == None:
        return None
    new_graph = Graph()
    head = graph.head
    while head:
        new_graph.add_node(head.code, head.type)
        head = head.next
    head = graph.head
    while head:
        edges = head.edges
        while edges:
            new_graph.add_edge(head.code, edges.target, edges.weight)
            new_graph.add_edge(edges.target, head.code, edges.weight)
            edges = edges.next
        head = head.next
    return new_graph



def linkedlist_search(head:Linked_list, data):
    while head:
        if head.data == data:
            return True
        head = head.next
    return False


def hospital_get_ambulance(hospital:Node, amb_code):
    ambulances = hospital.ambulances
    while ambulances:
        if ambulances.code == amb_code:
            return ambulances
        ambulances = ambulances.next
    return None


def house_search_hospital(hospitals: Linked_list, name):
    pointer = hospitals
    while pointer:
        if pointer.data == name:
            return True
        pointer = pointer.next
    return False


def house_hospital_has_ambulance(graph: Graph, name):
    hospital = graph._get_node(name)
    ambs = hospital.ambulances
    if ambs:
        return True
    return False
