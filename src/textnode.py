from enum import Enum


class TextType(Enum):
    PLAIN_TEXT = "Text"
    BOLD_TEXT = "Bold"
    ITALIC_TEXT = "Italic"
    CODE_TEXT = "Code"
    LINKS = "Link"
    IMAGES = "Image"


class TextNode:
    def __init__(self, text, text_type: TextType, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
