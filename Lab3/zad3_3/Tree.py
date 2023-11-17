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

    @property
    def min_value(self):
        values = self.traverse()
        return min(values, key=lambda x: int(x))
    
# Przykład użycia
if __name__ == "__main__":
    my_tree = Tree("7")
    my_tree.add_child("2")
    my_tree.add_child("3")
    my_tree.children[0].add_child("4")
    my_tree.children[0].add_child("5")
    my_tree.children[1].add_child("6")

    print(my_tree)
    print(f"Najmniejsza wartość w drzewie: {my_tree.min_value}")