import random

class Node:
    """ Node class that can be doubly linked. Sets next and previous to None.
        
        Args:
            data (str): Pass the data for the node to store. Default is None.
    """
    def __init__(self, data: str | None = None):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    """ LinkedList class that will create nodes dynamically on init or add. This is a doubly linked list.
        This linked list keeps track of the head as well as the tail.

        Args:
            data (str): Data to pass to the node to store. Default is None.
    """
    def __init__(self, data: str | None = None):
        self.head = None
        self.tail = None

        if data is not None:
            self.append(data)

    def append(self, data: str):
        """ Add to the linked list and appropriately link previous, next, and tail.

            Args:
                data (str): Data to pass to the node.

            Returns:
                Node: The node that was input into the LinkedList.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return new_node
        
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node

        return new_node

    def prepend(self, data: str):
        """ Add to the start of the linked list.

            Args:
                data (str): Data to pass to the node.

            Returns:
                Node: The node that was input into the LinkedList.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return new_node

        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        
        return new_node
    
    def shuffle(self):
        """ Shuffle our LinkedList.
        """
        if not self.head or not self.head.next:
            return

        next_node = self.head
        shuff_nodes = []
        while next_node:
            shuff_nodes.append(next_node)
            next_node = next_node.next

        random.shuffle(shuff_nodes)
        self.head = shuff_nodes[0]
        self.tail = shuff_nodes[-1]

        for i in range(len(shuff_nodes) - 1):
            shuff_nodes[i].next = shuff_nodes[i+1]
            shuff_nodes[i + 1].previous = shuff_nodes[i]
        
        # We have to reset previous for head and next for tail because we are shuffling nodes.
        # So if our tail is a node that had a next before shuffling self.tail.next won't be None.
        # This will break while loops being used after shuffling.
        self.head.previous = None
        self.tail.next = None

    def __str__(self):
        """ Print the contents of the playlist.
        """
        next_node = self.head
        ll_str_list = []
        while next_node:
            ll_str_list.append(next_node.data)
            next_node = next_node.next
        return "\n".join(ll_str_list)

