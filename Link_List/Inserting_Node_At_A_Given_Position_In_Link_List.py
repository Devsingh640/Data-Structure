import numpy as np

class node():
    def __init__(self, data):
        self.info = data
        self.link = None

class linked_list():
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.info, end = " ")
            temp = temp.link
        
    def insert_node_at(self, data, head):
        at_index = int(input("Enter index for node where new node needs to be inserted : "))
        temp_node = node(data)
        temp = head
        count = 0
        if(head == None):
            head = temp_node
            return
        while (temp):
            if(count == at_index - 1):
                break
            temp = temp.link
            count = (count + 1)
        next = temp.link
        temp.link = temp_node
        temp_node.link = next
        return head

if __name__ == "__main__":
    x = np.random.randint(1,20)
    my_linked_list = linked_list()
    flag = 0
    for el in range(0, x):
        data = np.random.randint(0,20)
        temp = node(data)
        if(flag == 0):
            my_linked_list.head = temp
            flag = 1
        else:
            previous_node.link = temp
        previous_node = temp

    my_linked_list.print_linked_list()
    print(" ")
    my_linked_list.head = my_linked_list.insert_node_at(666, my_linked_list.head)
    my_linked_list.print_linked_list()