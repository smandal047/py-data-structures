class Tree:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            raise ValueError('{} insertion failed. No Duplicate value allowed')
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)

    # inorder transversal
    def find(self, data):

        if self.data == data:
            return self
        elif self.data > data:
            if self.left is None:
                return False
            else:
                self.left.find(data)
        else:
            if self.right is None:
                return False
            else:
                self.right.find(data)

    def __str__(self):

        print('==========Tree===========')
        self.tprint()
        return '=====str repr of tree====='

    def tprint(self, count=0, end='\n'):
        """
                    50
                    |
                    |--40
                    |
                    |--70
                       |
                       |--60
                       |
                       |--80
        """

        PIPE = "│"
        # ELBOW = "└──"
        ELBOW = "--"
        TEE = "├──"
        PIPE_PREFIX = "│   "
        SPACE_PREFIX = "    "

        if self is not None:
            print(self.data, end=end)
            # print(PIPE, end='')

            if self.left is not None:
                print(SPACE_PREFIX * count + TEE, end='')
                # print(ELBOW, end='')
                count += 1
                self.left.tprint(count, end='\n')

                count -= 1

            if self.right is not None:
                print(SPACE_PREFIX * count + TEE, end='')
                # print(ELBOW, end='')
                count += 1
                self.right.tprint(count, end='\n')

    def height(self):

        if self is None:
            return 0

        left_height = 0 if self.left is None else self.left.height()
        right_height = 0 if self.right is None else self.right.height()

        return max(left_height, right_height) + 1

    def __len__(self):

        return 0

    def delete(self, data):
        """
                      50                            60
                   /     \         delete(50)      /   \
                  40      70       --------->    40    70
                         /  \                            \
                        60   80                           80

        in order successor method -----------
        """

        # if self is None:

        parent = None
        curr = None

        # self.find(data)
        if self.data == data:
            # case 1 - leaf node
            if self.left is None and self.right is None:
                print(f'found u case 1 {self.data}')

            # case 2 - non leaf, 1 right child
            elif self.left is None and self.right is not None:
                # transverse right and find for child
                print(f'found u case 2.1 {self.data}')

            # case 2 - non leaf, 1 left child
            elif self.left is not None and self.right is None:
                print(f'found u case 2.2 {self.data}')

            # case 3 - non leaf, 2 child
            elif self.left is not None and self.right is not None:
                print(f'found u case 3 {self.data}')

            # case 4 - non leaf, 2 child w/ right leaf child

        else:
            if self.left is not None:
                self.left.delete(data)
            if self.right is not None:
                self.right.delete(data)

        # case 1 - leaf node

        # case 2 - non leaf, 1 child

        # case 3 - non lead, 2 child

        # case 4 - non leaf, 2 child w/ greater leaf child


if __name__ == '__main__':

    # a = Tree(1)
    # a.insert(2)
    # # a.insert(16)
    # a.insert(-5)

    a = Tree(50)
    a.insert(40)
    a.insert(70)
    a.insert(60)
    a.insert(80)
    a.insert(90)
    a.insert(10)
    a.insert(5)
    a.insert(30)
    a.insert(45)
    a.insert(46)

    # l = [500, 200, 75, 250, 100]
    # for i in l:
    #     a.insert(i)

    print(a)

    print(a.height())

    # print(a.find(2))
    # print(a.find(-5))

    print('---------del')
    a.delete(46)
    print('---------del done')

    print(a)
