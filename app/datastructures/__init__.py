"""
What is datastructure?
Answer:
 Data structures is a building blocks and raw material for any particular software programs.

  One can't become good programmer without good understanding of data structures.
"""


class Father:
    pass
    # def skills(self):
    #     print("Programming,Gardening")


class Mother:
    def skills(self):
        print("Cooking,Art")


class Child(Father,Mother):
    pass
    # def skills(self):
    #     print("sports")


child = Child()
child.skills()
