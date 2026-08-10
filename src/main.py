from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode


def main():
    x = TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev")
    print(x)
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

    print(node)


if __name__ == "__main__":
    main()
