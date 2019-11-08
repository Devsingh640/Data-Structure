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

    def tell_value(self):
        count = 0
        find_value = int(input("Enter index for node whose info needs to be found out : "))
        temp = self.head
        while(temp and count <= find_value):
            val = temp.info
            index = count
            count = (count + 1)
            temp = temp.link
        return (val, index)

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
    print(my_linked_list.tell_value())