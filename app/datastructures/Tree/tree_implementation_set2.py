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
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, hirarchy_type="both"):
        space = ' ' * self.get_level() * 3
        prefix = space + '|__' if self.parent else ''
        if hirarchy_type == "name":
            print(prefix + self.name)
        elif hirarchy_type == "designation":
            print(prefix + self.designation)
        else:
            print(prefix + "{} ({})".format(self.name, self.designation) )
        if self.children:
            for descentdant in self.children:
                descentdant.print_tree(hirarchy_type)


def create_employee_hierarchy():

    ceo = TreeNode("Nilupul", "CEO") ##==> root node (level 0)
    cto = TreeNode("Chinmay", "CTO") ##==> level 1
    infrastructure_head = TreeNode("Vishwa", "Infrastructure Head") ##==> level 2
    infrastructure_head.add_child(TreeNode("Dhamal", "Cloud Manager")) ##==> level 3
    infrastructure_head.add_child(TreeNode("Abhijit", "App Manager")) ##==> level 3
    application_head = TreeNode("Aamir", "Application Head") ##==> level 2

    cto.add_child(infrastructure_head)
    cto.add_child(application_head)

    hr_head = TreeNode("Gels", "HR Head") ##==> level 1
    hr_head.add_child(TreeNode("Peter", "Recruitment Management")) ##==> level 2
    hr_head.add_child(TreeNode("Waqas", "Policy Manager")) ## level 2

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == "__main__":
    root = create_employee_hierarchy()
    root.print_tree(hirarchy_type="name")
    # root.print_tree(hirarchy_type="name")
    # root.print_tree(hirarchy_type="designation")