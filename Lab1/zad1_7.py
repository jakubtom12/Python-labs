class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_value):
        child = Tree(child_value)
        self.children.append(child)

    def traverse(self):
        result = [self.value]
        for child in self.children:
            result.extend(child.traverse())
        return result

    def __str__(self, level=0):
        ret = "\t" * level + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

# Przykład użycia
if __name__ == "__main__":
    my_tree = Tree("A")
    my_tree.add_child("B")
    my_tree.add_child("C")
    my_tree.children[0].add_child("D")
    my_tree.children[0].add_child("E")
    my_tree.children[1].add_child("F")

    print(my_tree)