# node of the linked list
class ListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


# singly linked list creation by list
class SinglyLinkedList:
    # private member so that head can only be accessed via the class but nor by objects
    __init_node = None

    def __init__(self, list_arr):
        self.__init_node = None
        self.list_arr = list_arr
        self.__create_linked_list()

    # creates a single linked list using list
    def __create_linked_list(self):

        # takes the buffer of previous node
        prev_buffer = None
        for data in self.list_arr:
            # the current node
            buffer = ListNode(data)

            # checks for the `next` attribute and proceed
            if getattr(prev_buffer, 'next', False) is None:
                prev_buffer.next = buffer
            else:
                self.__init_node = buffer

            # setting the previous node
            prev_buffer = buffer

    # transversing the linked list
    def transverse(self):

        loop = True

        # setting the head
        buffer = self.__init_node

        # looping for the linked list
        while loop:
            print(buffer.data)

            # if `next` attribute is None exit
            if buffer.next is not None:
                buffer = buffer.next
            else:
                print('---the end---')
                loop = False


if __name__ == '__main__':
    a = range(14)

    ll = SinglyLinkedList(a)
    ll.transverse()
