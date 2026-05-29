from textnode import TextNode, TextType


def main():
    x = TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev")
    print(x)


if __name__ == "__main__":
    main()
