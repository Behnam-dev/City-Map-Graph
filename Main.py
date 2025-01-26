from packages.datastructures import *
from packages.functions import *

graph = Graph()
used_names = Linked_list()
used_names_pointer = used_names


graph.add_node("milad", "hospital")


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
        case "house": pass

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
    ambulances = node.ambulances
    code = input('Ambulance code: ')
    while ambulances:
        if ambulances.code == code:
            print("(!) Ambulance already exists!")
            return
        ambulances = ambulances.next
    new_ambulance = Ambulance(node, node.code, code)
    new_ambulance.next = node.ambulances
    node.ambulances = new_ambulance
    print("(*) Ambulance created!")
    return


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



    
    

# ________________________________________________Main____________________________


runprogram = True
while runprogram:
    ask_question = True
    while ask_question:
        try:
            ask_question = False
            choice = int(input('[1]Create Node\n[2]Define Edges\n[3]Enter Role\n[4]Show Graph\n[5]Exit program\n\nEnter your choice: '))
            if choice not in [1, 2, 3, 4, 5]:
                raise ValueError()
        except ValueError:
            ask_question = True
    match choice:
        case 5:
            runprogram = False
        case 2:
            define_edges()
        case 1:
            create_node()
        case 3:
            role_seperator()
        case 4:
            graph.display_graph()