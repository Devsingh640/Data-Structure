class node():
    def __init__(self, info):
        self.node_data = info
        self.next_node_link = None
    def print_node(self):
        print(node)
class link_list():
    def __init__(self):
        self.head = None
    def print_link_list(self):
        temp = self.head
        while(temp):
            print(temp.node_data, end = " ")
            temp = temp.next_node_link

if __name__ == "__main__":

    t = link_list()
    t.head = node(1)
    second_node = node(2)
    third_node = node(3)
    t.head.next_node_link = second_node
    second_node.next_node_link = third_node
    t.print_link_list()
    print(" ")
    deletion_node = second_node
    t.head.next_node_link = third_node
    second_node = None
    t.print_link_list()