from packages.datastructures import *
from packages.functions import *

graph = Graph()
used_names = Linked_list()
used_names_pointer = used_names

hospital_ll = Linked_list()
hospital_ll_pointer = hospital_ll

amb_ll = Linked_list()
amb_ll_pointer = amb_ll


graph.add_node("milad", "hospital")
hospital_ll_pointer.next = Linked_list("milad")
hospital_ll_pointer = hospital_ll_pointer.next

graph.add_node("ali", "house")
graph.add_node("reza", "house")
graph.add_node("meydoonemam", "normal_point")
graph.add_node("meydoonhosein", "normal_point")

graph.add_edge("ali", "milad", 5)
graph.add_edge("meydoonemam", "ali", 3)
graph.add_edge("reza", "meydoonemam", 8)
graph.add_edge("milad", "meydoonhosein", 5)
graph.add_edge("meydoonhosein", "reza", 5)



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
    global used_names_pointer, graph, hospital_ll, hospital_ll_pointer
    ask = True
    while ask:
        try:
            type = int(input('type of the node ([1]hospital [2]house [3]normal point): '))
            if type not in [1, 2, 3]:
                raise ValueError()
            ask = False
            match type:
                case 1: type_name = "hospital"
                case 2: type_name = "house"
                case 3: type_name = "normal_point" 
        except ValueError:
            print("Choose between 1, 2 and 3")
    ask = True
    while ask:
        name = input('Node name: ')
        if linkedlist_search(used_names, name):
            print('This name is already used! try again.')
        else:
            ask = False
            used_names_pointer.next = Linked_list(name)
            used_names_pointer = used_names_pointer.next
    graph.add_node(name, type_name)
    node = graph._get_node(name)
    ask = True
    while ask:
        to_code = input("Enter 'to_node' to create the first edge: ")
        weight = int(input("Enter 'weight' : "))
        graph.add_edge(name, to_code, weight)
        if node.edges:
            ask = False
        else:
            print('(!) Invalid "to_node". try again\n')
    if type_name == "hospital":                         #Add to hospital lili
        hospital_ll_pointer.next = Linked_list(name)
        hospital_ll_pointer = hospital_ll_pointer.next
    print("\n(*) Node creation Complete!\n")


def define_edges() ->None:
    global graph
    question = True
    while question:
        question = True
        try:
            question=False
            choice = int(input("[1]define edge  [2]exit\nChoice: "))
            if choice not in [1, 2]:
                raise ValueError()
            match choice:
                case 2:
                    pass
                case 1:
                    from_code = input("Enter 'from_node' : ")
                    to_code = input("Enter 'to_node' : ")
                    weight = int(input("Enter 'weight' : "))
                    graph.add_edge(from_code, to_code, weight)
                    question = True
        except ValueError:question=True


def Two_way_graph(graph):
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


def get_distance():
    from_code = input("\nEnter 'from_node' : ")
    to_code = input("Enter 'to_node' : ")
    if graph._get_node(from_code) == None or graph._get_node(to_code) == None:
        print("\n(!) Invalid Entry\n")
        return 
    shortest_distance = dijkstra(graph, from_code, to_code)
    print(f"Shortest distance from {from_code} to {to_code}: {shortest_distance}")


def role_seperator():
    global graph
    name = input("Enter name: ")
    node = graph._get_node(name)
    if node == None:
        print("Node not found!")
        return
    type = node.type
    match type:
        case "normal_point":
            print("This node is a normal point without function")
            return
        case "hospital": hospital_menu(node)
        case "house": house_menu(node)


# ________________________________________________Hospital____________________________


def hospital_menu(node:Node):
    print(f"\nLogged in as {node.code} Hospital\n")
    ask_question = True
    while ask_question:
        try:
            choice = int(input('\n[1]Create Ambulance    [2]Show all ambulences\n[3]Move ambulence  [4]Travel history    [5]Exit\n\nEnter your choice: '))
            if choice not in [1, 2, 3, 4, 5]:
                raise ValueError()
            match choice:
                case 5:
                    ask_question = False
                case 1:
                    create_ambulance(node)
                case 2:
                    show_ambulances(node)
                case 3:
                    move_ambulance(node)
                case 4:
                    pass
        except ValueError:
            print("\n(!) Enter a number between 1 to 5\n")
            pass


