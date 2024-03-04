class Node:
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        raise NotImplementedError("Subclass must implement abstract method")

class RootNode(Node):
    def render(self):
        rendered_text = ""
        for child in self.children:
            rendered_text += child.render()
        return rendered_text

class ActNode(Node):
    def __init__(self, content):
        super().__init__()
        self.content = content

    def render(self):
        return f"<ACT>{self.content}</ACT>"

class CommentNode(Node):
    def __init__(self, content):
        super().__init__()
        self.content = content

    def render(self):
        return f"<COMMENT>{self.content}</COMMENT>"

class QuoteNode(Node):
    def __init__(self, content):
        super().__init__()
        self.content = content

    def render(self):
        return f"<QUOTE>{self.content}</QUOTE>"
