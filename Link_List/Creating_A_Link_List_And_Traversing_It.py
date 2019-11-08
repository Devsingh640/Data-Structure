class node():
    
    def __init__(self, info):
        self.node_data = info
        self.next_node_link = None

class link_list():
    
    def __init__(self):
        self.head = None
    
    def print_link_list(self):
        temp_node = self.head
        while(temp_node):
            print(temp_node.node_data, end = " ")
            temp_node = temp_node.next_node_link

if __name__ == "__main__":
    x = int(input("Enter total no of data elements to be stored in link-list : "))
    flag = 0    #initially flag not set.
    my_link_list = link_list()
    for el in range(0, x):
        info = input("Enter %d element to be stored in link-list : " % (el + 1))
        this_node = node(info)
        if(flag == 0): #checked if flag is not set.
            my_link_list.head = this_node    
            flag = 1    #flag set.
        else:
            previous_node.next_node_link = this_node
        previous_node =  this_node
    my_link_list.print_link_list()