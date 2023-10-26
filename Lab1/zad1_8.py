import unittest
from zad1_7 import Tree  # Importujemy klasę Tree z pliku tree.py

class TestTree(unittest.TestCase):
    def test_add_child(self):
        tree = Tree("A")
        tree.add_child("B")
        self.assertEqual(tree.children[0].value, "B")

    def test_traverse(self):
        tree = Tree("A")
        tree.add_child("B")
        tree.add_child("C")
        tree.children[0].add_child("D")
        tree.children[0].add_child("E")
        tree.children[1].add_child("F")

        result = tree.traverse()
        self.assertEqual(result, ["A", "B", "D", "E", "C", "F"])

    def test_str(self):
        tree = Tree("A")
        tree.add_child("B")
        tree.add_child("C")
        tree.children[0].add_child("D")
        tree.children[0].add_child("E")
        tree.children[1].add_child("F")

        tree_str = str(tree)
        expected_str = "A\n\tB\n\t\tD\n\t\tE\n\tC\n\t\tF\n"
        self.assertEqual(tree_str, expected_str)

if __name__ == '__main__':
    unittest.main()