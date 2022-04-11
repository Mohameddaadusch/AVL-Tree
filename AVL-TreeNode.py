
# username - andalrhmana
# id1      - 322923087
# name1    - andalrhmana
# id2      - daadusch
# name2    - 212001192


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0
        self.prevheight = -1

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        if not self:
            return None
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        if not self:
            return None
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        if not self:
            return None
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        if not self:
            return None
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        if not self:
            return -1
        return self.height

    """returns the size

        @rtype: int
        @returns: the  of self, 0 if the node is virtual
        """

    def getSize(self):
        if not self:
            return 0
        return self.size

    """returns the previous height

        @rtype: int
        @returns: the  of self, -1 if the node is virtual
        """

    def getPrevHeight(self):
        if not self:
            return -1
        return self.prevheight

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        if self != None:
            self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        if self.height != -1:
            self.prevheight = self.height
            self.height = h
        else:
            self.prevheight = h
            self.height = h


    """sets the size of the node

    @type s: int\
    @param s: the size
    """


    def setSize(self, s):
        self.size = s


    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """


    def isRealNode(self):
        if not self:
            return False
        return True


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None
        # add your fields here

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.root == None

    """retrieves the node of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the node of the i'th item in the list
    """

    def Tree_select(self, i):
        return AVLTreeList.Tree_select_rec(self.root, i)

    def Tree_select_rec(root, i):
        z = AVLNode.getSize(AVLNode.getLeft(root)) + 1
        if i == z:
            return root
        elif i < z:
            return AVLTreeList.Tree_select_rec(AVLNode.getLeft(root), i)
        else:
            return AVLTreeList.Tree_select_rec(AVLNode.getRight(root), i - z)

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        return AVLNode.getValue(Tree_select(self, i))

    """retrieves the node of the 1'th item in the list of the node@self.root = node 

    @returns: the the node of the 1'th item in the list
    """

    def MinAvl(node):
        if AVLNode.isRealNode(node):
            while AVLNode.isRealNode(AVLNode.getLeft(node)):
                node = AVLNode.getLeft(node)
        return node

    """return the successor of the node in the list 

    @returns: the successor of the node in the list
    """

    def successor(node):
        if AVLNode.isRealNode(AVLNode.getRight(node)):
            return AVLTreeList.MinAvl(AVLNode.getRight(node))
        y = AVLNode.getParent(node)
        while AVLNode.isRealNode(y) and node == AVLNode.getRight(y):
            node = y
            y = AVLNode.getParent(node)
        return y

    """retrieves the node of the lasr item in the list of the node@self.root = node 

    @returns: the the node of the last item in the list
    """

    def MaxAvl(node):
        if AVLNode.isRealNode(node):
            while AVLNode.isRealNode(AVLNode.getRight(node)):
                node = AVLNode.getRight(node)
        return node

    """return the predecessor of the node in the list 

    @returns: the predecessor of the node in the list
    """

    def predecessor(node):
        if AVLNode.isRealNode(AVLNode.getLeft(node)):
            return AVLTreeList.MaxAvl(AVLNode.getLeft(node))
        y = AVLNode.getParent(node)
        while AVLNode.isRealNode(y) and node == AVLNode.getLeft(y):
            node = y
            y = AVLNode.getParent(node)
        return y

    """
    Set the height and size from the node to root of in the list
    """

    def setSizeandHeight(node):
        while AVLNode.isRealNode(node):
            AVLNode.setSize(node, AVLNode.getSize(AVLNode.getRight(node)) + AVLNode.getSize(AVLNode.getLeft(node)) + 1)
            AVLNode.setHeight(node, max(AVLNode.getHeight(AVLNode.getLeft(node)), AVLNode.getHeight(AVLNode.getRight(node))) + 1)
            node = AVLNode.getParent(node)

    """
    Set the height from the node to root of in the list
    """

    def setheightRotation(node):
        while AVLNode.isRealNode(AVLNode.getParent(node)):
            AVLNode.setHeight(node, max(AVLNode.getHeight(AVLNode.getLeft(node)), AVLNode.getHeight(AVLNode.getRight(node))) + 1)
            node = AVLNode.getParent(node)

    """
    balance the tree - left left rotaion
    """

    def RotationLL(B):
        A = AVLNode.getLeft(B)
        AVLNode.setLeft(B, AVLNode.getRight(A))
        AVLNode.setParent(AVLNode.getLeft(B), B)
        AVLNode.setRight(A, B)
        AVLNode.setParent(A, AVLNode.getParent(B))
        if AVLNode.isRealNode(AVLNode.getParent(B)):
            if AVLNode.getLeft(AVLNode.getParent(B)) == B:
                AVLNode.setLeft(AVLNode.getParent(B), A)
            else:
                AVLNode.setRight(AVLNode.getParent(B), A)
        AVLNode.setParent(B, A)
        AVLNode.setSize(B, AVLNode.getSize(AVLNode.getLeft(B)) + AVLNode.getSize(AVLNode.getRight(B)) + 1)
        AVLNode.setSize(A, AVLNode.getSize(AVLNode.getLeft(A)) + AVLNode.getSize(AVLNode.getRight(A)) + 1)
        AVLNode.setHeight(B, max(AVLNode.getHeight(AVLNode.getLeft(B)), AVLNode.getHeight(AVLNode.getRight(B))) + 1)
        AVLNode.setHeight(A, max(AVLNode.getHeight(AVLNode.getLeft(A)), AVLNode.getHeight(AVLNode.getRight(A))) + 1)

    """
    balance the tree - right right rotaion
    """

    def RotationRR(B):
        A = AVLNode.getRight(B)
        AVLNode.setRight(B, AVLNode.getLeft(A))
        AVLNode.setParent(AVLNode.getRight(B), B)
        AVLNode.setLeft(A, B)
        AVLNode.setParent(A, AVLNode.getParent(B))
        if AVLNode.isRealNode(AVLNode.getParent(B)):
            if AVLNode.getRight(AVLNode.getParent(B)) == B:
                AVLNode.setRight(AVLNode.getParent(B), A)
            else:
                AVLNode.setLeft(AVLNode.getParent(B), A)

        AVLNode.setParent(B, A)
        AVLNode.setSize(B, AVLNode.getSize(AVLNode.getLeft(B)) + AVLNode.getSize(AVLNode.getRight(B)) + 1)
        AVLNode.setSize(A, AVLNode.getSize(AVLNode.getLeft(A)) + AVLNode.getSize(AVLNode.getRight(A)) + 1)
        AVLNode.setHeight(B, max(AVLNode.getHeight(AVLNode.getLeft(B)), AVLNode.getHeight(AVLNode.getRight(B))) + 1)
        AVLNode.setHeight(A, max(AVLNode.getHeight(AVLNode.getLeft(A)), AVLNode.getHeight(AVLNode.getRight(A))) + 1)

    """
    balance the tree - left right rotaion
    """

    def RotationLR(C):
        B = AVLNode.getRight(AVLNode.getLeft(C))
        A = AVLNode.getLeft(C)
        AVLNode.setLeft(C, AVLNode.getRight(B))
        AVLNode.setParent(AVLNode.getLeft(C), C)
        AVLNode.setRight(A, AVLNode.getLeft(B))
        AVLNode.setParent(AVLNode.getRight(A), A)
        AVLNode.setRight(B, C)
        AVLNode.setParent(B, AVLNode.getParent(C))
        if AVLNode.isRealNode(AVLNode.getParent(C)):
            if AVLNode.getRight(AVLNode.getParent(C)) == C:
                AVLNode.setRight(AVLNode.getParent(C), B)
            else:
                AVLNode.setLeft(AVLNode.getParent(C), B)
        AVLNode.setParent(C, B)
        AVLNode.setLeft(B, A)
        AVLNode.setParent(A, B)
        AVLNode.setSize(C, AVLNode.getSize(AVLNode.getLeft(C)) + AVLNode.getSize(AVLNode.getRight(C)) + 1)
        AVLNode.setSize(A, AVLNode.getSize(AVLNode.getLeft(A)) + AVLNode.getSize(AVLNode.getRight(A)) + 1)
        AVLNode.setSize(B, AVLNode.getSize(AVLNode.getLeft(B)) + AVLNode.getSize(AVLNode.getRight(B)) + 1)
        AVLNode.setHeight(C, max(AVLNode.getHeight(AVLNode.getLeft(C)), AVLNode.getHeight(AVLNode.getRight(C))) + 1)
        AVLNode.setHeight(A, max(AVLNode.getHeight(AVLNode.getLeft(A)), AVLNode.getHeight(AVLNode.getRight(A))) + 1)
        AVLNode.setHeight(B, max(AVLNode.getHeight(AVLNode.getLeft(B)), AVLNode.getHeight(AVLNode.getRight(B))) + 1)

    """
    balance the tree - right left rotaion
    """

    def RotationRL(C):
        B = AVLNode.getLeft(AVLNode.getRight(C))
        A = AVLNode.getRight(C)
        AVLNode.setRight(C, AVLNode.getLeft(B))
        AVLNode.setParent(AVLNode.getRight(C), C)
        AVLNode.setLeft(A, AVLNode.getRight(B))
        AVLNode.setParent(AVLNode.getLeft(A), A)
        AVLNode.setLeft(B, C)
        AVLNode.setParent(B, AVLNode.getParent(C))
        if AVLNode.isRealNode(AVLNode.getParent(C)):
            if AVLNode.getLeft(AVLNode.getParent(C)) == C:
                AVLNode.setLeft(AVLNode.getParent(C), B)
            else:
                AVLNode.setRight(AVLNode.getParent(C), B)
        AVLNode.setParent(C, B)
        AVLNode.setRight(B, A)
        AVLNode.setParent(A, B)
        AVLNode.setSize(C, AVLNode.getSize(AVLNode.getLeft(C)) + AVLNode.getSize(AVLNode.getRight(C)) + 1)
        AVLNode.setSize(A, AVLNode.getSize(AVLNode.getLeft(A)) + AVLNode.getSize(AVLNode.getRight(A)) + 1)
        AVLNode.setSize(B, AVLNode.getSize(AVLNode.getLeft(B)) + AVLNode.getSize(AVLNode.getRight(B)) + 1)
        AVLNode.setHeight(C, max(AVLNode.getHeight(AVLNode.getLeft(C)), AVLNode.getHeight(AVLNode.getRight(C))) + 1)
        AVLNode.setHeight(A, max(AVLNode.getHeight(AVLNode.getLeft(A)), AVLNode.getHeight(AVLNode.getRight(A))) + 1)
        AVLNode.setHeight(B, max(AVLNode.getHeight(AVLNode.getLeft(B)), AVLNode.getHeight(AVLNode.getRight(B))) + 1)
    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        newnode = AVLNode(val)
        AVLNode.setHeight(newnode, 0)
        AVLNode.setSize(newnode, 1)
        if i < AVLNode.getSize(self.root):
            current = AVLTreeList.Tree_select(self, i + 1)
            if not AVLNode.isRealNode(AVLNode.getLeft(current)):
                AVLNode.setLeft(current, newnode)
                AVLNode.setParent(newnode, current)
            else:
                predecesso = AVLTreeList.predecessor(current)
                AVLNode.setRight(predecesso, newnode)
                AVLNode.setParent(newnode, predecesso)
        else:
            maxnode = AVLTreeList.MaxAvl(self.root)
            if AVLNode.isRealNode(maxnode):
                AVLNode.setRight(maxnode, newnode)
                AVLNode.setParent(newnode, maxnode)
            else:
                self.root = newnode
        AVLTreeList.setSizeandHeight(newnode)
        dad = AVLNode.getParent(newnode)
        count = 0
        while AVLNode.isRealNode(dad):
            BFdad = AVLNode.getHeight(AVLNode.getLeft(dad)) - AVLNode.getHeight(AVLNode.getRight(dad))
            if -1 <= BFdad <= 1:
                if AVLNode.getHeight(dad) == AVLNode.getPrevHeight(dad):
                    break
                dad = AVLNode.getParent(dad)
            else:
                if BFdad == 2:
                    BFleftson = AVLNode.getHeight(AVLNode.getLeft(AVLNode.getLeft (dad))) - AVLNode.getHeight(AVLNode.getRight(AVLNode.getLeft(dad)))
                    if BFleftson == 1:
                        AVLTreeList.RotationLL(dad)
                        count += 1
                    else:
                        AVLTreeList.RotationLR(dad)
                        count += 2
                else:
                    BFrightson = AVLNode.getHeight(AVLNode.getLeft(AVLNode.getRight(dad))) - AVLNode.getHeight(AVLNode.getRight(AVLNode.getRight(dad)))
                    if BFrightson == 1:
                        AVLTreeList.RotationRL(dad)
                        count += 2
                    else:
                        AVLTreeList.RotationRR(dad)
                        count += 1
                if dad == self.root:
                    self.root = AVLNode.getParent(dad)
                dad = AVLNode.getParent(dad)
                AVLTreeList.setheightRotation(dad)
                break

        return count

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        pop = Tree_select(self, i)
        if getLeft(pop) == None and getRight(pop) == None:
            if getParent(pop) == None:
                self.root == None
            elif getRight(getParent(pop)) == pop:
                setRight(getParent(pop), None)
            else:
                setLeft(getParent(pop), None)
        elif getLeft(pop) == None:
            dad = getParent(pop)
            if dad == None:
                self.root = getRight(pop)
                getParent(self.root, None)
            elif getRight(dad) == pop:
                setRight(dad, getRight(pop))
                setParent(getRight(dad), dad)
            else:
                setLeft(dad, getRight(pop))
                setParent(getLeft(dad), dad)
        elif getRight(pop) == None:
            dad = getParent(pop)
            if dad == None:
                self.root = getLeft(pop)
                getParent(self.root, None)
            elif getRight(dad) == pop:
                setRight(dad, getLeft(pop))
                setParent(getRight(dad), dad)
            else:
                setLeft(dad, getLeft(pop))
                setParent(getLeft(dad), dad)
        else:
            y = successor(pop)
            dad = getParent(y)
            ansecctor = getParent(pop)
            setLeft(ansecctor, getRight(pop))
            setParent(getLeft(ansecctor), ansecctor)
            setLeft(y, getLeft(pop))
            setRight(y, getRight(pop))
            setParent(getLeft(y), y)
            setParent(getRight(y), y)
            setParent(y, ansecctor)
            if dad != None:
                if getRight(ansecctor) == pop:
                    setRight(ansecctor, y)
                else:
                    setLeft(ansecctor, y)
        setSizeandHeight(seccessordad)
        count = 0
        while dad != None:
            BFdad = getHeight(getLeft(dad)) - getHeight(getRight(dad))
            if -1 <= BFdad <= 1:
                if getHeight(dad) == getPrevHeight(dad):
                    break
                dad = getParent(dad)
            else:
                if BFdad == 2:
                    BFleftson = getHeight(getLeft(getLeft(dad))) - getHeight(getLeft(getRight(dad)))
                    if BFleftson == 1 or BFleftson == 0:
                        RotationLL(dad)
                        count += 1
                    else:
                        RotationLR(dad)
                        count += 2
                else:
                    BFrightson = getHeight(getRight(getLeft(dad))) - getHeight(getRight(getRight(dad)))
                    if BFrightson == 1:
                        RotationRL(dad)
                        count += 2
                    else:
                        RotationRR(dad)
                        count += 1
                dad = getParent(dad)
        setheightRotation(dad)
        return count

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        Min = MinAvl(self.root)
        if Min == None:
            return None
        return getValue(MinAvl(self.root))

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        Max = MaxAvl(self.root)
        if Max == None:
            return None
        return getValue(MaxAvl(self.root))

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        listAvl = []
        node = AVLTreeList.MinAvl(self.root)
        if not AVLNode.isRealNode(node):
            return listAvl
        while AVLNode.isRealNode(node):
            listAvl += [AVLNode.getValue(node)]
            node = AVLTreeList.successor(node)
        return listAvl

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return getSize(self.root)

    """splits the list at the i'th index

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list according to whom we split
    @rtype: list
    @returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
    right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
    """

    def split(self, i):
        x = Tree_select(self, i)
        val = getValue(x)
        lefttree = AVLTreeList()
        setParent(getLeft(x), None)
        lefttree.root = getLeft(x)
        righttree = AVLTreeList()
        setParent(getRight(x), None)
        tree.root = getRight(x)
        dad = getParent(x)
        tree = AVLTreeList()
        while dad != None:
            if getRight(dad) == x:
                setRight(dad, None)
                x = dad
                dad = getParent(x)
                setParent(x, None)
                tree.root = x
                Lefttree.concat(tree)
            else:
                setLeft(dad, None)
                x = dad
                dad = getParent(x)
                setParent(x, None)
                tree.root = getRight(x)
                setParent(tree.root, None)
                setRight(x, None)
                setLeft(x, righttree.root)
                setParent(righttree.root, x)
                righttree.root = x
                righttree.concat(tree)
        return [lefttree, val, rightree]

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        if self.root == None:
            self = lst
            return getHeight(lst.root)
        elif lst.root == None:
            return getHeight(self.root)
        node = MaxAvl(self.root)
        Delete(self, getSize(self.root) - 1)
        if getHeight(self.root) >= getHeight(lst.root):
            nodeself = self.root
            absouluteHeight = getHeight(self.root) - getHeight(lst.root)
            while getHeight(nodeself) > getHeight(lst.root):
                nodeself = getRight(nodeself)
            setParent(node, getParent(nodeself))
            setRight(getParent(node), node)
            setLeft(node, nodeself)
            setParent(nodeself, node)
            setRight(node, lst.root)
            setParent(lst.root, node)
            lst = self
            setSizeandHeight(getParent(node), getSize(getRight(node)))
        else:
            absouluteHeight = getHeight(lst.root) - getHeight(self.root)
            nodelst = lst.root
            while getHeight(nodeself) > getHeight(self.root):
                nodelst = getLeft(nodeself)
            setParent(node, getParent(nodelst))
            setLeft(getParent(node), node)
            setRight(node, nodelst)
            setParent(nodelst, node)
            setLeft(node, lst.root)
            setParent(lst.root, node)
            self = lst
        setSizeandHeight(node)
        dad = getParent(node)
        while dad != None:
            BFdad = getHeight(getLeft(dad)) - getHeight(getRight(dad))
            if -1 <= BFdad <= 1:
                if getHeight(dad) == getPrevHeight(dad):
                    break
                dad = getParent(dad)
            else:
                if BFdad == 2:
                    BFleftson = getHeight(getLeft(getLeft(dad))) - getHeight(getLeft(getRight(dad)))
                    if BFleftson == 1 or BFleftson == 0:
                        RotationLL(dad)
                    else:
                        RotationLR(dad)
                else:
                    BFrightson = getHeight(getRight(getLeft(dad))) - getHeight(getRight(getRight(dad)))
                    if BFrightson == 1:
                        RotationRL(dad)
                    else:
                        RotationRR(dad)
                dad = getParent(dad)
        setheightRotation(dad)
        return absouluteHeight

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        count = 1
        node = MinAvl(self.root)
        while node != None:
            if getValue(node) == val:
                return count
            count += 1
            node = successor(node)
        return -1

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root


    def print2(root, space, count):
        if root == None:
           return
        space += count[0]
        AVLTreeList.print2(AVLNode.getRight(root), space, count)
        print()
        for i in range(count[0], space):
            print(end=" ")
        print(AVLNode.getValue(root))
        AVLTreeList.print2(AVLNode.getLeft(root), space, count)

    def print2d(root):
        AVLTreeList.print2(root, 0, [10])

b = AVLTreeList()
b.getRoot()
b.insert(0, "a")
b.insert(1, "b")
b.insert(0, "c")
b.insert(3, "d")
b.insert(0, "e")
b.insert(4, "p")
b.insert(0, "k")
b.insert(0, "l")
b.insert(4, "h")
b.insert(3, "o")
b.insert(3, "w")

print(b.listToArray())
AVLTreeList.print2d(b.getRoot())