"""
Main Tree Structure:
  Nilupul (CEO)
    |__Chinmay (CTO)
        |__Vishwa (Infrastructure Head)
            |__Dhamal (Cloud Manager)
            |__Abhijit (App Manager)
        |__Aamir (Application Head)
    |__ Gels (HR Head)
        |__Peter (Recruitment Management)
        |__Waqas (Policy Manager)
"""

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        ancestor = self.parent
        while ancestor:
            level += 1
            ancestor = ancestor.parent
        return level

    def print_tree(self, level=0):
        if self.get_level() > level:
            return
        space = ' ' * self.get_level() * 3
        prefix = space + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for descentdant in self.children:
                descentdant.print_tree(level)


def creat_global_hirarchy():

    global_root = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))
    karnatak = TreeNode("Karnataka")
    karnatak.add_child(TreeNode("Bangalore"))
    karnatak.add_child(TreeNode("Mysore"))
    india.add_child(gujarat)
    india.add_child(karnatak)
    usa = TreeNode("USA")
    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))
    califonia = TreeNode("Califonia")
    califonia.add_child(TreeNode("San Francisco"))
    califonia.add_child(TreeNode("Mountain View"))
    califonia.add_child(TreeNode("Palo Alto"))
    usa.add_child(new_jersey)
    usa.add_child(califonia)
    global_root.add_child(india)
    global_root.add_child(usa)
    return global_root

if __name__ == "__main__":
    root = creat_global_hirarchy()
    root.print_tree(level=2)