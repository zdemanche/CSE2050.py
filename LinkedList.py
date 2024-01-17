class LLNode:
    def __init__(self, data, link=None):
        """A linked list node"""
        self.data = data
        self.link = link

    # Recursive Example - recursively call on self.link until tail node
    def __len__(self):
        """Recursively calculates how many items are in LL starting at this node"""
        if self.link is None:
            return 1  # base case - tail node, len = 1
        return 1 + len(self.link)  # otherwise, len = 1 + len(next)

    # Recursive example - helper function to create a mutable to store state at all levels of recursion
    def __repr__(self):
        """Recursively prints all nodes"""
        return ''.join(self._repr([]))

    def _repr(self, item_list):
        """Helper function (so item_list can be initialized as an empty mutable)"""
        if self.link is None:
            item_list.append(f"{self.data}")  # Base case - add the final item
        else:
            item_list.append(f"{self.data} ->")  # Print the current node, no newline
            self.link._repr(item_list)

        return item_list

    # Recursive example - get the last item, and pass it back through all levels of recursion
    def get_tail(self):
        """Recursively gets the item stored in the tail node"""
        if self.link is None:
            return self.data
        else:
            return self.link.get_tail()

    def add_last(self, item):
        """Recursively adds an item to the end of the linked list"""
        if self.link is None:
            self.link = LLNode(item)
        else:
            self.link.add_last(item)

    def sum_all(self):
        """Recursively calculates the sum of all items in the linked list"""
        if self.link is None:
            return self.data
        else:
            return self.data + self.link.sum_all()

    def reverse(self, prev=None):
        """Recursively reverses the linked list in place"""
        if self.link is None:
            self.link = prev
            return self
        else:
            next_node = self.link
            self.link = prev
            return next_node.reverse(self)


class LinkedList:
    def __init__(self, items=None):
        """Initializes a new empty LinkedList"""
        self._head = None
        if items is not None:
            for item in items:
                self.add_last(item)  # use add_last() to maintain ordering

    def add_first(self, item):
        """Adds to the beginning of Linked List"""
        self._head = LLNode(item, self._head)

    def remove_first(self):
        """Removes and returns the first item"""
        if self._head is None:
            raise RuntimeError('Cannot remove from an empty list.')  # Edge case

        item = self._head.data  # retrieve data
        self._head = self._head.link  # update head
        return item  # return

    # For demonstration and debug purposes: Prints all the elements
    def __repr__(self):
        """Recursively prints the Linked List"""
        return repr(self._head)

    def __len__(self):
        """Returns the number of nodes in Linked List"""
        return len(self._head) if self._head else 0

    def add_last(self, item):
        """Adds item to the end of Linked List"""
        if self._head is None:
            return self.add_first(item)
        self._head.add_last(item)

    def sum_all(self):
        """Returns sum of all items in Linked List"""
        return self._head.sum_all() if self._head else 0

    # Reverses the list in linear time, no copying of the data
    def reverse(self):
        """Reverses linked list"""
        # Note that LLNode.reverse() should return the new head
        self._head = self._head.reverse() if self._head else None

    def get_tail(self):
        """Returns the item stored in the tail"""
        return self._head.get_tail() if self._head else None

# Example usage:
if __name__ == '__main__':
    L = [1, 2, 3, 4, 5]
    linked_list = LinkedList(L)

    print("Original Linked List:", linked_list)
    linked_list.reverse()
    print("Reversed Linked List:", linked_list)
    print("Sum of All Elements:", linked_list.sum_all())
    print("Length of Linked List:", len(linked_list))
    print("Tail of Linked List:", linked_list.get_tail())
