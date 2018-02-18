"""To demonstrate how to break cyclic reference during destructions"""


class Circle:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.child = None

        if self.parent:
            parent.child = self

    def cleanup(self):
        self.child = self.parent = None

