from packages.datastructures import *
from packages.functions import *

graph = Graph()
used_names = Linked_list()
used_names_pointer = used_names

# # Example usage
# graph = Graph()

# # Add nodes
# graph.add_node("A", "house")
# graph.add_node("B", "hospital")
# graph.add_node("C", "normal")
# graph.add_node("D", "normal")

# # Add edges
# graph.add_edge("A", "B", 2)
# graph.add_edge("A", "C", 5)
# graph.add_edge("B", "D", 1)
# graph.add_edge("C", "D", 2)

# # Display the graph
# graph.display_graph()
# # Find the shortest path from A to D
# shortest_distance = dijkstra(graph, "A", "D")
# print(f"Shortest distance from A to D: {shortest_distance}")


def create_node() ->None:
    global used_names_pointer, graph
    ask = True
    while ask:
        try:
            type = int(input('type of the node ([1]hospital [2]house [3]normal point): '))
            if type not in [1, 2, 3]:
                raise ValueError()
            ask = False
        except ValueError:
            print("Choose between 1, 2 and 3")
    ask = True
    while ask:
        name = input('Node name: ')
        print(not linkedlist_search(used_names, name))
        if linkedlist_search(used_names, name):
            print('This name is already used! try again.')
        else:
            ask = False
            used_names_pointer.next = Linked_list(name)
            used_names_pointer = used_names_pointer.next
    graph.add_node(name, type)
    print("Node created Successfuly!")


runprogram = True
while runprogram:
    ask_question = True
    while ask_question:
        try:
            ask_question = False
            choice = int(input('[1]Create Node    [2]  [3]Exit program\nEnter your choice: '))
            if choice not in [1, 2, 3]:
                raise ValueError()
        except ValueError:
            ask_question = True
    match choice:
        case 3:
            runprogram = False
        case 2:
            # sign_up()
            pass
        case 1:
            create_node()
graph.display_graph()