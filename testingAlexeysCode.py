class Tree:
    def __init__(self, name="TreeDefault"):
        self.name = name
        self.age = 0


class FruitTree(Tree):
    def __init__(self, name="FruitDefault"):
        self.stuff = None
        super(FruitTree, self).__init__(name)


if __name__ == '__main__':
    tree1 = Tree()
    fruit1 = FruitTree()

    print(tree1.name)
    print(fruit1.name)
