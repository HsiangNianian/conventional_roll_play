from .parser import parse_text
from .renderer import Renderer

def main():
    text = input("Enter your text for parsing and rendering: ")
    ast = parse_text(text)
    renderer = Renderer(ast)
    rendered_text = renderer.render()
    print("Rendered Text:")
    print(rendered_text)

if __name__ == "__main__":
    main()
