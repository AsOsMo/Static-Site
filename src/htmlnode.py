from multiprocessing import Value


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_result = ""
        if self.props != None:
            for i in iter(self.props):
                html_result += f" {i}={self.props[i]}"
        else:
            return html_result

    def __repr__(self):
        return f"{self.tag}\n {self.value}\n {self.children}\n {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value in Leaf Node")
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"{self.tag}\n {self.value}\n {self.props}"