def create_ambulance(node: Node):
    global amb_ll, amb_ll_pointer

    code = input("Ambulance code: ")
    current = node.ambulances
    while current:
        if current.code == code:
            print("(!) Ambulance already exists!")
            return
        current = current.next

    new_ambulance = Ambulance(node, node.code, code)
    if node.ambulances is None:  
        node.ambulances = new_ambulance
    else:
        current = node.ambulances
        while current.next:
            current = current.next
        current.next = new_ambulance

    if amb_ll_pointer is None:
        amb_ll = new_ambulance
        amb_ll_pointer = new_ambulance
    else:
        amb_ll_pointer.next = new_ambulance
        amb_ll_pointer = new_ambulance

    if graph._get_node(new_ambulance.location.code) is None:
        print(f"Warning: Ambulance location {new_ambulance.location.code} not found in the graph.")
    else:
        print("(*) Ambulance created!")


def show_all_ambulances():
    global amb_ll
    current = amb_ll
    print("\nAll Ambulances:")
    while current:
        print(f"Ambulance Code: {current.code}, Location: {current.location.code if current.location else 'None'}")
        current = current.next
    print()


def show_ambulances(node: Node):
    ambulances = node.ambulances
    print()
    if not ambulances :
        print("No ambulences!")
    while ambulances:
        print(f"Code: {ambulances.code}     Location ==> {ambulances.location.code}")
        ambulances = ambulances.next
    print()


def move_ambulance(node:Node):
    amb_code = input("Enter ambulance code: ")
    amb_result = hospital_get_ambulance(node, amb_code) #Functions.py  search and return the amb with that code
    if amb_result == None:
        print('\n(!) This hospital doesnt have this ambulance\n')
        return
    target_node_code = input("Enter destination name: ")
    target_result = graph._get_node(target_node_code)
    if target_result == None:
        print('\n(!) The location You are looking for doesnt exist\n')
        return
    previous_loc = amb_result.location
    amb_result.location = target_result
    print(f'\n(*) Ambulance {amb_result} location :   {previous_loc} ==> {target_result}\n')


# ________________________________________________House____________________________

def house_menu(node: Node):
    print(f"\nLogged in as {node.code} Citizen\n")
    ask_question = True
    while ask_question:
        try:
            choice = int(input('\n[1]Request Ambulance    [2]Exit\n\n\nEnter your choice: '))
            if choice not in [1, 2, 3, 4, 5]:
                raise ValueError()
            match choice:
                case 1:
                    house_request_ambulance(node)
                case 2:
                    ask_question = False           
        except ValueError:
            print("\n(!) Enter a number from 1 and 2\n")
            pass
    
    
def house_request_ambulance(node):
    global amb_ll
    hpointer = hospital_ll.next
    while hpointer:
        print(hpointer.data)
        hpointer = hpointer.next
    ask = True
    while ask:
        hos_name = input("\nchoose your hospital: ")
        if not house_search_hospital(hospital_ll, hos_name):  # functions.py
            print("\n(!) Choose a valid hospital")
        else:
            ask = False
    if not house_hospital_has_ambulance(graph, hos_name):  # functions.py
        print("\n(!) This hospital has no ambulances")
        ambulences = amb_ll
    ambulences = graph._get_node(hos_name).ambulances
    new_graph = Two_way_graph(graph)
    
    # Ensure each ambulance in the list has a valid location
    current = ambulences
    while current:
        if graph._get_node(current.location.code) is None:
            print(f"Warning: Ambulance location {current.location.code} not found in the graph.")
        current = current.next
    
    closest_amb = new_graph.house_request_ambulance(node.code, ambulences)
    print(closest_amb)

    

# ________________________________________________Main____________________________


runprogram = True
while runprogram:
    ask_question = True
    while ask_question:
        try:
            ask_question = False
            choice = int(input('[1]Create Node\n[2]Define Edges\n[3]Enter Role\n[4]Show Graph\n[5]Calculate Distance\n[6]Exit program\n\nEnter your choice: '))
            if choice not in [1, 2, 3, 4, 5,6]:
                raise ValueError()
        except ValueError:
            ask_question = True
    match choice:
        case 6:
            runprogram = False
        case 2:
            define_edges()
        case 1:
            create_node()
        case 3:
            role_seperator()
        case 4:
            graph.display_graph()
        case 5:
            get_distance()