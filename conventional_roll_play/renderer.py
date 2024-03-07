from .ast_nodes import RootNode, ActNode, CommentNode, QuoteNode

class Renderer:
    def __init__(self, root):
        if not isinstance(root, RootNode):
            raise ValueError("Root must be an instance of RootNode")
        self.root = root

    def render(self):
        return self.root.render()

# Example usage
if __name__ == "__main__":
    # Assuming the AST has been built correctly and passed as `root_node`
    # This part is just for demonstration and will not work without the rest of the implementation
    root_node = RootNode()
    act_node = ActNode("This is an ACT")
    comment_node = CommentNode("This is a COMMENT")
    quote_node = QuoteNode("This is a QUOTE")

    root_node.add_child(act_node)
    root_node.add_child(comment_node)
    root_node.add_child(quote_node)

    renderer = Renderer(root_node)
    print(renderer.render())
