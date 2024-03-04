from .lexer import Lexer, Token
from .ast_nodes import ActNode, CommentNode, QuoteNode, RootNode


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        root = RootNode()
        while self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            if token.type == "ACT":
                node = ActNode(token.value)
                root.add_child(node)
            elif token.type == "COMMENT":
                node = CommentNode(token.value)
                root.add_child(node)
            elif token.type == "QUOTE":
                node = QuoteNode(token.value)
                root.add_child(node)
            self.pos += 1
        return root


def parse_text(text):
    lexer = Lexer(text)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    return ast


if __name__ == "__main__":
    text = input("Enter your text: ")
    ast = parse_text(text)
    print(ast)
