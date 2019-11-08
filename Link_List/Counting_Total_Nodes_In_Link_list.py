class node():
    def __init__(self, data):
        self.info = data
        self.link = None


class linklist():
    def __init__(self):
        self.head = None

    def print_linklist(self):
        temp = self.head
        while(temp):
            print(temp.info, end = " ")
            temp = temp.link

    def total_nodes(self):
        temp = self.head
        count = 0
        while(temp):
            count = (count + 1)
            temp = temp.link
        return count

if __name__ == "__main__":
    x = int(input("Enter total no of data elements to be stored in link-list : "))
    my_linklist = linklist()
    flag = 0
    for x in range(0, x):
        data = int(input("Enter data : "))
        temp = node(data)
        if (flag==0):
            my_linklist.head = temp
            flag = 1
        else:
            previous_node.link = temp
        previous_node = temp

    print(" ")
    my_linklist.print_linklist()
    print(" ")
    print("Total number of nodes : ", my_linklist.total_nodes())