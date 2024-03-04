import re

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def tokenize(self):
        tokens = []
        while self.pos < len(self.text):
            char = self.text[self.pos]

            if char == "#":
                self.pos += 1
                act_content = self._read_until_newline()
                tokens.append(Token("ACT", act_content))

            elif char in ["（", "("]:
                self.pos += 1
                comment_content = self._read_until_close_parenthesis(char)
                tokens.append(Token("COMMENT", comment_content))

            elif char in ['"', "“", "”"]:
                self.pos += 1
                quote_content = self._read_until_quote(char)
                tokens.append(Token("QUOTE", quote_content))

            else:
                self.pos += 1  # Skip irrelevant characters

        return tokens

    def _read_until_newline(self):
        start = self.pos
        while self.pos < len(self.text) and self.text[self.pos] != "\n":
            self.pos += 1
        return self.text[start:self.pos]

    def _read_until_close_parenthesis(self, open_parenthesis):
        close_parenthesis = "）" if open_parenthesis == "（" else ")"
        start = self.pos
        while self.pos < len(self.text) and self.text[self.pos] != close_parenthesis:
            self.pos += 1
        self.pos += 1  # Skip the close parenthesis
        return self.text[start:self.pos-1]

    def _read_until_quote(self, open_quote):
        close_quote = open_quote
        start = self.pos
        while self.pos < len(self.text) and self.text[self.pos] != close_quote:
            self.pos += 1
        self.pos += 1  # Skip the close quote
        return self.text[start:self.pos-1]
